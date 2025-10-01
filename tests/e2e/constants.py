from importlib.metadata import version as get_version
from pathlib import Path

import ci_starter
from ci_starter.presets import DISTRIBUTION_ARTIFACTS_DIR, SEMANTIC_RELEASE_CONFIG_FILE

CI_STARTER_VERSION = get_version(ci_starter.__name__)
SUCCESSFUL_RETURN_CODE = 0
TEST_PROJECT_DIR_NAME = "my-test.project"
TEST_REPO_PATH = Path(TEST_PROJECT_DIR_NAME, "master")
TEST_REPO_NAME = "ci-starter-test-repo-name"
PSR_CONFIG_FILE_NAME = SEMANTIC_RELEASE_CONFIG_FILE
PSR_CONFIG_DIST_GLOB_PATTERNS = [f"{DISTRIBUTION_ARTIFACTS_DIR}/*"]

TEST_PACKAGE_NAME = "my-test-project"
TEST_DISTRIBUTION_FILE_INCIPIT = "my_test_project"
TEST_TEST_DEPENDENCY_GROUP = "testgroup"
TEST_RUN_TEST_COMMAND = "uv run -- pytest -vx"
TEST_SEMANTIC_RELEASE_CONFIG_FILE = "./test-semantic-release.toml"
TEST_DISTRIBUTION_ARTIFACTS_NAME = "distribution"
TEST_DISTRIBUTION_ARTIFACTS_DIR = "distrib"
TEST_LOCK_FILE_ARTIFACT = "pylock.toml"
