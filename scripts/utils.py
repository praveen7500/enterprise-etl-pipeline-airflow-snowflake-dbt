import yaml

def load_yaml(file):

    with open(file) as f:
        return yaml.safe_load(f)
