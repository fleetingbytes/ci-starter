from re import compile
from typing import Self

from ruamel.yaml.constructor import Constructor
from ruamel.yaml.nodes import ScalarNode
from ruamel.yaml.representer import Representer
from ruamel.yaml.tokens import CommentToken
from semver import VersionInfo

from .errors import ActionNotParsableError


class Action:
    yaml_tag = "!action"
    action_pattern = compile(r"(?P<user>[\w_-]+)/(?P<repo>[\w_-]+)@(?P<commit>[\S]+)")

    def __init__(
        self,
        user: str,
        repo: str,
        commit: str,
        version: VersionInfo | None = None,
        comment: list[CommentToken, None] | None = None,
    ) -> None:
        self.user = user
        self.repo = repo
        self.commit = commit
        self.version = version
        self.comment = comment

    @classmethod
    def to_yaml(cls, representer: Representer, node: Self):
        tag = cls.yaml_tag
        value = f"{node.user}/{node.repo}@{node.commit}"
        # There is no way how we can pass the node.comment to the representer
        return representer.represent_scalar(tag, value)

    @classmethod
    def from_yaml(cls, constructor: Constructor, node: ScalarNode):
        version = None
        if node.comment:
            semver_text = next(iter(node.comment)).value.strip(" #v\n")
            version = VersionInfo.parse(semver_text)

        match = cls.action_pattern.search(node.value)
        if not match:
            raise ActionNotParsableError(node.value)

        return cls(**match.groupdict(), version=version, comment=node.comment)
