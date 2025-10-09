from pathlib import Path

from click.testing import CliRunner, Result
from ruamel.yaml import YAML as Yaml
from semver.version import Version

from ci_starter.action import Action
from ci_starter.cli import cli
from ci_starter.constants import GITHUB_WORKFLOWS_DIR
from ci_starter.utils import compare, get_actions
from tests.e2e.constants import SUCCESSFUL_RETURN_CODE


def test_update_action(cli_runner: CliRunner, test_project_path_str, step_parser: Yaml) -> None:
    result: Result = cli_runner.invoke(cli, ["-C", test_project_path_str, "workflows"])
    assert result.exit_code == SUCCESSFUL_RETURN_CODE
    result: Result = cli_runner.invoke(cli, ["-C", test_project_path_str, "update-actions"])
    assert result.exit_code == SUCCESSFUL_RETURN_CODE

    workflows = Path(test_project_path_str, GITHUB_WORKFLOWS_DIR).rglob("*.yml")

    expected_actions: dict[str, Action] = {}

    # adding keys and values to expected_actions is managed by scripts/update-test_update_actions.sh
    expected_actions["actions/checkout"] = Action(
        owner="actions",
        repo="checkout",
        commit="08c6903cd8c0fde910a37f88322edcfb5dd907a8",
        version=Version.parse("5.0.0"),
    )
    expected_actions["actions/download-artifact"] = Action(
        owner="actions",
        repo="download-artifact",
        commit="634f93cb2916e3fdff6788551b99b062d0335ce0",
        version=Version.parse("5.0.0"),
    )
    expected_actions["actions/setup-python"] = Action(
        owner="actions",
        repo="setup-python",
        commit="e797f83bcb11b83ae66e0230d6156d7c80228e7c",
        version=Version.parse("6.0.0"),
    )
    expected_actions["actions/upload-artifact"] = Action(
        owner="actions",
        repo="upload-artifact",
        commit="ea165f8d65b6e75b540449e92b4886f43607fa02",
        version=Version.parse("4.6.2"),
    )
    expected_actions["astral-sh/ruff-action"] = Action(
        owner="astral-sh",
        repo="ruff-action",
        commit="57714a7c8a2e59f32539362ba31877a1957dded1",
        version=Version.parse("3.5.1"),
    )
    expected_actions["astral-sh/setup-uv"] = Action(
        owner="astral-sh",
        repo="setup-uv",
        commit="eb1897b8dc4b5d5bfe39a428a8f2304605e0983c",
        version=Version.parse("7.0.0"),
    )
    expected_actions["pypa/gh-action-pypi-publish"] = Action(
        owner="pypa",
        repo="gh-action-pypi-publish",
        commit="ed0c53931b1dc9bd32cbe73a98c7f6766f8a527e",
        version=Version.parse("1.13.0"),
    )

    for file in workflows:
        data = step_parser.load(file)
        for action in get_actions(data):
            actual_version = action.version
            actual_commit = action.commit
            expected_version = expected_actions[action.name].version
            expected_commit = expected_actions[action.name].commit

            compare_result = compare(actual_version, expected_version)
            assert actual_version == expected_version, (
                f"actual version is {compare_result} than the expected version"
            )
            assert actual_commit == expected_commit
