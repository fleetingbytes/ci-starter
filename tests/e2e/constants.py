from importlib.metadata import version as get_version

import ci_starter
from ci_starter.presets import DISTRIBUTION_ARTIFACTS_DIR, SEMANTIC_RELEASE_CONFIG_FILE

CI_STARTER_VERSION = get_version(ci_starter.__name__)
SUCCESSFUL_RETURN_CODE = 0
TEST_PROJECT_DIR_NAME = "my-test.project"
TEST_REPO_PATH = f"{TEST_PROJECT_DIR_NAME}/master"
TEST_REPO_NAME = "ci-starter-test-repo-name"
PSR_CONFIG_FILE_NAME = SEMANTIC_RELEASE_CONFIG_FILE
PSR_CONFIG_DIST_GLOB_PATTERNS = [f"{DISTRIBUTION_ARTIFACTS_DIR}/*"]
