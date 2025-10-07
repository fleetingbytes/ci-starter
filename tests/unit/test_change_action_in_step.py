from io import StringIO
from textwrap import dedent

from semver import VersionInfo

from ci_starter.action import Action


def test_change_action_in_step_and_shift_comment_column(step_parser) -> None:
    string = dedent("""\
                    steps:
                    - !step
                      name: Step1
                      uses: test_user/test_repo@0cafe  # v1.2.3
                    """)
    data = step_parser.load(string)
    step = data["steps"][0]

    action = Action(owner="new_user", repo="new_repo", commit="7ea42", version=VersionInfo.parse("4.5.6"))
    step.uses = action

    actual = StringIO()
    step_parser.dump(data, actual)

    expected = dedent("""\
                    steps:
                    - !step
                      name: Step1
                      uses: new_user/new_repo@7ea42  # v4.5.6
                    """)
    assert actual.getvalue() == expected
