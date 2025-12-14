#!/usr/bin/env sh

get_absolute_path_to_parent_dir_of_this_script() {
    local absolute_path="$(readlink -f -- "$1")"
    local parent_dir="$(dirname "$absolute_path")"
    printf "$parent_dir"
}

SCRIPT_DIR="$(get_absolute_path_to_parent_dir_of_this_script "$0")"
PROJECT_DIR=$(dirname "$SCRIPT_DIR")

if git -C "$PROJECT_DIR" pull; then

    uv --directory "$PROJECT_DIR" run -- ci-start --project-path "$PROJECT_DIR" update-actions
    "$SCRIPT_DIR"/update-test_update_actions.sh

    git -C "$PROJECT_DIR" add .
    git -C "$PROJECT_DIR" commit -m "ci: update action versions"
    git -C "$PROJECT_DIR" push

fi
