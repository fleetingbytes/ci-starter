from collections.abc import Iterable

from click.testing import CliRunner, Result
from pytest import mark, param

from ci_starter.cli import cli
from tests.e2e.constants import CI_STARTER_VERSION


@mark.parametrize(
    "subcommand, option, start, end",
    (
        param((), ("--version",), "ci-start", CI_STARTER_VERSION, id="version"),
        param((), ("--help",), "Usage", "workflows", id="help"),
        param(("psr-config",), ("--help",), "Usage", "exit.", id="psr-config"),
        param(("workflows",), ("--help",), "Usage", "exit.", id="workflows"),
    ),
)
def test_cli(
    cli_runner: CliRunner, subcommand: Iterable[str], option: Iterable[str], start: str, end: str
) -> None:
    result: Result = cli_runner.invoke(cli, subcommand + option)
    assert result.stdout.startswith(start)
    assert result.stdout.strip().endswith(end)
