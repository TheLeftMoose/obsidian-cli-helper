# Development Workflow

## Clone the Repository
- Clone the repository to your local machine.
- Navigate into the project directory.

  git clone <repository-url>
  cd <repository-directory>

## Set Up the Development Environment
- Create a virtual environment.
- Activate the virtual environment.
- Install the package and its dependencies.

  python3 -m venv venv
  source venv/bin/activate  # On Windows: .\venv\Scripts\activate
  pip install -e .

## Make Changes
- Create a new branch for your feature or bug fix.
- Make your changes in the codebase.

  git checkout -b feature/my-new-feature

## Run Tests
- Run the tests to ensure your changes do not break existing functionality.

  pytest tests/

## Commit and Push Changes

- Use conventional commit messages to trigger version bumps:
  - `fix: description` for patch releases
  - `feat: description` for minor releases
  - `BREAKING CHANGE: description` for major releases

- Add and commit your changes.
- Push your branch to the remote repository.

  git add .
  git commit -m "feat: Add new feature"
  git push origin feature/my-new-feature

## Create a Pull Request

- Go to the repository on GitHub.
- Create a pull request from your branch to the main branch.
- Provide a description of your changes and request a review.

## Review and Merge
- Address any feedback from code reviews.
- Once approved, merge the pull request into the main branch.

## Cleanup
- Delete the branch after merging.
- Pull the latest changes from the main branch.

  git checkout main
  git pull origin main
  git branch -d feature/my-new-feature

## Example Workflow

### Clone the Repository

  git clone https://github.com/TheLeftMoose/obsidian-cli-helper.git
  cd obsidian-cli-helper

### Set Up the Development Environment

  python3 -m venv venv
  source venv/bin/activate
  pip install -e .

### Create a New Branch

  git checkout -b feature/add-ocr-support

### Make Changes

- Edit `src/ocr.py` to add new OCR functionality.

### Run Tests

  pytest tests/

### Commit and Push Changes

- Use a conventional commit message to trigger a version bump:
  - `feat: Add OCR support for new image format`

  git add src/ocr.py
  git commit -m "feat: Add OCR support for new image format"
  git push origin feature/add-ocr-support

### Create a Pull Request

- Go to GitHub and create a pull request from `feature/add-ocr-support` to `main`.

### Review and Merge

- Address any feedback.
- Merge the pull request once approved.

### Cleanup

  git checkout main
  git pull origin main
  git branch -d feature/add-ocr-support

By following this workflow, you ensure that your development process is organized, and your code changes are properly reviewed and integrated into the main branch.