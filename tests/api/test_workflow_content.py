from ci_starter import generate_base_workflow
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
