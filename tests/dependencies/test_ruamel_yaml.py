from io import StringIO
from textwrap import dedent

from ruamel.yaml import YAML

from ci_starter.asset_getter import get_asset


def test_parse_string_to_yaml() -> None:
    string = get_asset("workflows/continuous-delivery.yml")
    yaml = YAML()
    data = yaml.load(string)

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


def test_dump_yaml_to_string() -> None:
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

    yaml = YAML()
    data = yaml.load(source)

    data["a"][0]["b"] = "whiz"
    data["a"][0]["c"] = "what"
    data["a"][1]["d"] = "won"
    data["a"][1]["e"] = "wonder"

    actual = StringIO()
    yaml.dump(data, actual)

    assert actual.getvalue() == expected
