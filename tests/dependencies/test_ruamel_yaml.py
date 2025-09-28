from io import StringIO
from textwrap import dedent

from ruamel.yaml.comments import Comment, CommentedMap, CommentedSeq
from ruamel.yaml.tokens import CommentToken

from ci_starter.asset_getter import get_asset
from ci_starter.step import Step


def test_parse_string_to_yaml(yaml_parser) -> None:
    string = get_asset("workflows/continuous-delivery.yml")
    data = yaml_parser.load(string)

    actual_top_level = tuple(data.keys())
    expected_top_level = ("name", "on", "permissions", "env", "jobs")
    assert actual_top_level == expected_top_level

    actual_jobs = tuple(data["jobs"].keys())
    expected_jobs = ("lint", "variables", "build", "test-e2e", "release", "publish")
    assert actual_jobs == expected_jobs

    assert isinstance(data["jobs"]["lint"], dict)
    assert isinstance(data["jobs"]["lint"]["steps"], list)
    assert isinstance(data["jobs"]["lint"]["steps"][0]["name"], str)
    assert isinstance(data["jobs"]["lint"]["steps"][0]["uses"], str)


def test_dump_yaml_to_string(yaml_parser) -> None:
    source = dedent(
        """\
        a:
        - b: this
          c: that

        - d: yon
          e: yonder
        """
    )

    expected = dedent(
        """\
        a:
        - b: whiz
          c: what

        - d: won
          e: wonder
        """
    )

    data = yaml_parser.load(source)

    data["a"][0]["b"] = "whiz"
    data["a"][0]["c"] = "what"
    data["a"][1]["d"] = "won"
    data["a"][1]["e"] = "wonder"

    actual = StringIO()
    yaml_parser.dump(data, actual)

    assert actual.getvalue() == expected


def test_parse_commented_map(yaml_parser) -> None:
    string = dedent("""\
                    steps:
                      - name: Setup | Checkout Repository
                        uses: actions/checkout@08c6903cd8c0fde910a37f88322edcfb5dd907a8  # v5.0.0
                    """)
    data = yaml_parser.load(string)

    assert isinstance(data, CommentedMap)
    assert isinstance(data.ca, Comment)
    assert isinstance(data.ca.items, dict)
    assert data.ca.items == {}

    assert isinstance(data["steps"], CommentedSeq)
    assert isinstance(data["steps"].ca, Comment)
    assert data["steps"].ca.items == {}

    assert isinstance(data["steps"][0], CommentedMap)
    assert isinstance(data["steps"][0]["name"], str)
    assert isinstance(data["steps"][0]["uses"], str)

    assert isinstance(data["steps"][0].ca, Comment)
    assert isinstance(data["steps"][0].ca.items, dict)
    items_length = len(data["steps"][0].ca.items)
    expected_items_length = 1
    assert items_length == expected_items_length

    assert isinstance(data["steps"][0].ca.items["uses"], list)
    list_length = len(data["steps"][0].ca.items["uses"])
    expected_list_length = 4
    assert list_length == expected_list_length

    assert data["steps"][0].ca.items["uses"][0] is None
    assert data["steps"][0].ca.items["uses"][1] is None
    assert isinstance(data["steps"][0].ca.items["uses"][2], CommentToken)
    assert data["steps"][0].ca.items["uses"][3] is None

    assert isinstance(data["steps"][0].ca.items["uses"][2].value, str)
    assert data["steps"][0].ca.items["uses"][2].value == "# v5.0.0\n"


def test_dump_commented_map(yaml_parser) -> None:
    string = dedent("""\
                    - name: Setup | Checkout Repository
                      uses: actions/checkout@08c6903cd8c0fde910a37f88322edcfb5dd907a8  # v5.0.0
                    """)
    data = yaml_parser.load(string)

    actual = StringIO()
    yaml_parser.dump(data, actual)

    expected = string
    assert actual.getvalue() == expected


def test_parse_step(step_parser) -> None:
    string = dedent("""\
                    steps:
                    - !step
                      name: Step1
                      uses: test_user/test_repo@0cafe  # v1.2.3
                    """)
    data = step_parser.load(string)

    assert isinstance(data["steps"][0], Step)
    assert isinstance(data["steps"][0].yaml_tag, str)
    assert data["steps"][0].yaml_tag == "!step"


def test_parse_step_roundtrip(step_parser) -> None:
    string = dedent("""\
                    steps:
                    - !step
                      name: Step1
                      uses: test_user/test_repo@0cafe  # v1.2.3
                    """)
    data = step_parser.load(string)

    actual = StringIO()
    step_parser.dump(data, actual)

    expected = string
    assert actual.getvalue() == expected
