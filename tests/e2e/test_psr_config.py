from pathlib import Path
from tomllib import load

from click.testing import CliRunner, Result
from pytest import mark

from ci_starter.cli import cli
from ci_starter.errors import RemoteNotFoundError
from tests.e2e.constants import (
    PSR_CONFIG_DIST_GLOB_PATTERNS,
    PSR_CONFIG_FILE_NAME,
    SUCCESSFUL_RETURN_CODE,
    TEST_REPO_NAME,
)


def test_psr_config_creation_without_origin_url_set(cli_runner: CliRunner, test_project_path_str) -> None:
    result: Result = cli_runner.invoke(cli, ["-C", test_project_path_str, "psr-config"])
    assert result.exit_code == RemoteNotFoundError.code


@mark.usefixtures("set_remote_url")
def test_psr_config_creation_with_origin_url_set(cli_runner: CliRunner, test_project_path_str) -> None:
    result: Result = cli_runner.invoke(cli, ["-C", test_project_path_str, "psr-config"])
    assert result.exit_code == SUCCESSFUL_RETURN_CODE

    config_file = Path(test_project_path_str) / PSR_CONFIG_FILE_NAME
    assert config_file.is_file()

    config_file_toml: dict[str, str] = load(config_file.open("rb"))
    config = config_file_toml["semantic_release"]
    assert config["repo_dir"] == f"/home/runner/work/{TEST_REPO_NAME}/{TEST_REPO_NAME}/"
    assert config["publish"]["dist_glob_patterns"] == PSR_CONFIG_DIST_GLOB_PATTERNS
