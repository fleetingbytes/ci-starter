from pathlib import Path

from click.testing import CliRunner, Result
from ruamel.yaml import YAML as Yaml

from ci_starter.cli import cli
from ci_starter.constants import GITHUB_WORKFLOWS_DIR
from ci_starter.dataclasses import CommitVersion, OwnerRepo
from ci_starter.utils import get_actions
from tests.e2e.constants import SUCCESSFUL_RETURN_CODE


def test_update_action(cli_runner: CliRunner, test_project_path_str, step_parser: Yaml) -> None:
    result: Result = cli_runner.invoke(cli, ["-C", test_project_path_str, "workflows"])
    assert result.exit_code == SUCCESSFUL_RETURN_CODE
    result: Result = cli_runner.invoke(cli, ["-C", test_project_path_str, "update-actions"])
    assert result.exit_code == SUCCESSFUL_RETURN_CODE

    workflows = Path(test_project_path_str, GITHUB_WORKFLOWS_DIR).rglob("*.yml")

    expected_actions: dict[OwnerRepo, CommitVersion] = {}

    # adding keys and values to expected_actions is managed by scripts/update-test_update_actions.sh
    expected_actions[OwnerRepo("actions", "checkout")] = CommitVersion(
        "08c6903cd8c0fde910a37f88322edcfb5dd907a8", "5.0.0"
    )
    expected_actions[OwnerRepo("actions", "download-artifact")] = CommitVersion(
        "634f93cb2916e3fdff6788551b99b062d0335ce0", "5.0.0"
    )
    expected_actions[OwnerRepo("actions", "setup-python")] = CommitVersion(
        "e797f83bcb11b83ae66e0230d6156d7c80228e7c", "6.0.0"
    )
    expected_actions[OwnerRepo("actions", "upload-artifact")] = CommitVersion(
        "ea165f8d65b6e75b540449e92b4886f43607fa02", "4.6.2"
    )
    expected_actions[OwnerRepo("astral-sh", "ruff-action")] = CommitVersion(
        "57714a7c8a2e59f32539362ba31877a1957dded1", "3.5.1"
    )
    expected_actions[OwnerRepo("astral-sh", "setup-uv")] = CommitVersion(
        "eb1897b8dc4b5d5bfe39a428a8f2304605e0983c", "7.0.0"
    )
    expected_actions[OwnerRepo("pypa", "gh-action-pypi-publish")] = CommitVersion(
        "ed0c53931b1dc9bd32cbe73a98c7f6766f8a527e", "1.13.0"
    )

    for file in workflows:
        data = step_parser.load(file)
        for action in get_actions(data):
            actual_commit_and_version = CommitVersion(action.commit, str(action.version))
            expected_commit_and_version = expected_actions[OwnerRepo(action.owner, action.repo)]
            assert actual_commit_and_version == expected_commit_and_version
