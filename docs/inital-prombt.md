# Obsidian CLI helper

## Project Overview

I have an Obsidian.md vault containing markdown files and session-related images of PowerPoint presentations from events like reInvent 2024. I want a Python script using `click` for a custom CLI to handle the following pipeline:

### Requirements:

1. **Scope Selection**:
   - The script should allow specifying a folder (or .md files) as the scope.
   - For .md file scope:
     - Retain links to the respective files throughout the pipeline.
     - Use the YAML metadata section (--- block at the top of the file) to track processing status with a flag like `processed: true/false`.

2. **Image Cropping**:
   - Crop session-related images to show only slides (do not resize yet, to preserve resolution for OCR).

3. **OCR Integration**:
   - Apply OCR to cropped images to extract text.
   - Save the extracted text inline in the original .md notes alongside the images in markdown format.
   - Preserve existing handwritten notes in the .md files and organize the OCR text and slide image together within the same note.

4. **Metadata Management**:
   - Add or update a `processed` flag in the YAML metadata section of the .md files:
     - `processed: false` for unprocessed files.
     - Update to `processed: true` after successful OCR.

5. **Interactive Workflow**:
   - When run with the `--scope` option:
     - Report how many .md files and image files are in scope.
     - Indicate how many .md files still need OCR processing.
   - Ask for confirmation before proceeding with OCR.
   - If all files are processed, ask for confirmation before optionally cleaning up (e.g., deleting original images).

6. **Cleanup**:
   - Include a cleanup step to optionally delete original, large-size image files after processing is confirmed as complete.

7. **YAML Metadata Integration**:
   - Use the YAML metadata in the .md files as the single source of truth for tracking the processing state.
   - If no metadata exists, initialize it with the required `processed: false` flag.

### Key Features:

- Use `click` for CLI interactivity and command structure.
- Include commands like:
  - `analyze`: Reports scope details and processing status.
  - `ocr`: Processes unprocessed .md files and updates metadata.
  - `cleanup`: Deletes original images after confirmation if all files are processed.
- Handle re-running the pipeline by skipping files already marked as `processed: true`.

### Workflow Example:

1. Run `analyze` to determine scope and status.
2. Run `ocr` to process unprocessed files, extract text, and update metadata.
3. Optionally, run `cleanup` to delete original images after processing.

### Development Workflow:

1. **Clone the Repository**:
   - Clone the repository to your local machine.
   - Navigate into the project directory.

     git clone <repository-url>
     cd <repository-directory>

2. **Set Up the Development Environment**:
   - Create a virtual environment.
   - Activate the virtual environment.
   - Install the package and its dependencies.

     python3 -m venv venv
     source venv/bin/activate  # On Windows: .\venv\Scripts\activate
     pip install -e .

3. **Make Changes**:
   - Create a new branch for your feature or bug fix.
   - Make your changes in the codebase.

     git checkout -b feature/my-new-feature

4. **Run Tests**:
   - Run the tests to ensure your changes do not break existing functionality.

     pytest tests/

5. **Commit and Push Changes**:
   - Use conventional commit messages to trigger version bumps:
     - `fix: description` for patch releases
     - `feat: description` for minor releases
     - `BREAKING CHANGE: description` for major releases

   - Add and commit your changes.
   - Push your branch to the remote repository.

     git add .
     git commit -m "feat: Add new feature"
     git push origin feature/my-new-feature

6. **Create a Pull Request**:
   - Go to the repository on GitHub.
   - Create a pull request from your branch to the main branch.
   - Provide a description of your changes and request a review.

7. **Review and Merge**:
   - Address any feedback from code reviews.
   - Once approved, merge the pull request into the main branch.

8. **Cleanup**:
   - Delete the branch after merging.
   - Pull the latest changes from the main branch.

     git checkout main
     git pull origin main
     git branch -d feature/my-new-feature

### Using `python-semantic-release`:

1. **Install `python-semantic-release`**:
   pip install python-semantic-release

2. **Configure `python-semantic-release`**:
   Create a `.releaserc` file in the root of your project with the following content:

   {
     "branch": "main",
     "version_variable": "setup.py:version",
     "upload_to_pypi": false
   }

3. **Set Up GitHub Actions**:
   Create a GitHub Actions workflow file to automate the release process.

   **.github/workflows/release.yml**:
   name: Release

   on:
     push:
       branches:
         - main

   jobs:
     release:
       runs-on: ubuntu-latest

       steps:
         - name: Checkout code
           uses: actions/checkout@v3

         - name: Set up Python
           uses: actions/setup-python@v4
           with:
             python-version: '3.9'

         - name: Install dependencies
           run: |
             python -m pip install --upgrade pip
             pip install python-semantic-release

         - name: Run semantic release
           env:
             GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
           run: semantic-release publish

By following this prompt, you can develop a comprehensive CLI tool for processing markdown files and images in an Obsidian.md vault, with a well-defined development workflow and automated versioning and release process.