#!/bin/sh

for file in $(ls .github/workflows/*.yml); do
    sed -E "s/@[0-9a-f]{40}  # v[.[:digit:]]+$/@0000000000000000000000000000000000000000  # v0.0.0/" "$file" > "src/ci_starter/assets/workflows/$(basename "$file")"
done

