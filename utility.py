import os
import base64
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers.string import StrOutputParser
from langsmith.wrappers import wrap_openai
from langsmith import traceable
from constants import MODEL, SYSTEM_PROMPT

def format_data_for_openai(diffs, readme_content, commit_messages):
    prompt = None

    # Combine the changes into a string with clear delineation.
    changes = '\n'.join([f"File: {diff['filename']}\n{diff['patch']}" for diff in diffs])

    # Combine all commit messages
    commit_messages = '\n'.join(commit_messages)

    # Decode the README content
    readme_content = base64.b64decode(readme_content.content).decode('utf-8')

    # Construct the prompt with clear instructions for the LLM.
    base_prompt = (
        "Please review the following code changes and commit messages from a GitHub pull request:\n"
        "Code changes from Pull Request:\n"
        f"{changes}\n"
        "Commit messages:\n"
        f"{commit_messages}"
        "Here is the current README file content:\n"
        f"{readme_content}\n"
    )

    prompt_readme = (
        f"{base_prompt}"
        "Consider the code changes and commit messages, and determine if the README needs to be updated. If so, edit the README, ensuring to maintain its existing style and clarity. Do not perform a code review.\n"
        "Updated README:\n"
    )

    prompt_review = (
        f"{base_prompt}"
        "Consider the code changes and commit messages, and perform a basic code review. If you have any questions or suggested improvements, please leave a concise comment on the pull request. Never include suggestions for updating the README.\n"
        "Code Review Comments:\n"
    )

    return prompt_readme, prompt_review

def call_openai(prompt):
    client = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"), model=MODEL)

    try:
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ]

        response = client.invoke(input=messages)
        parser = StrOutputParser()
        return parser.invoke(input=response)
    except Exception as e:
        print(f"Error making LLM: {e}")
        return "An error occurred while processing the request. Please try again later."
    
def update_readme_in_existing_pr(repo, updated_readme, pr_branch_name):
    commit_message = "AI COMMIT: Proposed README update based on recent code changes."

    # Fetch the latest README.md file to get the current SHA
    contents = repo.get_contents("README.md", ref=pr_branch_name)
    current_sha = contents.sha

    # Update the README.md file directly in the existing PR branch
    repo.update_file("README.md", commit_message, updated_readme, current_sha, pr_branch_name)

def add_code_review_comment(repo, pr_number, comment_body):
    """
    Adds a code review comment to a specified pull request.

    Args:
    repo (Repository): The repository object from the GitHub API.
    pr_number (int): The number of the pull request to which the comment will be added.
    comment_body (str): The content of the comment to be added.
    """
    pull_request = repo.get_pull(pr_number)
    pull_request.create_issue_comment(comment_body)

def get_pr_labels(repo, pr_number):
    """
    Retrieves the labels associated with a specified pull request.

    Args:
    repo (Repository): The repository object from the GitHub API.
    pr_number (int): The number of the pull request from which to retrieve labels.

    Returns:
    list: A list of label names associated with the pull request.
    """
    pull_request = repo.get_pull(pr_number)
    return [label.name for label in pull_request.labels]

def merge_pull_request(repo, pr_number, commit_title, commit_message, merge_method='merge'):
    """
    Merges a specified pull request.

    Args:
    repo (Repository): The repository object from the GitHub API.
    pr_number (int): The number of the pull request to merge.
    commit_title (str): The title for the commit message.
    commit_message (str): The detailed commit message.
    merge_method (str): The method of merging (merge, squash, or rebase).

    Returns:
    bool: True if the merge was successful, False otherwise.
    """
    try:
        pull_request = repo.get_pull(pr_number)
        pull_request.merge(commit_title=commit_title, commit_message=commit_message, merge_method=merge_method)
        return True
    except Exception as e:
        print(f"Failed to merge PR: {e}")
        return False
    


def notify_user_for_merge(repo, pr_number, user_login):
    """
    Notifies the GitHub user when the action has been completed and the PR is ready to be merged.

    Args:
    repo (Repository): The repository object from the GitHub API.
    pr_number (int): The number of the pull request.
    user_login (str): The GitHub login of the user to notify.
    """
    issue = repo.get_issue(pr_number)
    notification_message = f"@{user_login}, the automated checks are complete and the PR is ready to be merged. Please review the changes."
    issue.create_comment(notification_message)

