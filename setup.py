from setuptools import setup, find_packages

def parse_requirements(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file if line and not line.startswith('#')]

setup(
    name="obsidian_cli_helper",
    version="0.1.0",  # This line will be updated by python-semantic-release
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=parse_requirements('requirements.txt'),
    entry_points={
        "console_scripts": [
            "obsidian-cli-helper=cli:main",
        ],
    },
)