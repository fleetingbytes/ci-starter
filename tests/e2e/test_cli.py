from click.testing import CliRunner, Result

from ci_starter.cli import cli
from tests.e2e.constants import CI_STARTER_VERSION


def test_version(cli_runner: CliRunner) -> None:
    result: Result = cli_runner.invoke(cli, ["--version"])
    assert result.stdout.strip().endswith(CI_STARTER_VERSION)


def test_help(cli_runner: CliRunner) -> None:
    result: Result = cli_runner.invoke(cli, ["--help"])
    assert result.stdout.startswith("Usage")
    assert result.stdout.strip().endswith("workflows")
