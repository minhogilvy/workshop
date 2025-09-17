import os
import json
import requests
import openai
from typing import Dict, List, Any

# Configuration
PR_NUMBER = os.environ.get("PR_NUMBER")
REPO = os.environ.get("REPO")
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# Initialize OpenAI client
openai.api_key = OPENAI_API_KEY
client = openai.OpenAI()

def get_pr_diff() -> str:
    """Get the PR diff from GitHub API."""
    headers = {
        "Accept": "application/vnd.github.v3.diff",
        "Authorization": f"token {GITHUB_TOKEN}",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    url = f"https://api.github.com/repos/{REPO}/pulls/{PR_NUMBER}"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.text

def analyze_code_changes(diff: str) -> Dict[str, Any]:
    """Analyze code changes using OpenAI API."""
    # Truncate diff if too large
    if len(diff) > 10000:
        diff = diff[:10000] + "\n...[diff truncated due to size]"

    prompt = f"""
    Analyze this PR diff for potential issues and improvement suggestions:

    ```diff
    {diff}
    ```

    Provide a detailed analysis including:
    1. Potential bugs or logic errors
    2. Security vulnerabilities
    3. Performance issues
    4. Code style violations
    5. Missing tests or documentation

    Format response as JSON with these keys:
    - "issues": Array of issue objects with "category", "severity", "description", "file" (if applicable), and "suggestion"
    - "suggestions": Array of suggestion objects with "title" and "description"

    Only include substantive issues and suggestions.
    """

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.1,
        response_format={"type": "json_object"}
    )

    try:
        return json.loads(response.choices[0].message.content)
    except json.JSONDecodeError:
        return {
            "error": "Failed to parse response",
            "issues": [],
            "suggestions": []
        }

def main():
    """Main function to analyze PR and save results."""
    # Get PR diff
    diff = get_pr_diff()

    # Analyze code changes
    analysis = analyze_code_changes(diff)

    # Save analysis to file
    with open("pr_analysis.json", "w") as f:
        json.dump(analysis, f, indent=2)

    print("PR analysis complete")

if __name__ == "__main__":
    main()
