from pathlib import Path
from shlex import join, split
from subprocess import run

from click.testing import CliRunner
from git import Remote, Repo
from pytest import fixture

from ci_starter.constants import (
    GITHUB_WORKFLOWS_DIR,
)
from tests.e2e.constants import (
    TEST_PROJECT_DIR_NAME,
    TEST_REPO_NAME,
    TEST_REPO_PATH,
)


@fixture
def cli_runner() -> CliRunner:
    return CliRunner(catch_exceptions=False)


@fixture
def test_project_path_str(tmp_path) -> str:
    absolute_test_repo_path = tmp_path / TEST_REPO_PATH

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
                str(absolute_test_repo_path),
            )
        )
    )

    run(create_uv_project_cmd, check=True, capture_output=True, text=True)

    expected_project_path = absolute_test_repo_path
    assert expected_project_path.is_dir()

    return str(expected_project_path)


@fixture(autouse=True)
def set_remote_url(test_project_path_str) -> None:
    repo = Repo(test_project_path_str)
    Remote.add(repo, "origin", f"git@github.com:username/{TEST_REPO_NAME}.git")


@fixture
def remote_url_not_set(test_project_path_str) -> None:
    repo = Repo(test_project_path_str)
    remote = next(iter(repo.remotes))
    Remote.remove(repo, remote.name)


@fixture
def test_project_workflows_path(test_project_path_str) -> Path:
    return Path(test_project_path_str, GITHUB_WORKFLOWS_DIR)
