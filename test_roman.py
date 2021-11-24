from roman import to_roman, from_roman


def test_all_from_and_to_are_matching():
    for i in range(1, 3001):
        assert from_roman(to_roman(i)) == i


def test_1878_to_roman():
    assert to_roman(1878) == 'MDCCCLXXVIII'


def test_2999_to_roman():
    assert to_roman(2999) == 'MMCMXCIX'


def test_MCMLXXII_from_roman():
    assert from_roman('MCMLXXII') == 1972


def test_CMXCIV_from_roman():
    assert from_roman('CMXCIV') == 994
