#!/bin/sh
# Rationale:
# Ci-starter has the subcommand update-actions to update an end-user's project's workflow files to that they
# use the latest versions of the GitHub actions. This updates the actions in all of the end-user's project's
# workflow files, regardless whether these workflow files have been created with ci-starter or manually.
# 
# Ci-starter project has an end-to-end test where we test if this update-actions subcommand works properly.
# In that test we check if the handful of actions ci-starter uses in its workflow templates are updated
# correctly and match their respective expeced commit SHA and version. The expected current commit SHA
# and version of each GitHub action needs to be hard-coded in the end-to-end test.
# However, as time goes on, the expected commit SHAs and versions of the updated actions from ci-starter's
# templates change because these actions, too, are getting new releases from time to time.
#
# The maintainer of the ci-starter project needs a way to update the end-to-end test's code
# so that the expected versions match the actual current version of the actions. Doing this manually is
# cumbersome. This script was written to update the code of the end-to-end test of the
# update-actions subcommand programatically.
#
# Usage:
# - make sure you are in the ci-starter's project directory
# - uv executable is in $PATH
# - ci-starter project is installed with the lint dev-dependency group
# - for frequent use provide a GitHub personal access token to avoid getting rate-limited
# CI_STARTER_GH_API_TOKEN=<your-access-token-for-github> ./scripts/update-test_update_actions.sh

WORKFLOWS=./.github/workflows
TEST_FILE=./tests/e2e/test_update_actions.py

actions_from_all_workflows() {
    find "$WORKFLOWS" -type f -name "*.yml" \
        | xargs sed -nE 's$uses: ([^[:space:]]+)/([^[:space:]]+)@([0-9a-f]{40})  # v([^[:space:]]+)$\1 \2 \3 \4$p' \
        | sort | uniq
}

get_actions_from_all_workflows_with_their_latest_commits_and_versions() {
    actions_from_all_workflows | while read owner repo old_commit old_version; do
        url="https://api.github.com/repos/$owner/$repo/tags"

        if [ -n "$CI_STARTER_GH_API_TOKEN" ]; then
            tags=$(curl -sS -H "Authorization: token $CI_STARTER_GH_API_TOKEN" "$url")
        else
            tags=$(curl -sS "$url")
        fi

        latest_release=$(echo "$tags" | jq -rc '.[0]')
        commit=$(echo "$latest_release" | jq -r '.commit.sha')

        latest_tag_name=$(echo "$latest_release" | jq -r '.name')
        version=${latest_tag_name#v}

        printf "%s %s %s %s\n" "$owner" "$repo" "$commit" "$version"
    done
}

find_line_where_to_insert_code() {
    sed -n '/# adding keys and values to expected_actions is managed by scripts\/update-test_update_actions.sh/=' "$TEST_FILE"
}

find_line_where_original_code_continues() {
    sed -n '/for file in workflows:/=' "$TEST_FILE"
}

generate_code() {
    get_actions_from_all_workflows_with_their_latest_commits_and_versions | while read owner repo commit version; do
        name="$owner/$repo"
        printf '    expected_actions["%s"] = Action(owner="%s", repo="%s", commit="%s", version=Version.parse("%s"),)\n' \
            "$name" "$owner" "$repo" "$commit" "$version"
    done
    printf "\n"
}

main() {
    head_lines=$(find_line_where_to_insert_code)
    tail_lines=$(find_line_where_original_code_continues)

    temp_test_file=$(mktemp)

    head -n "$head_lines" "$TEST_FILE" >> "$temp_test_file"
    generate_code >> "$temp_test_file"
    tail -n +"$tail_lines" "$TEST_FILE" >> "$temp_test_file"

    mv "$temp_test_file" "$TEST_FILE"

    uv run -- ruff format "$TEST_FILE"
}

main
