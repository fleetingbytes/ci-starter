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
        commit="de0fac2e4500dabe0009e67214ff5f5447ce83dd",
        version=Version.parse("6.0.2"),
    )
    expected_actions["actions/download-artifact"] = Action(
        owner="actions",
        repo="download-artifact",
        commit="3e5f45b2cfb9172054b4087a40e8e0b5a5461e7c",
        version=Version.parse("8.0.1"),
    )
    expected_actions["actions/setup-python"] = Action(
        owner="actions",
        repo="setup-python",
        commit="a309ff8b426b58ec0e2a45f0f869d46889d02405",
        version=Version.parse("6.2.0"),
    )
    expected_actions["actions/upload-artifact"] = Action(
        owner="actions",
        repo="upload-artifact",
        commit="043fb46d1a93c77aae656e7c1c64a875d1fc6a0a",
        version=Version.parse("7.0.1"),
    )
    expected_actions["astral-sh/ruff-action"] = Action(
        owner="astral-sh",
        repo="ruff-action",
        commit="0ce1b0bf8b818ef400413f810f8a11cdbda0034b",
        version=Version.parse("4.0.0"),
    )
    expected_actions["astral-sh/setup-uv"] = Action(
        owner="astral-sh",
        repo="setup-uv",
        commit="08807647e7069bb48b6ef5acd8ec9567f424441b",
        version=Version.parse("8.1.0"),
    )
    expected_actions["pypa/gh-action-pypi-publish"] = Action(
        owner="pypa",
        repo="gh-action-pypi-publish",
        commit="cef221092ed1bacb1cc03d23a2d87d1d172e277b",
        version=Version.parse("1.14.0"),
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
