from pathlib import Path

from click.testing import CliRunner, Result
from pytest import mark, param

from ci_starter.cli import cli
from ci_starter.constants import (
    BASE_WORKFLOW_ASSET_PATH,
    BASE_WORKFLOW_FILE_PATH,
    BUILD_WORKFLOW_ASSET_PATH,
    BUILD_WORKFLOW_FILE_PATH,
    HELPER_SCRIPT_ASSET_PATH,
    HELPER_SCRIPT_FILE_PATH,
    RELEASE_WORKFLOW_ASSET_PATH,
    RELEASE_WORKFLOW_FILE_PATH,
    TEST_E2E_WORKFLOW_ASSET_PATH,
    TEST_E2E_WORKFLOW_FILE_PATH,
)
from ci_starter.presets import (
    DISTRIBUTION_ARTIFACTS_DIR,
    DISTRIBUTION_ARTIFACTS_NAME,
    LOCKFILE_ARTIFACT,
    SEMANTIC_RELEASE_CONFIG_FILE,
    WORKFLOWS_DIR,
)
from ci_starter.utils import get_asset
from tests.e2e.comparator import Comparator
from tests.e2e.constants import (
    SUCCESSFUL_RETURN_CODE,
    TEST_DISTRIBUTION_FILE_INCIPIT,
    TEST_PACKAGE_NAME,
    TEST_RUN_TEST_COMMAND,
    TEST_TEST_DEPENDENCY_GROUP,
)


def get_comparator(
    runner: CliRunner, test_project_path_str: str, asset_path: Path, rendered_path: Path
) -> Comparator:
    asset: str = get_asset(asset_path)

    rendered_path = Path(test_project_path_str, rendered_path)
    assert not rendered_path.exists()

    result: Result = runner.invoke(cli, ["-C", test_project_path_str, "workflows"])
    assert result.exit_code == SUCCESSFUL_RETURN_CODE

    rendered = rendered_path.read_text(encoding="utf-8")
    return Comparator(asset, rendered)


@mark.parametrize(
    "asset_path, rendered_path",
    (
        param(HELPER_SCRIPT_ASSET_PATH, HELPER_SCRIPT_FILE_PATH, id=HELPER_SCRIPT_FILE_PATH.stem),
        param(BASE_WORKFLOW_ASSET_PATH, BASE_WORKFLOW_FILE_PATH, id=BASE_WORKFLOW_FILE_PATH.stem),
        param(BUILD_WORKFLOW_ASSET_PATH, BUILD_WORKFLOW_FILE_PATH, id=BUILD_WORKFLOW_FILE_PATH.stem),
        param(RELEASE_WORKFLOW_ASSET_PATH, RELEASE_WORKFLOW_FILE_PATH, id=RELEASE_WORKFLOW_FILE_PATH.stem),
        param(
            TEST_E2E_WORKFLOW_ASSET_PATH, TEST_E2E_WORKFLOW_FILE_PATH, id=TEST_E2E_WORKFLOW_FILE_PATH.stem
        ),
    ),
)
def test_asset_vs_rendered_file(
    cli_runner: CliRunner, test_project_path_str: str, asset_path: Path, rendered_path: Path
) -> None:
    comparator = get_comparator(cli_runner, test_project_path_str, asset_path, rendered_path)
    comparator.compare_lines()


def test_base_file_env_vars(cli_runner: CliRunner, test_project_path_str, yaml_parser):
    custom_workflow_file_name = "main.yml"

    result: Result = cli_runner.invoke(
        cli,
        [
            "-C",
            test_project_path_str,
            "workflows",
            "--test-group",
            TEST_TEST_DEPENDENCY_GROUP,
            "--test-command",
            TEST_RUN_TEST_COMMAND,
            "--module-name",
            TEST_DISTRIBUTION_FILE_INCIPIT,
            "--workflow-file-name",
            custom_workflow_file_name,
        ],
    )
    assert result.exit_code == SUCCESSFUL_RETURN_CODE

    base_workflow_file = Path(test_project_path_str, WORKFLOWS_DIR, custom_workflow_file_name)
    data: dict = yaml_parser.load(base_workflow_file)

    assert data["env"]["PACKAGE_NAME"] == TEST_PACKAGE_NAME
    assert data["env"]["DISTRIBUTION_FILE_INCIPIT"] == TEST_DISTRIBUTION_FILE_INCIPIT
    assert data["env"]["TEST_DEPENDENCY_GROUP"] == TEST_TEST_DEPENDENCY_GROUP
    assert data["env"]["RUN_TEST_COMMAND"] == TEST_RUN_TEST_COMMAND

    assert data["env"]["SEMANTIC_RELEASE_CONFIG_FILE"] == SEMANTIC_RELEASE_CONFIG_FILE
    assert data["env"]["DISTRIBUTION_ARTIFACTS_NAME"] == DISTRIBUTION_ARTIFACTS_NAME
    assert data["env"]["DISTRIBUTION_ARTIFACTS_DIR"] == DISTRIBUTION_ARTIFACTS_DIR
    assert data["env"]["LOCKFILE_ARTIFACT"] == LOCKFILE_ARTIFACT
