#!/bin/sh

# Usage: run this from project directory: ./scripts/update-action-versions

if git pull; then

    uv run -- ci-start update-actions
    ./scripts/update-test_update_actions.sh

    git add .
    git commit -m "ci: update action versions"
    git push

fi
