Based on the code changes and commit messages provided in the GitHub pull request, the README needs to be updated to reflect the new automation workflow, additional functions, and any new dependencies or environment variables used. Here's an updated version of the README:

---

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