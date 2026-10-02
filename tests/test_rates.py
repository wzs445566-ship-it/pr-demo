import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import pytest

from fx import convert


def test_convert_usd_to_cny():
    result = convert(100, "USD", "CNY", rate=7.2)
    assert result == 720.0


def test_convert_same_currency_is_identity():
    result = convert(50, "USD", "USD", rate=7.2)
    assert result == 50.0


def test_convert_zero_amount():
    result = convert(0, "USD", "CNY", rate=7.2)
    assert result == 0.0


def test_convert_negative_amount_raises():
    with pytest.raises(ValueError):
        convert(-10, "USD", "CNY", rate=7.2)


def test_convert_nonpositive_rate_raises():
    with pytest.raises(ValueError):
        convert(100, "USD", "CNY", rate=0)
