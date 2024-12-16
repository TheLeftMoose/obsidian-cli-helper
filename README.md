# Obsidian Pipeline CLI

This project provides a CLI tool to process markdown files and images in an Obsidian.md vault.

## Setup

1. **Clone the repository**:

   ```sh
   `git clone <repository-url>`
   `cd <repository-directory>`
   ```

2. **Create a virtual environment**:
   `python3 -m venv venv`

3. **Activate the virtual environment**:
   - On Linux/macOS:
     `source venv/bin/activate`
   - On Windows:
     `.\venv\Scripts\activate`

4. **Install the package and its dependencies**:
   `pip install -e .`

## Usage

### Analyze

Reports scope details and processing status.

`obsidian-pp analyze --scope /path/to/vault`

### OCR

Processes unprocessed .md files and updates metadata.

`obsidian-pp ocr --scope /path/to/vault`

### Cleanup

Deletes original images after confirmation if all files are processed.

`obsidian-pp cleanup --scope /path/to/vault`

## Development

### Development workflow

Find good documentation in the specific documentation page:

[development workflow](./docs/development-workflow.md)

### Running Tests

To run the tests, use the following command:

`pytest tests/`

### Adding Dependencies

To add new dependencies, update the [requirements.txt](http://_vscodecontentref_/1) file and then run:

`pip install -r requirements.txt`

### Updating the Package

If you make changes to the package, you can reinstall it using:

`pip install -e .`

## Contributing

Feel free to open issues or submit pull requests if you have any improvements or bug fixes.

## License

This project is licensed under the MIT License.