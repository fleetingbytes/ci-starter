from click.testing import CliRunner, Result
from pytest import mark

from ci_starter.cli import cli
from tests.e2e.constants import SUCCESSFUL_RETURN_CODE


@mark.usefixtures("set_remote_url")
def test_helper_script_created(
    cli_runner: CliRunner, test_project_path_str: str, helper_script: str
) -> None:
    expected_script, path = helper_script

    result: Result = cli_runner.invoke(cli, ["-C", test_project_path_str])
    assert result.exit_code == SUCCESSFUL_RETURN_CODE

    actual_script = path.read_text(encoding="utf-8")
    assert expected_script == actual_script
