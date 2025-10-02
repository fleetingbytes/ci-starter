from dataclasses import dataclass
from io import StringIO
from string import ascii_uppercase


@dataclass
class Comparator:
    asset: str
    rendered: str

    def compare_lines(self) -> None:
        asset = StringIO(self.asset)
        rendered = StringIO(self.rendered)
        for line_number, (asset_line, rendered_line) in enumerate(
            zip(map(str.strip, asset), map(str.strip, rendered), strict=True), start=1
        ):
            if asset_line and self.starts_with_uppercase(asset_line):
                continue
            assert asset_line == rendered_line, f"line {line_number}: {asset_line!r} != {rendered_line!r}"

    @staticmethod
    def starts_with_uppercase(line: str) -> bool:
        if not line:
            return False
        initial_letter = next(iter(line))
        return initial_letter in ascii_uppercase
