from pathlib import Path

from ruamel.yaml import YAML as Yaml


def from_yaml(s: str) -> tuple[dict, Path]:
    yaml = Yaml()
    yaml.load(s)
    return yaml
