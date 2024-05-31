from andrew_utils import time_to_seconds


def test_time_to_seconds():
    assert time_to_seconds('00:59:59') == 3599
    assert time_to_seconds('00:00:59') == 59
    assert time_to_seconds('00:00:59.955') == 59.955
    assert time_to_seconds('01:59:59.955') == 7199.955
    assert time_to_seconds('00:00:01') == 1
    assert time_to_seconds('00:00:01.006') == 1.006
    assert time_to_seconds('00:00:01.0061') == 1.0061
    assert time_to_seconds('00:00:01.0065') == 1.0065

