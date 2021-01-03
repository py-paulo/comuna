import yaml
import pathlib

CONFIG_BASE_DIR = pathlib.Path(__file__).parent.parent

config_path = CONFIG_BASE_DIR / 'config' / 'config.yaml'

def get_config(path) -> dict:
    try:
        with open(path) as f:
            config_yaml = yaml.safe_load(f)
        return config_yaml
    except FileNotFoundError:
        return {}

config = get_config(config_path)