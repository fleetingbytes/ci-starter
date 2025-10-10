# CHANGELOG

<!-- version list -->

## v0.10.3 (2025-10-10)

### Bug Fixes

- Cli now uses only the name of the workflow file even if a whole path was given
  ([`56090f5`](https://github.com/fleetingbytes/ci-starter/commit/56090f591507fb2cb1c327a9814de6da19ceef80))

### Chores

- Bump uv_build version
  ([`ba45225`](https://github.com/fleetingbytes/ci-starter/commit/ba45225085e6ec17869146c7933c6d37293aa8d8))

### Continuous Integration

- Update version of setup-uv
  ([`bef6f48`](https://github.com/fleetingbytes/ci-starter/commit/bef6f4886ff42a455b22cbecf23fd509b9657103))

### Documentation

- Update documentation in update-test_update_actions.sh
  ([`e139126`](https://github.com/fleetingbytes/ci-starter/commit/e13912659882d1fc97f1aa55e45bde53711fbcb5))

- Update readme
  ([`5d699fb`](https://github.com/fleetingbytes/ci-starter/commit/5d699fbfd2542a561c28c13d2ae5727b8feca288))

### Testing

- **fix**: Update expected end of help output in --help
  ([`182531a`](https://github.com/fleetingbytes/ci-starter/commit/182531a456de6733babb4804d6153683ec1b657f))


## v0.10.2 (2025-10-09)

### Refactoring

- **test**: Add error text if versions are different
  ([`aa07920`](https://github.com/fleetingbytes/ci-starter/commit/aa079208024f9c338a454113eebeba0d9b5c2303))


## v0.10.1 (2025-10-09)

### Refactoring

- Do not fallback to GH_API_TOKEN, only use CI_STARTER_GH_API_TOKEN
  ([`f477100`](https://github.com/fleetingbytes/ci-starter/commit/f477100e41f6bcfd2faa5671537d4b9d75183222))


## v0.10.0 (2025-10-09)

### Bug Fixes

- Fallback to GH_API_TOKEN
  ([`bed760f`](https://github.com/fleetingbytes/ci-starter/commit/bed760fd098aeca72c511f8165d4549afc76d017))

### Chores

- Add .env to gitignore
  ([`376bc0e`](https://github.com/fleetingbytes/ci-starter/commit/376bc0e261a13a9e0fd15c647ac02210e3f39b0d))

- Add script to generate workflow assets
  ([`975bb7c`](https://github.com/fleetingbytes/ci-starter/commit/975bb7cf3ba921726e292ad4c5f8ff966ad41611))

- Update ruff dependency
  ([`dac4c32`](https://github.com/fleetingbytes/ci-starter/commit/dac4c3206c39825c8c67283090d7d41f711073cb))

### Code Style

- Update ruff rules
  ([`1e0b1dd`](https://github.com/fleetingbytes/ci-starter/commit/1e0b1dd2afd8c580d6995df30c0b86b168751577))

### Continuous Integration

- Map GH_API_TOKEN explicitly by name
  ([`3144078`](https://github.com/fleetingbytes/ci-starter/commit/31440789464e33c6f6b97cff8e1bde0833e05661))

- Try to use GITHUB_TOKEN as GH_API_TOKEN
  ([`5d66001`](https://github.com/fleetingbytes/ci-starter/commit/5d66001cf1400461276ae06864f52ce95f089c8d))

- Update action version
  ([`ea7fbfb`](https://github.com/fleetingbytes/ci-starter/commit/ea7fbfb003588a4b5fe5096830e6cee149c1b8d6))

- Use GH_API_TOKEN
  ([`45975ef`](https://github.com/fleetingbytes/ci-starter/commit/45975effcad74a30df874da0e1b565f3f0ff147a))

### Features

- Add subcommand update-actions
  ([`03c4a27`](https://github.com/fleetingbytes/ci-starter/commit/03c4a271660f36c34b017704d15efd64cc6f46e8))

### Refactoring

- Do not specify any action version in assets
  ([`f43455c`](https://github.com/fleetingbytes/ci-starter/commit/f43455cd8ea75247e92e4efc62338bdbd586ad32))

- Move dataclasses to ci_starter
  ([`92e36c7`](https://github.com/fleetingbytes/ci-starter/commit/92e36c71dba7e61f6651b9ba746f75eb5d53a407))

- Move get_actions to utils
  ([`74d01d9`](https://github.com/fleetingbytes/ci-starter/commit/74d01d9b0420461a31a72df8f11eaaa16aa54e4e))

- Rename field user to owner
  ([`1770fd1`](https://github.com/fleetingbytes/ci-starter/commit/1770fd1ffb8d0576632d0d8059ccf3ea5527db56))

### Testing

- Add test for update-actions
  ([`081b5ad`](https://github.com/fleetingbytes/ci-starter/commit/081b5ad50dafdb20d3a370d6666f9fba1cfe3136))

- **refactor**: Test_update_actions to use Action rather than dataclasses.OwnerRepo |
  dataclasses.CommitVersion
  ([`72f42cc`](https://github.com/fleetingbytes/ci-starter/commit/72f42cc8436b6674b242c61eb5330e3a86e1184e))


## v0.9.4 (2025-10-06)

### Refactoring

- Rename lock-file-artifact to lockfile-artifact
  ([`cb70c2d`](https://github.com/fleetingbytes/ci-starter/commit/cb70c2d3267bec71e8a1a4f9abf629cfea78ae5f))

### Testing

- Test main workflow file cli-settable variables
  ([`310973e`](https://github.com/fleetingbytes/ci-starter/commit/310973e47df11f7e4fc80610fe83e8860cdd977c))

- **fix**: Correct renaming lock file artifact to lockfile artifact
  ([`49d4831`](https://github.com/fleetingbytes/ci-starter/commit/49d48310e3348a2a0f72884c64ba87978f737e9d))


## v0.9.3 (2025-10-06)

### Refactoring

- Move get_asset to utils
  ([`bb7e7a8`](https://github.com/fleetingbytes/ci-starter/commit/bb7e7a85362a6ff24f6460683b2b05dc1edb3d5a))


## v0.9.2 (2025-10-02)

### Refactoring

- Improve readability
  ([`93e1097`](https://github.com/fleetingbytes/ci-starter/commit/93e109711e31a4deaa551ff3ec9a519af29bda09))

### Testing

- Compare asset vs rendered file
  ([`d1cdffd`](https://github.com/fleetingbytes/ci-starter/commit/d1cdffdd0b7c08500e39f94cbf62eb679b305d2b))

- Test all reusable workflows
  ([`0fe8757`](https://github.com/fleetingbytes/ci-starter/commit/0fe87576c65690deb427eaa879e3c8b79603e7be))


## v0.9.1 (2025-10-02)

### Bug Fixes

- Preserve my yaml style
  ([`5b6b660`](https://github.com/fleetingbytes/ci-starter/commit/5b6b660cfaeaa8860af725c19580d782e77aa35f))

- Preserve order of step keys
  ([`9004120`](https://github.com/fleetingbytes/ci-starter/commit/90041202bc3ad86cc709e01f50c6f2236a9bd029))


## v0.9.0 (2025-10-02)

### Bug Fixes

- Update other allowed tags in psr config
  ([`1f8aecd`](https://github.com/fleetingbytes/ci-starter/commit/1f8aecd1468232ac606b7b98f56c86e464142556))

### Code Style

- Reorder constants
  ([`4cc7b35`](https://github.com/fleetingbytes/ci-starter/commit/4cc7b35dc29daf716d7ea50645330758d4adce63))

### Features

- Make cli dump base workflow
  ([`5437361`](https://github.com/fleetingbytes/ci-starter/commit/543736113e10a2c7427c50f5a916f2d3fd984113))

### Refactoring

- Remove obsolete fixture
  ([`bf1d8a8`](https://github.com/fleetingbytes/ci-starter/commit/bf1d8a8c578097fe872831f9fe8ea43aeeea1fbf))

### Testing

- Compare asset vs rendered file draft, not working yet
  ([`9598b1d`](https://github.com/fleetingbytes/ci-starter/commit/9598b1d53cb06d0036b33fd1e061f841a830c9df))

- Improved comparator
  ([`bf3564a`](https://github.com/fleetingbytes/ci-starter/commit/bf3564ab27445ffa00a34de18647363d98be9c93))

- Skip comparing files for now
  ([`4d1ae32`](https://github.com/fleetingbytes/ci-starter/commit/4d1ae321f6de166d66fa9d4d4e986609f9217704))


## v0.8.2 (2025-10-01)

### Refactoring

- Generate_helper_script now returns a str
  ([`29f3bba`](https://github.com/fleetingbytes/ci-starter/commit/29f3bbaef2b28fce8c779e52965c7c5060160803))


## v0.8.1 (2025-10-01)

### Refactoring

- Use constants in WorkDir class
  ([`a4759be`](https://github.com/fleetingbytes/ci-starter/commit/a4759be9516647f94d78e5b6a1598f4e23d8ad4e))


## v0.8.0 (2025-10-01)

### Features

- Generate reusable workflow
  ([`1838c69`](https://github.com/fleetingbytes/ci-starter/commit/1838c69075edf9c62fd0e626a7c2a1cea2a3bd87))

### Testing

- Add dependency tests
  ([`4cec28b`](https://github.com/fleetingbytes/ci-starter/commit/4cec28bbb9d817b7bcb0270044fdeb88045ab1e8))

- Add tests of reusable workflows
  ([`e086ea2`](https://github.com/fleetingbytes/ci-starter/commit/e086ea2efd719df484b20216be88d167a7eab25d))


## v0.7.1 (2025-10-01)

### Bug Fixes

- Update env instead of overwriting it
  ([`d8147f1`](https://github.com/fleetingbytes/ci-starter/commit/d8147f1f4b76194b9305acf0d92a6cc4a6a153f9))


## v0.7.0 (2025-10-01)

### Bug Fixes

- Replace hard-coded 'uv.lock' in 'semantic-release.toml' with a placeholder bound to the preset
  LOCKFILE_ARTIFACT
  ([`9897bce`](https://github.com/fleetingbytes/ci-starter/commit/9897bcea9cf9a745a3db26d71e8c67d88239a867))

- Return object of from_yaml
  ([`8fb6480`](https://github.com/fleetingbytes/ci-starter/commit/8fb6480c4460a03f9f9f97c8ae0139ddb8f8760c))

### Code Style

- Update ruff rules
  ([`14d31a5`](https://github.com/fleetingbytes/ci-starter/commit/14d31a5620902676191b321203f5748896d50875))

- YAML -> Yaml
  ([`1d9266b`](https://github.com/fleetingbytes/ci-starter/commit/1d9266b1d77372c5227e3c04aba4f353e1daabbe))

### Continuous Integration

- Correct comment
  ([`a08def2`](https://github.com/fleetingbytes/ci-starter/commit/a08def23d1319298a02893073b9d57273413099a))

- Remove redundant comments
  ([`caeb8c1`](https://github.com/fleetingbytes/ci-starter/commit/caeb8c1c673ad638ee9b8c8546060cb8715ee64e))

- **fix**: Typehints
  ([`a4f7a75`](https://github.com/fleetingbytes/ci-starter/commit/a4f7a753987d225a5a7ee1774f696fd7595925d6))

### Documentation

- Create technical-decisions.md
  ([`f3146a5`](https://github.com/fleetingbytes/ci-starter/commit/f3146a51b5540dbcc43fa32dbfa0ed869ecb6eb7))

### Features

- Generate base workflow
  ([`21fd7e4`](https://github.com/fleetingbytes/ci-starter/commit/21fd7e46645c758c6746fc88b784902704346054))

### Refactoring

- Remove redundant mark to use an autouse fixture
  ([`38848bb`](https://github.com/fleetingbytes/ci-starter/commit/38848bbf1d7f33c370276404a80c545a10675c09))

### Testing

- Correct imports
  ([`e160b7c`](https://github.com/fleetingbytes/ci-starter/commit/e160b7c000cad9c7a5a8b762e689027d66a172b6))

- Move come constants to ci_starter.constants
  ([`726ec4a`](https://github.com/fleetingbytes/ci-starter/commit/726ec4a52162a30993a7335125baa4078657d951))

- Move to_yaml to utils as from_yaml
  ([`601999f`](https://github.com/fleetingbytes/ci-starter/commit/601999f7bb2b3a1af63e46b515a0d714a671025e))


## v0.6.3 (2025-09-30)

### Refactoring

- Simplify init, improve readability
  ([`f861b20`](https://github.com/fleetingbytes/ci-starter/commit/f861b20ac077e1e9d471300efd650e7dd37ab797))


## v0.6.2 (2025-09-30)

### Refactoring

- Remove the need of manually updating self.items
  ([`688f832`](https://github.com/fleetingbytes/ci-starter/commit/688f8325609cc5fe426f84b526cbf014307fb388))


## v0.6.1 (2025-09-30)

### Bug Fixes

- Shift comment start if lenght of action text changes
  ([`d0e218f`](https://github.com/fleetingbytes/ci-starter/commit/d0e218fab5fc36e08bbceea85214c3b6e8621b5f))


## v0.6.0 (2025-09-30)

### Bug Fixes

- Deal with mystery offset only when setting action manually
  ([`abaa813`](https://github.com/fleetingbytes/ci-starter/commit/abaa813b57704096bc9d1de2c06d4fb41e5e2dd9))

### Code Style

- Update ruff rules
  ([`20da425`](https://github.com/fleetingbytes/ci-starter/commit/20da425d79f9aec1ec887ec44c2be1eac531da07))

### Features

- Changeable Action in Step
  ([`61d1985`](https://github.com/fleetingbytes/ci-starter/commit/61d19852ea1e5f2a4103862a0e29cf761b29d50c))

### Refactoring

- Remove obsolete code
  ([`5dda06d`](https://github.com/fleetingbytes/ci-starter/commit/5dda06d68d2acd0d671a335e8338376d8c6d928b))


## v0.5.0 (2025-09-28)

### Chores

- Update click
  ([`af5aa99`](https://github.com/fleetingbytes/ci-starter/commit/af5aa99da7f812e52336c562505c9ebdba634886))

### Continuous Integration

- Really test tag and comment
  ([`a4f49ce`](https://github.com/fleetingbytes/ci-starter/commit/a4f49ceb8515bb5952f530e56d7cb5e05291d52d))

- Test tag and comment
  ([`8b5b3fa`](https://github.com/fleetingbytes/ci-starter/commit/8b5b3fa27a5812310be56657daa4a78389786ea2))

- Test tagging actions
  ([`9b0baa2`](https://github.com/fleetingbytes/ci-starter/commit/9b0baa20eb4ad9b991efc61ab7b871fe3104e787))

### Features

- Add Step and Action objects for yaml parsing and dumping
  ([`101a358`](https://github.com/fleetingbytes/ci-starter/commit/101a3585fb3d0598777eb36bdd72e2aee0cbed54))

### Testing

- Learn to use the ruamel.yaml dependency
  ([`d000781`](https://github.com/fleetingbytes/ci-starter/commit/d0007817430805ff0905c40b0f5c5778442734d4))

- Parse step, but don't use Action class
  ([`fcf6f3b`](https://github.com/fleetingbytes/ci-starter/commit/fcf6f3bbb9ab0e83ed20dd17cf5ce72879f81d02))

- Parse step, use Action class
  ([`2fe4a3b`](https://github.com/fleetingbytes/ci-starter/commit/2fe4a3bf42fe70e76d523a9d88439e54f5845698))

- Remove action tag with which github cannot deal
  ([`de767e5`](https://github.com/fleetingbytes/ci-starter/commit/de767e520f0806a36f2f8280a5771d82338a5ab9))

- Remove obsolete tests
  ([`1c17f57`](https://github.com/fleetingbytes/ci-starter/commit/1c17f57344c9a0e6a19ada4db0de4eb5e7523dc0))


## v0.4.4 (2025-09-20)

### Chores

- Update ruff
  ([`4eac6cf`](https://github.com/fleetingbytes/ci-starter/commit/4eac6cf7142483a3c59dc37eb950174cf4175243))

### Refactoring

- Make get_asset accept strings
  ([`b867453`](https://github.com/fleetingbytes/ci-starter/commit/b8674534c5deea7111f23d8703a651844d743ba7))


## v0.4.3 (2025-09-20)

### Bug Fixes

- **docs**: Use new workflow name in readme
  ([`585df52`](https://github.com/fleetingbytes/ci-starter/commit/585df52e6ccc4177b3b38a04e953723701261df1))


## v0.4.2 (2025-09-19)

### Bug Fixes

- **test**: Hardcode entry point name
  ([`3d09dce`](https://github.com/fleetingbytes/ci-starter/commit/3d09dce94447ede1511aaaba5de11f5581a15c60))

### Testing

- Refactor fixtures
  ([`3aa03ec`](https://github.com/fleetingbytes/ci-starter/commit/3aa03ec83e74ffcfc2cf2c9779d7f8c77cea31b3))

- Rewrite cli tests
  ([`4e27f6f`](https://github.com/fleetingbytes/ci-starter/commit/4e27f6f2ceeac07e517cb05a16cc51b68ae1776b))


## v0.4.1 (2025-09-19)

### Bug Fixes

- AttributeError
  ([`44a7bf4`](https://github.com/fleetingbytes/ci-starter/commit/44a7bf4889597e7def059f5e838932307b374beb))

### Refactoring

- Introduce contracts and base classes
  ([`eeac570`](https://github.com/fleetingbytes/ci-starter/commit/eeac5700412b1c3a08e5793d219587b3e67638e8))


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
