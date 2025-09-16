from shlex import join, split
from subprocess import run

from click.testing import CliRunner
from pytest import fixture

from tests.e2e.constants import (
    TEST_PROJECT_DIR_NAME,
    TEST_REPO_NAME,
    TEST_REPO_PATH,
)


@fixture
def cli_runner() -> CliRunner:
    return CliRunner()


@fixture
def test_project_path_str(tmp_path) -> str:
    create_uv_project_cmd = split(
        join(
            (
                "uv",
                "--directory",
                str(tmp_path),
                "init",
                "--package",
                "--app",
                "--vcs",
                "git",
                "--name",
                TEST_PROJECT_DIR_NAME,
                str(TEST_REPO_PATH),
            )
        )
    )

    run(create_uv_project_cmd, check=True, capture_output=True, text=True)

    expected_project_path = tmp_path / TEST_REPO_PATH
    assert expected_project_path.is_dir()

    return str(expected_project_path)


@fixture
def set_remote_url(test_project_path_str) -> None:
    set_remote_cmd = split(
        join(
            (
                "git",
                "-C",
                test_project_path_str,
                "remote",
                "add",
                "origin",
                f"git@github.com:username/{TEST_REPO_NAME}.git",
            )
        )
    )

    run(set_remote_cmd, check=True, capture_output=True, text=True)
