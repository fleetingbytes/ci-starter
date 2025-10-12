from pathlib import Path
from stat import S_IXGRP as EXECUTABLE_FOR_GROUP
from stat import S_IXOTH as EXECUTABLE_FOR_OTHERS
from stat import S_IXUSR as EXECUTABLE_FOR_USER

from click.testing import CliRunner, Result

from ci_starter.cli import cli
from ci_starter.constants import HELPER_SCRIPT_FILE_PATH
from tests.e2e.constants import SUCCESSFUL_RETURN_CODE


def is_executable(path: Path) -> bool:
    mode = path.stat().st_mode
    return all((mode | EXECUTABLE_FOR_USER, mode | EXECUTABLE_FOR_GROUP, mode | EXECUTABLE_FOR_OTHERS))


def test_helper_script_is_executable(test_project_path_str: str, cli_runner: CliRunner):
    result: Result = cli_runner.invoke(cli, ["-C", test_project_path_str, "workflows"])
    assert result.exit_code == SUCCESSFUL_RETURN_CODE

    script = Path(test_project_path_str, HELPER_SCRIPT_FILE_PATH)

    assert is_executable(script)
