from dataclasses import dataclass
from typing import Iterable


@dataclass
class Vector:
    row: int | float
    col: int | float

    def __add__(self, other):
        return Vector(self.row + other.row, self.col + other.col)

    def __sub__(self, other):
        return Vector(self.row - other.row, self.col - other.col)

    def __iter__(self):
        yield self.row
        yield self.col

    def __hash__(self):
        return hash((self.row, self.col))

    def __eq__(self, other):
        return (self.row == other.row) and (self.col) == (other.col)


def manhattan(
    vector1: Iterable[int | float], vector2: Iterable[int | float]
) -> int | float:
    r1, c1 = vector1
    r2, c2 = vector2
    return abs(r1 - r2) + abs(c1 - c2)
