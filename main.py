import os
from github import Github

from utility import *

def main():
    # Initialize GitHub API with token
    g = Github(os.getenv('GITHUB_TOKEN'))

    # Get the repo path and PR number from the environment variables
    repo_path = os.getenv('REPO_PATH')
    pull_request_number = int(os.getenv('PR_NUMBER'))
    pull_request_branch_name = os.getenv('PR_BRANCH_NAME')
    
    # Get the repo object
    repo = g.get_repo(repo_path)

    # Fetch README content (assuming README.md)
    readme_content = repo.get_contents("README.md")
    
    # print(readme_content)
    # Fetch pull request by number
    pull_request = repo.get_pull(pull_request_number)

    # Get the diffs of the pull request
    pull_request_diffs = [
        {
            "filename": file.filename,
            "patch": file.patch 
        } 
        for file in pull_request.get_files()
    ]
    
    # Get the commit messages associated with the pull request
    commit_messages = [commit.commit.message for commit in pull_request.get_commits()]

    # Format data for OpenAI prompt
    prompt_readme, prompt_review = format_data_for_openai(pull_request_diffs, readme_content, commit_messages)

    # Check if the last commit message is not an automated update
    if commit_messages[-1] != "AI COMMIT: Proposed README update based on recent code changes.":
        # Check if the only changed file is README.md
        if not all(file['filename'] == 'README.md' for file in pull_request_diffs):
            # Add code review comments
            comment_body = call_openai(prompt_review, True)
            add_code_review_comment(repo, pull_request_number, comment_body)

            # Create new commit for the README update
            updated_readme = call_openai(prompt_readme, False)
            update_readme_in_existing_pr(repo, updated_readme, pull_request_branch_name)
            # dummy commit to trigger the workflow
            
if __name__ == '__main__':
    main()
