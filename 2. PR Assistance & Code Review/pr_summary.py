import os
import json
import requests
import openai

# Configuration
PR_NUMBER = os.environ.get("PR_NUMBER")
REPO = os.environ.get("REPO")
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# Initialize OpenAI client
openai.api_key = OPENAI_API_KEY
client = openai.OpenAI()

def get_pr_details():
    """Get PR details from GitHub API."""
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"token {GITHUB_TOKEN}",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    url = f"https://api.github.com/repos/{REPO}/pulls/{PR_NUMBER}"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def get_pr_files():
    """Get files changed in PR from GitHub API."""
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"token {GITHUB_TOKEN}",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    url = f"https://api.github.com/repos/{REPO}/pulls/{PR_NUMBER}/files"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def generate_summary(pr_details, pr_files):
    """Generate PR summary using OpenAI."""
    # Extract PR information
    title = pr_details.get("title", "")
    description = pr_details.get("body", "")

    # Prepare files information
    files_info = []
    for file in pr_files:
        files_info.append({
            "filename": file.get("filename"),
            "status": file.get("status"),
            "additions": file.get("additions"),
            "deletions": file.get("deletions"),
        })

    # Create prompt
    prompt = f"""
    Generate a concise but comprehensive summary of this pull request:

    PR Title: {title}

    PR Description:
    {description if description else "No description provided"}

    Files changed:
    {json.dumps(files_info, indent=2)}

    Your summary should include:
    1. What changes were made (core functionality, bug fixes, features, etc.)
    2. The primary affected components or areas of the codebase
    3. Potential impact on the system
    4. Testing considerations

    Format the response as Markdown.
    """

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
        max_tokens=1000
    )

    return response.choices[0].message.content

def main():
    """Main function to generate PR summary."""
    # Get PR information
    pr_details = get_pr_details()
    pr_files = get_pr_files()

    # Generate summary
    summary = generate_summary(pr_details, pr_files)

    # Save summary to file
    with open("pr_summary.md", "w") as f:
        f.write(summary)

    print("PR summary generated")

if __name__ == "__main__":
    main()
