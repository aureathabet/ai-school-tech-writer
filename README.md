## Code Review

### Overview
The changes in this pull request significantly improve the automation workflow for updating the README and performing code reviews. The enhancements include broader trigger conditions, better handling of environment variables, and new utility functions to support future automation features. The commits are well-documented, and the updated README provides a clear and comprehensive overview of the project's setup, usage, and features.

### Workflow File Changes (`.github/workflows/update_readme.yaml`)

1. **Trigger Events**:
   - The workflow now also triggers on `synchronize` and `reopened` events, broadening the scope for automation. This ensures the workflow runs in more scenarios where pull requests are updated.

2. **Job Execution Condition**:
   - The job now runs if the pull request is not merged (`github.event.pull_request.merged == false`). This change ensures that README updates and code reviews are performed before merging, which is typically when they are most needed.

3. **Environment Variables**:
   - Added `PR_BRANCH_NAME` to the list of environment variables. This allows the automation scripts to know the branch name of the pull request, which is useful for updating the README in the correct branch.

### Main Script Changes (`main.py`)

1. **Environment Variable Extraction**:
   - The script now extracts the `PR_BRANCH_NAME` from the environment variables, allowing it to know the branch name of the pull request.

2. **Conditional Code Review**:
   - The script now checks if the only changed file is `README.md`. If so, it skips adding code review comments to avoid unnecessary comments when only the README is updated.

3. **README Update**:
   - The `update_readme_in_existing_pr` function now uses the `PR_BRANCH_NAME` to update the README directly in the existing PR branch.

### Utility Script Changes (`utility.py`)

1. **Review Prompt**:
   - The review prompt was updated to exclude README update suggestions. This helps in focusing the review comments on actual code changes.

2. **Update README Function**:
   - The `update_readme_in_existing_pr` function was modified to dynamically fetch the latest `README.md` SHA from the PR branch. This ensures the script is always working with the latest version of the file.

3. **New Functions**:
   - `get_pr_labels`: Retrieves labels associated with a PR.
   - `merge_pull_request`: Merges a specified PR using the chosen method (merge, squash, or rebase).
   - `notify_user_for_merge`: Notifies the user when the PR is ready to be merged.

### Commit Messages

- The commit messages are clear and descriptive, reflecting the changes made in the code. They include additions and updates to the workflow, new functions for future automation features, and fine-tuning of prompts and conditions.

## Updated README Content

```markdown
# AI-School Tech Writer

## Overview

This repository contains automated tools and workflows to assist in generating and updating README files based on code changes and commit messages.

## Features

- **Automated README Updates**: Automatically updates the README file when a pull request is opened, edited, or synchronized.
- **Automated Code Review**: Uses OpenAI to perform basic code reviews and leave comments on pull requests.
- **Pull Request Labels**: Retrieves and processes labels associated with pull requests.
- **Automated Merge Notifications**: Notifies users when a pull request is ready to be merged after automated checks.

## Workflow

The `.github/workflows/update_readme.yaml` file defines a GitHub Actions workflow that triggers on various pull request events such as opened, edited, ready_for_review, synchronize, and reopened.

### Key Changes in Workflow

- **Trigger Events**: The workflow now triggers on `synchronize` and `reopened` events in addition to the existing ones.
- **Job Execution Condition**: The job now runs if the pull request is not merged (`github.event.pull_request.merged == false`).
- **Environment Variables**: Extracts additional environment variables like PR branch name (`PR_BRANCH_NAME`).

### Key Functions and Scripts

- **main.py**: 
  - Extracts repository path, PR number, and branch name from environment variables.
  - Performs code review and updates the README in the existing PR branch.

- **utility.py**:
  - `format_data_for_openai()`: Formats data for OpenAI with a prompt that excludes README update suggestions.
  - `update_readme_in_existing_pr()`: Updates the README file in the existing PR branch.
  - `get_pr_labels()`: Retrieves labels associated with a PR.
  - `merge_pull_request()`: Merges a specified PR using a specified method (merge, squash, or rebase).
  - `notify_user_for_merge()`: Notifies the user when the PR is ready to be merged.

## Setup

### Prerequisites

- Python 3.11
- GitHub Personal Access Token with repository permissions

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/aureathabet/ai-school-tech-writer.git
   cd ai-school-tech-writer
   ```

2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   - `GITHUB_TOKEN`: Your GitHub personal access token.
   - `REPO_PATH`: The repository path (e.g., `username/repo`).
   - `PR_NUMBER`: The pull request number.
   - `PR_BRANCH_NAME`: The pull request branch name.
   - `COMMIT_SHA`: The commit SHA.

### Usage

Run the main script to trigger the automated README update and code review:
```sh
python main.py
```

## Contributing

We welcome contributions! Please read our [CONTRIBUTING](CONTRIBUTING.md) guidelines before submitting a pull request.

---

This updated README provides a clear overview of the new workflow, functions, and setup instructions, while maintaining the existing style and clarity. If you need further adjustments or additional sections, please let me know!
```

## Summary

The code changes introduce new functionalities and improve the existing workflow for automated README updates and code reviews. The updated README accurately reflects these changes, providing clear instructions on setup, usage, and new features. The commit messages are well-documented and align with the changes made in the code.