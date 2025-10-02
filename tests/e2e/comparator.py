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

        stripped_lines = zip(map(str.strip, asset), map(str.strip, rendered), strict=True)

        for line_number, (asset_line, rendered_line) in enumerate(stripped_lines, start=1):
            if self.is_env_var_definition(asset_line):
                continue
            assert asset_line == rendered_line, f"line {line_number}: {asset_line!r} != {rendered_line!r}"

    @staticmethod
    def is_env_var_definition(line: str) -> bool:
        if not line:
            return False
        initial_letter = next(iter(line))
        return initial_letter in ascii_uppercase
