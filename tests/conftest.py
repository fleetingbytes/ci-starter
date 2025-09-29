from pytest import fixture
from ruamel.yaml import YAML as Yaml

from ci_starter.step import Step


@fixture
def yaml_parser() -> Yaml:
    return Yaml()


@fixture
def step_parser(yaml_parser) -> Yaml:
    yaml_parser.register_class(Step)
    return yaml_parser
