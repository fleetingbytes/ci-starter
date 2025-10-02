from pathlib import Path

from click.testing import CliRunner, Result
from pytest import mark, param

from ci_starter.asset_getter import get_asset
from ci_starter.cli import cli
from ci_starter.constants import (
    BASE_WORKFLOW_ASSET_PATH,
    BASE_WORKFLOW_FILE_PATH,
    HELPER_SCRIPT_ASSET_PATH,
    HELPER_SCRIPT_FILE_PATH,
)
from tests.e2e.comparator import Comparator
from tests.e2e.constants import SUCCESSFUL_RETURN_CODE


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
    ),
)
def test_asset_vs_rendered_file(
    cli_runner: CliRunner, test_project_path_str: str, asset_path: Path, rendered_path: Path
) -> None:
    comparator = get_comparator(cli_runner, test_project_path_str, asset_path, rendered_path)
    comparator.compare_lines()
