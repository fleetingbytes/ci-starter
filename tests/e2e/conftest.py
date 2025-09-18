from pathlib import Path
from shlex import join, split
from subprocess import run

from click.testing import CliRunner
from pytest import fixture
from ruamel.yaml import YAML

from ci_starter.asset_getter import get_asset
from tests.e2e.constants import (
    BASE_WORKFLOW_ASSET_PATH,
    BASE_WORKFLOW_FILE_NAME,
    BUILD_WORKFLOW_ASSET_PATH,
    BUILD_WORKFLOW_FILE_NAME,
    GITHUB_WORKFLOWS_DIR,
    HELPER_SCRIPT_ASSET_PATH,
    HELPER_SCRIPT_FILE_NAME,
    RELEASE_WORKFLOW_ASSET_PATH,
    RELEASE_WORKFLOW_FILE_NAME,
    TEST_E2E_WORKFLOW_ASSET_PATH,
    TEST_E2E_WORKFLOW_FILE_NAME,
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


@fixture
def test_project_workflows_path(test_project_path_str) -> Path:
    return Path(test_project_path_str, GITHUB_WORKFLOWS_DIR)


@fixture
def helper_script(test_project_workflows_path) -> str:
    script: str = get_asset(HELPER_SCRIPT_ASSET_PATH)
    path = test_project_workflows_path / HELPER_SCRIPT_FILE_NAME
    return script, path


def to_yaml(s: str) -> YAML:
    yaml = YAML()
    yaml.load(s)
    return yaml


@fixture
def build_workflow(test_project_workflows_path) -> YAML:
    workflow: str = get_asset(BUILD_WORKFLOW_ASSET_PATH)
    yaml = to_yaml(workflow)
    path = test_project_workflows_path / BUILD_WORKFLOW_FILE_NAME
    return yaml, path


@fixture
def test_e2e_workflow(test_project_workflows_path) -> YAML:
    workflow: str = get_asset(TEST_E2E_WORKFLOW_ASSET_PATH)
    yaml = to_yaml(workflow)
    path = test_project_workflows_path / TEST_E2E_WORKFLOW_FILE_NAME
    return yaml, path


@fixture
def release_workflow(test_project_workflows_path) -> YAML:
    workflow: str = get_asset(RELEASE_WORKFLOW_ASSET_PATH)
    yaml = to_yaml(workflow)
    path = test_project_workflows_path / RELEASE_WORKFLOW_FILE_NAME
    return yaml, path


@fixture
def base_workflow(test_project_workflows_path) -> YAML:
    workflow: str = get_asset(BASE_WORKFLOW_ASSET_PATH)
    yaml = to_yaml(workflow)
    path = test_project_workflows_path / BASE_WORKFLOW_FILE_NAME
    return yaml, path
