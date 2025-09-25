from pytest import fixture
from ruamel.yaml import YAML as Yaml

from ci_starter.action import Action
from ci_starter.step import Step


@fixture
def yaml_parser() -> Yaml:
    return Yaml()


@fixture
def action_parser(yaml_parser) -> Yaml:
    yaml_parser.register_class(Action)
    return yaml_parser


@fixture
def step_parser(action_parser) -> Yaml:
    action_parser.register_class(Step)
    return action_parser
