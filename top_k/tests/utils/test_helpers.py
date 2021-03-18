import pytest

from utils.helpers import eval_bool


@pytest.mark.parametrize(
    "value, expected", [
        ("53", False),
        ('1', True),
        ("YEs", True),
        ("true", True),
    ])
def test_eval_bool(value, expected: bool):

    assert eval_bool(value) is expected
