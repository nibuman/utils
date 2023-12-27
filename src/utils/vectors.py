from dataclasses import dataclass
from typing import Iterable
import numpy as np

vector_type = Iterable[list | float]
"""test"""


@dataclass
class Vector:
    row: int | float
    col: int | float

    def __add__(self, other):
        return Vector(self.row + other.row, self.col + other.col)

    def __sub__(self, other):
        return Vector(self.row - other.row, self.col - other.col)

    def __mul__(self, other: int | float):
        return Vector(self.row * other, self.col * other)

    def __rmul__(self, other: int | float):
        return self.__mul__(other)

    def __iter__(self):
        yield self.row
        yield self.col

    def __hash__(self):
        return hash((self.row, self.col))

    def __eq__(self, other):
        return (self.row == other.row) and (self.col == other.col)


def manhattan(vector1: vector_type, vector2: vector_type) -> int | float:
    """Computes the Manhattan distance between 2 vectors (the sum of the absolute differences of
    their respective Cartesian coordinates)"""
    r1, c1 = vector1
    r2, c2 = vector2
    return abs(r1 - r2) + abs(c1 - c2)


def shoelace(coordinates: Iterable[vector_type]) -> int | float:
    """The shoelace formula, also known as Gauss's area formula and the surveyor's formula, is a
    mathematical algorithm to determine the area of a simple polygon whose vertices are described by
    their Cartesian coordinates in the plane"""
    return (
        sum(
            np.linalg.det([[*p1], [*p2]])
            for p1, p2 in zip(coordinates, coordinates[1:] + [coordinates[0]])
        )
        / 2
    )
