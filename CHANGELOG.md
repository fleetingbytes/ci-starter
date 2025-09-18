# CHANGELOG

<!-- version list -->

## v0.4.0 (2025-09-18)

### Chores

- Update uv_build version
  ([`b487b6f`](https://github.com/fleetingbytes/ci-starter/commit/b487b6fffd2097f62313741ce38cc8b286a7f030))

### Features

- Generate helper script
  ([`bd108b7`](https://github.com/fleetingbytes/ci-starter/commit/bd108b75af33d78039b4eab43bb2c5b9d4e392c1))

### Refactoring

- Changed cli so that it has subcommands
  ([`da8e00f`](https://github.com/fleetingbytes/ci-starter/commit/da8e00ffea76982a5eb9ae8b70d893554610e71b))

### Testing

- Rewrite tests to adapt to future cli
  ([`f4d8463`](https://github.com/fleetingbytes/ci-starter/commit/f4d8463bc5123130c9a8a5dbb51256e329a7c15c))

- Write test for creation of helper script
  ([`c426b29`](https://github.com/fleetingbytes/ci-starter/commit/c426b298cbdc82ea368364119c8cc91935f3fcf3))


## v0.3.4 (2025-09-16)

### Documentation

- Spelling
  ([`a48fcf6`](https://github.com/fleetingbytes/ci-starter/commit/a48fcf697faccf2e0146c6760f9a84b61a3d3a95))

- Spelling
  ([`8a809ba`](https://github.com/fleetingbytes/ci-starter/commit/8a809babb14b310a84faf23f971172aa326eb50d))

### Refactoring

- General CiStarterError handling
  ([`7e4ddb3`](https://github.com/fleetingbytes/ci-starter/commit/7e4ddb32154dd1b1158f57c0dae5f83a95605d6b))

### Testing

- Test cli
  ([`ae4c301`](https://github.com/fleetingbytes/ci-starter/commit/ae4c301b9c3b53d54ad87f426acb0ddae3c5c9dc))


## v0.3.3 (2025-09-15)

### Refactoring

- Write semantic release config
  ([`d779670`](https://github.com/fleetingbytes/ci-starter/commit/d779670ee6755c82c7236c8a428f1ca673f590bc))


## v0.3.2 (2025-09-14)

### Continuous Integration

- Upgrade to actions/setup-python v6.0.0
  ([`cb8ad09`](https://github.com/fleetingbytes/ci-starter/commit/cb8ad09d56a8a03999b5fe62da46837c7e98ebbc))

- Upgrade to astral-sh/setup-uv v6.6.1
  ([`f951646`](https://github.com/fleetingbytes/ci-starter/commit/f951646e67c9dcbf664d11982f6132785d5c49a4))

### Refactoring

- Introduce presets (things we can configure, but are not configurable by the user)
  ([`47dece6`](https://github.com/fleetingbytes/ci-starter/commit/47dece64422145a30b29bb564bdafac93c1b9f82))


## v0.3.1 (2025-09-14)

### Bug Fixes

- Improved parsing of upstream branch name
  ([`3cbf976`](https://github.com/fleetingbytes/ci-starter/commit/3cbf9764d534e15415eefbaee96e7b62bae39509))

- Remove unused workspace
  ([`75037c7`](https://github.com/fleetingbytes/ci-starter/commit/75037c795bde0bcce926872225d714fd5d6a8734))

### Code Style

- Add type hints
  ([`dca2182`](https://github.com/fleetingbytes/ci-starter/commit/dca218261f73fa2691c3be5af9fb619d793f4f55))

### Continuous Integration

- Make semantic release config file name not configurable by the user
  ([`3101632`](https://github.com/fleetingbytes/ci-starter/commit/31016326c26b1b0cd3b7359e0454c485b9f11d60))

- Remove redundant env var
  ([`6bb3322`](https://github.com/fleetingbytes/ci-starter/commit/6bb3322210a28d1b130eb890ed0d75c4dce2ec90))


## v0.3.0 (2025-09-13)

### Continuous Integration

- Debug build: uv sync
  ([`61b3292`](https://github.com/fleetingbytes/ci-starter/commit/61b32926a1e548dcc1e600466efe9f857371bc9e))

- Debug build: uv sync
  ([`b683be4`](https://github.com/fleetingbytes/ci-starter/commit/b683be4604df9f49c41f77af8c2ce6621394b0f6))

- Don't use uv --locked when installing the project
  ([`0ab202a`](https://github.com/fleetingbytes/ci-starter/commit/0ab202a1dda93c6a3115124c3f25b3e6256423ce))

- Don't use uv --locked when installing the project for release
  ([`d6132b9`](https://github.com/fleetingbytes/ci-starter/commit/d6132b94201f7f1a3c4fb15661403acaecbc3e48))

- Don't use uv --locked when installing the project for test
  ([`0c5d020`](https://github.com/fleetingbytes/ci-starter/commit/0c5d0200dbac733a791b29b99485bbd2a4e736d6))

### Features

- Render semantic-release config file
  ([`e735da7`](https://github.com/fleetingbytes/ci-starter/commit/e735da759a1f64414cc63750d3579d33b2bb2543))


## v0.2.0 (2025-09-08)

### Chores

- Add click as a dependency
  ([`62dcdb6`](https://github.com/fleetingbytes/ci-starter/commit/62dcdb6f93c7144dcc18abf1864d0464cf6ed2f2))

### Code Style

- Update linting rules
  ([`dff02d0`](https://github.com/fleetingbytes/ci-starter/commit/dff02d0aeb58341939c676fc9a828bf44dd6421a))

### Continuous Integration

- Remove erroneous step from build command
  ([`fa0aa80`](https://github.com/fleetingbytes/ci-starter/commit/fa0aa806d2412ed41b7f12325db47973f05204db))

### Documentation

- Add keywords and classifiers
  ([`a17b118`](https://github.com/fleetingbytes/ci-starter/commit/a17b118b98ab2a0fbd15908b0614286bd9d8e5a6))

- Prerequisites and usage
  ([`c489ea8`](https://github.com/fleetingbytes/ci-starter/commit/c489ea836c091842545367193fc20cdd3b45a88c))

### Features

- Outline cli
  ([`95dcddb`](https://github.com/fleetingbytes/ci-starter/commit/95dcddb8966ab299cbf3821c745af79664f043ba))

### Refactoring

- Change entrypoint function to cli
  ([`90829a8`](https://github.com/fleetingbytes/ci-starter/commit/90829a8e8f3865691bf0cc2e6e186ca1f5b394f2))


## v0.1.0 (2025-09-07)

- Initial Release
