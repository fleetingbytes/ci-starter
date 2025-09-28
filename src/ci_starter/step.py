from typing import ClassVar, Self

from ruamel.yaml.comments import Comment, CommentedMap, comment_attrib
from ruamel.yaml.constructor import Constructor
from ruamel.yaml.nodes import MappingNode
from ruamel.yaml.representer import Representer
from ruamel.yaml.tokens import CommentToken

from .action import Action


class Step:
    yaml_tag: ClassVar[str] = "!step"

    def __init__(self, name: str, uses: Action, comment: list[CommentToken | None]) -> None:
        self.name = name
        self.uses = uses
        self.comment = comment
        setattr(self, comment_attrib, self.comment)
        self.items = self.value.items

    @property
    def value(self) -> dict:
        return {"name": self.name, "uses": self.uses}

    @classmethod
    def from_yaml(cls, constructor: Constructor, node: MappingNode) -> Self:
        comment = cls.get_action_comment(node)
        data = CommentedMap()
        constructor.construct_mapping(node, maptyp=data, deep=False)
        return cls(**data, comment=comment)

    @classmethod
    def get_action_comment(cls, node: MappingNode) -> list[CommentToken | None]:
        f = filter(lambda tupl: tupl[0].value == "uses", node.value)
        _, scalar_node = next(f)
        comments: list[CommentToken | None] = scalar_node.comment
        comment = Comment()
        comment._items = {"uses": [None, None, *comments]}
        return comment

    @classmethod
    def to_yaml(cls, representer: Representer, node: Self) -> MappingNode:
        tag = cls.yaml_tag
        result = representer.represent_mapping(tag, node)
        return result
