from collections.abc import Iterable, Mapping

from pytest import mark, param

from ci_starter import generate_base_workflow
from ci_starter.action import Action
from ci_starter.constants import (
    BUILD_WORKFLOW_ASSET_PATH,
    RELEASE_WORKFLOW_ASSET_PATH,
    TEST_E2E_WORKFLOW_ASSET_PATH,
)
from ci_starter.step import Step
from tests.e2e.constants import (
    TEST_DISTRIBUTION_ARTIFACTS_DIR,
    TEST_DISTRIBUTION_ARTIFACTS_NAME,
    TEST_DISTRIBUTION_FILE_INCIPIT,
    TEST_LOCK_FILE_ARTIFACT,
    TEST_PACKAGE_NAME,
    TEST_RUN_TEST_COMMAND,
    TEST_SEMANTIC_RELEASE_CONFIG_FILE,
    TEST_TEST_DEPENDENCY_GROUP,
)


def test_base_workflow_content():
    test_env_dict = {
        "package_name": TEST_PACKAGE_NAME,
        "distribution_file_incipit": TEST_DISTRIBUTION_FILE_INCIPIT,
        "test_dependency_group": TEST_TEST_DEPENDENCY_GROUP,
        "run_test_command": TEST_RUN_TEST_COMMAND,
        "semantic_release_config_file": TEST_SEMANTIC_RELEASE_CONFIG_FILE,
        "distribution_artifacts_name": TEST_DISTRIBUTION_ARTIFACTS_NAME,
        "distribution_artifacts_dir": TEST_DISTRIBUTION_ARTIFACTS_DIR,
        "lock_file_artifact": TEST_LOCK_FILE_ARTIFACT,
    }

    expected = {k.upper(): v for k, v in test_env_dict.items()}

    base_workflow: dict = generate_base_workflow(**test_env_dict)

    assert base_workflow["env"] == expected


def get_actions_from_list(lst: list) -> Iterable[Action]:
    for item in lst:
        if isinstance(item, Step):
            yield item.uses


def get_actions(workflow: Mapping) -> Iterable[Action]:
    for v in workflow.values():
        if isinstance(v, list):
            yield from get_actions_from_list(v)
        elif isinstance(v, Mapping):
            yield from get_actions(v)


@mark.parametrize(
    "workflow, expected",
    (
        param(BUILD_WORKFLOW_ASSET_PATH, 5, id=BUILD_WORKFLOW_ASSET_PATH.name),
        param(RELEASE_WORKFLOW_ASSET_PATH, 5, id=RELEASE_WORKFLOW_ASSET_PATH.name),
        param(TEST_E2E_WORKFLOW_ASSET_PATH, 4, id=TEST_E2E_WORKFLOW_ASSET_PATH.name),
    ),
    indirect=("workflow",),
)
def test_reusable_workflow_content(workflow, expected):
    actions = set(get_actions(workflow))
    assert len(actions) == expected
