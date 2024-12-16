import click
from .image_processing import crop_images
from .ocr import apply_ocr
from .metadata import update_metadata, analyze_scope, cleanup_images

@click.group()
def main():
    pass

@click.command()
@click.option('--scope', type=click.Path(exists=True), help='Specify the folder or .md files as the scope.')
def analyze(scope):
    """Reports scope details and processing status."""
    analyze_scope(scope)

@click.command()
@click.option('--scope', type=click.Path(exists=True), help='Specify the folder or .md files as the scope.')
def ocr(scope):
    """Processes unprocessed .md files and updates metadata."""
    crop_images(scope)
    apply_ocr(scope)
    update_metadata(scope)

@click.command()
@click.option('--scope', type=click.Path(exists=True), help='Specify the folder or .md files as the scope.')
def cleanup(scope):
    """Deletes original images after confirmation if all files are processed."""
    cleanup_images(scope)

main.add_command(analyze)
main.add_command(ocr)
main.add_command(cleanup)

if __name__ == "__main__":
    main()