import os
import subprocess
import openai
import argparse
from typing import List, Dict, Any, Optional
import json

class PRAssistant:
    """AI-powered Pull Request assistant."""

    def __init__(self, api_key: Optional[str] = None):
        """Initialize the PR assistant with OpenAI API key."""
        # Use provided key or get from environment
        self.api_key = api_key or os.environ.get("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OpenAI API key is required")

        self.client = openai.OpenAI(api_key=self.api_key)

    def get_git_diff(self, base_branch: str = "main") -> str:
        """Get the git diff between current branch and base branch."""
        try:
            # Get current branch name
            current_branch = subprocess.check_output(
                ["git", "rev-parse", "--abbrev-ref", "HEAD"],
                text=True
            ).strip()

            # Get the diff
            diff = subprocess.check_output(
                ["git", "diff", f"{base_branch}...{current_branch}"],
                text=True
            )

            return diff
        except subprocess.CalledProcessError as e:
            print(f"Error getting git diff: {e}")
            return ""

    def get_commit_messages(self, count: int = 10) -> List[str]:
        """Get recent commit messages."""
        try:
            commits = subprocess.check_output(
                ["git", "log", f"-{count}", "--pretty=format:%s"],
                text=True
            )
            return commits.splitlines()
        except subprocess.CalledProcessError as e:
            print(f"Error getting commit messages: {e}")
            return []

    def generate_pr_description(self,
                                base_branch: str = "main",
                                include_diff: bool = True) -> str:
        """Generate a comprehensive PR description."""
        # Get commit messages
        commits = self.get_commit_messages()
        commit_text = "\n".join([f"- {commit}" for commit in commits])

        # Get diff if requested
        diff_text = ""
        if include_diff:
            diff = self.get_git_diff(base_branch)
            # Truncate diff if too large
            if len(diff) > 10000:
                diff_text = diff[:10000] + "... [diff truncated for brevity]"
            else:
                diff_text = diff

        # Create prompt
        prompt = f"""
        Based on the following commits and code changes, generate a comprehensive
        pull request description:

        ## Recent Commits:
        {commit_text}

        ## Code Changes:
        ```diff
        {diff_text}
        ```

        Create a PR description with:
        1. A clear title summarizing the changes
        2. A detailed description of the changes made
        3. The problem being solved
        4. Implementation approach and reasoning
        5. Testing instructions
        6. Potential risks or areas for reviewer attention
        7. Related issues or tickets

        Format as Markdown.
        """

        # Generate description
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
            max_tokens=1500
        )

        return response.choices[0].message.content

    def analyze_code_changes(self, diff: Optional[str] = None) -> Dict[str, Any]:
        """Analyze code changes for potential issues."""
        if diff is None:
            diff = self.get_git_diff()

        # Truncate if needed
        if len(diff) > 12000:
            diff = diff[:12000] + "... [diff truncated for brevity]"

        prompt = f"""
        Analyze the following code diff for:
        1. Potential bugs or logic errors
        2. Security vulnerabilities
        3. Performance issues
        4. Code style violations
        5. Missing error handling
        6. Test coverage gaps

        Provide a JSON response with these categories and specific issues found:

        ```diff
        {diff}
        ```

        Format response as valid JSON with these keys:
        "bugs", "security", "performance", "style", "error_handling", "test_coverage"

        Each key should contain an array of found issues with "file", "line" (if applicable),
        "description", and "severity" (high/medium/low).
        """

        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.1,
            max_tokens=2000,
            response_format={"type": "json_object"}
        )

        try:
            return json.loads(response.choices[0].message.content)
        except json.JSONDecodeError:
            # Fallback if not valid JSON
            return {
                "error": "Could not parse response as JSON",
                "raw_response": response.choices[0].message.content
            }

    def suggest_test_cases(self, file_path: str) -> List[Dict[str, Any]]:
        """Suggest test cases for the given file."""
        try:
            with open(file_path, 'r') as f:
                code = f.read()

            prompt = f"""
            For the following code, suggest comprehensive test cases:

            ```python
            {code}
            ```

            For each function or class, provide:
            1. Test case name
            2. Input values
            3. Expected output or behavior
            4. Edge cases to consider

            Return as a JSON array of test case objects.
            """

            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.2,
                max_tokens=2000,
                response_format={"type": "json_object"}
            )

            try:
                return json.loads(response.choices[0].message.content)["test_cases"]
            except (json.JSONDecodeError, KeyError):
                return [{"error": "Could not parse test cases from response"}]

        except Exception as e:
            return [{"error": f"Error processing file: {str(e)}"}]

    def generate_release_notes(self) -> str:
        """Generate release notes based on recent commits."""
        commits = self.get_commit_messages(count=50)
        commit_text = "\n".join([f"- {commit}" for commit in commits])

        prompt = f"""
        Based on these recent commits, generate comprehensive release notes:

        {commit_text}

        Group changes into categories:
        - New Features
        - Improvements
        - Bug Fixes
        - Breaking Changes
        - Documentation

        Format as Markdown with version heading and categories as subheadings.
        Only include categories that have relevant changes.
        """

        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            max_tokens=1000
        )

        return response.choices[0].message.content

# Example CLI usage
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AI-powered PR assistant")
    parser.add_argument("--action", choices=["pr-description", "analyze", "tests", "release-notes"],
                        required=True, help="Action to perform")
    parser.add_argument("--base", default="main", help="Base branch for comparison")
    parser.add_argument("--file", help="File path for test case generation")

    args = parser.parse_args()

    pr_assistant = PRAssistant()

    if args.action == "pr-description":
        description = pr_assistant.generate_pr_description(args.base)
        print(description)

    elif args.action == "analyze":
        analysis = pr_assistant.analyze_code_changes()
        print(json.dumps(analysis, indent=2))

    elif args.action == "tests":
        if not args.file:
            print("Error: --file is required for test case generation")
        else:
            test_cases = pr_assistant.suggest_test_cases(args.file)
            print(json.dumps(test_cases, indent=2))

    elif args.action == "release-notes":
        notes = pr_assistant.generate_release_notes()
        print(notes)