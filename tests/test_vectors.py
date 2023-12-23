import utils.vectors
import pytest
from utils.vectors import Vector as V


@pytest.mark.parametrize(
    ["vec1", "vec2", "vec3"],
    [
        [(0, 0), (1, 2), (1, 2)],
        [(-10, -10), (2, 2), (-8, -8)],
    ],
)
def test_Vector_add(vec1, vec2, vec3):
    assert V(*vec1) + V(*vec2) == V(*vec3)


def test_Vector_add_float():
    vec1 = V(1.2, -0.5)
    vec2 = V(-3.4, 8.6)
    expected_answer = V(-2.2, 8.1)
    answer = vec1 + vec2
    r, c = answer
    expected_r, expected_c = expected_answer
    assert r == pytest.approx(expected_r) and c == pytest.approx(expected_c)


def test_Vector_equality():
    new_vector = V(12, -5) + V(6, 20)
    assert new_vector == V(18, 15)


def test_Vector_sets():
    vec_set = set()
    vec_set.add(V(1, 0))
    vec_set.add(V(1, 2))
    vec_set.add(V(0, 1))
    vec_set.add(V(2, 1))
    assert len(vec_set) == 4

    # Length shouldn't change when a duplicate is added
    vec_set.add(V(2, 1))
    assert len(vec_set) == 4


def test_Vector_dict_key():
    vec_map = {V(1, 0): "a", V(2, 1): "b", V(1, 2): "c"}
    assert vec_map[V(2, 1)] == "b"
    vec_map[V(2, 1)] = "d"
    assert vec_map[V(2, 1)] == "d"


@pytest.mark.parametrize(
    ["vec1", "vec2", "distance"],
    [
        [(0, 0), (10, 10), 20],
        [(0, 0), (-10, -10), 20],
        [(0, 0), (-10, 10), 20],
        [(-150, 200), (55, -8), 413],
        [(1.2, -0.5), (-3.8, 8.1), 13.6],
    ],
)
def test_manhattan(vec1, vec2, distance):
    # Check with tuple arguments
    assert utils.vectors.manhattan(vec1, vec2) == distance

    # Check with Vector arguments
    assert utils.vectors.manhattan(V(*vec1), V(*vec2)) == distance
