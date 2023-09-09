import pytest


def calculate_speed(n: int, m: int, cookies: list[int]) -> int:
    return 0


@pytest.mark.parametrize('n,m,cookies,expected', [
    (3, 6, [4, 4, 4], 2),
    (3, 6, [4, 4, 5], 3),
    (3, 3, [6, 6, 8], 8),
])
def test_calculate_speed_given_cases(
        n: int,
        m: int,
        cookies: list[int],
        expected: int,
) -> None:
    assert calculate_speed(n, m, cookies) == expected
