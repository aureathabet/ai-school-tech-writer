## Code Review Summary

### Workflow File Changes (`.github/workflows/update_readme.yaml`)
1. **Trigger Events**:
   - Added `synchronize` and `reopened` events to trigger the workflow.
2. **Job Execution Condition**:
   - Changed the condition to run the job if the pull request is not merged (`github.event.pull_request.merged == false`).
3. **Environment Variables**:
   - Added `PR_BRANCH_NAME` to the list of environment variables passed to the Python script.

### Main Script Changes (`main.py`)
1. **Environment Variable Extraction**:
   - Added extraction of `PR_BRANCH_NAME`.
2. **Conditional Code Review**:
   - Added condition to check if the only changed file is `README.md`. If not, perform the code review and update the README in the existing PR branch.

### Utility Script Changes (`utility.py`)
1. **Review Prompt**:
   - Updated the review prompt to exclude README update suggestions.
2. **Update README Function**:
   - Modified `update_readme_in_existing_pr` to dynamically fetch the latest `README.md` SHA from the PR branch.
3. **New Functions**:
   - Added `get_pr_labels` to retrieve labels associated with a PR.
   - Added `merge_pull_request` to merge a specified PR.
   - Added `notify_user_for_merge` to notify the user when the PR is ready to be merged.

### Commit Messages
- The commit messages are clear and reflect the changes made in the code. They include additions and updates to the workflow, new functions for future automation features, and fine-tuning of prompts and conditions.

---

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