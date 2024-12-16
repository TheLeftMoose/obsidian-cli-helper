import os
import yaml

def get_md_files(scope):
    if os.path.isfile(scope) and scope.endswith('.md'):
        return [scope]
    return [os.path.join(scope, f) for f in os.listdir(scope) if f.endswith('.md')]

def get_image_files(md_file):
    folder = os.path.dirname(md_file)
    return [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith(('.png', '.jpg', '.jpeg'))]

def read_yaml_metadata(md_file):
    with open(md_file, 'r') as f:
        lines = f.readlines()
    yaml_lines = []
    in_yaml = False
    for line in lines:
        if line.strip() == '---':
            in_yaml = not in_yaml
            continue
        if in_yaml:
            yaml_lines.append(line)
    return yaml.safe_load(''.join(yaml_lines)) if yaml_lines else {}

def analyze_scope(scope):
    md_files = get_md_files(scope)
    image_files = []
    unprocessed_files = []

    for md_file in md_files:
        images = get_image_files(md_file)
        image_files.extend(images)
        metadata = read_yaml_metadata(md_file)
        if not metadata.get('processed', False):
            unprocessed_files.append(md_file)

    print(f"Total .md files: {len(md_files)}")
    print(f"Total image files: {len(image_files)}")
    print(f"Unprocessed .md files: {len(unprocessed_files)}")