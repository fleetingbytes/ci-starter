from collections.abc import Mapping
from pathlib import Path
from sys import version_info
from typing import TYPE_CHECKING, TextIO

from ruamel.yaml import YAML as Yaml

from ci_starter.step import Step

if TYPE_CHECKING:
    from importlib.resources.abc import Traversable

OLD_PYTHON_MINOR_VERSION = 11

if version_info.minor == OLD_PYTHON_MINOR_VERSION:
    from importlib_resources import files
else:
    from importlib.resources import files


def get_asset(path: str) -> str:
    path = Path(path)
    asset: Traversable = files(f"{__package__}.assets")
    for path_segment in path.parts:
        asset = asset.joinpath(path_segment)
    result: str = asset.read_text(encoding="utf-8")
    return result


def step_yaml() -> Yaml:
    yaml = Yaml()
    yaml.width = 150
    yaml.preserve_quotes = True
    yaml.sequence_indent = 4
    yaml.sequence_dash_offset = 2
    yaml.register_class(Step)
    return yaml


def from_yaml(s: str) -> dict:
    yaml = step_yaml()
    obj = yaml.load(s)
    return obj


def dump(obj: Mapping, filelike: TextIO) -> None:
    yaml = step_yaml()
    yaml.dump(obj, filelike)
