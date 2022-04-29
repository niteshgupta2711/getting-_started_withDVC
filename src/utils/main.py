import yaml,os
def read_yaml(path: str) -> dict:
    with open('path') as yamlfile:
        content=yaml.safe_load(yamlfile)
    return content
def make_dirs(join_path: list):
    for dir in join_path:
        os.makedirs(dir)