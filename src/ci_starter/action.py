from re import compile
from typing import Self

from semver import VersionInfo

from .errors import ActionNotParsableError


class Action:
    PATTERN = compile(r"(?P<owner>[\w_-]+)/(?P<repo>[\w_-]+)@(?P<commit>[\S]+)")

    def __init__(self, owner: str, repo: str, commit: str, version: VersionInfo | None = None) -> None:
        self.owner: str = owner
        self.repo: str = repo
        self.commit: str = commit
        self.version: VersionInfo = version

    def to_text(self):
        text = f"{self.owner}/{self.repo}@{self.commit}"
        return text

    @classmethod
    def from_text(cls, text: str, version: VersionInfo | None = None) -> Self:
        match = cls.PATTERN.search(text)
        if not match:
            raise ActionNotParsableError(text)

        action = cls(**match.groupdict(), version=version)

        return action

    def __repr__(self) -> str:
        string = (
            f"{self.__class__.__name__}(user={self.user}, repo={self.repo}, "
            f"commit={self.commit}, version={self.version})"
        )
        return string

    def __len__(self) -> int:
        return len(self.to_text())
