from dataclasses import dataclass
from io import StringIO


@dataclass
class Comparator:
    asset: str
    rendered: str

    def compare_lines(self) -> None:
        asset = StringIO(self.asset)
        rendered = StringIO(self.rendered)
        for asset_line, rendered_line in zip(map(str.strip, asset), map(str.strip, rendered), strict=True):
            assert asset_line == rendered_line, f"{asset_line!r} != {rendered_line!r}"
