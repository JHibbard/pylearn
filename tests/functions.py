from pylearn.functions import add, filter_even


def test_add():
    assert add(1, 3) == 4


def test_filter_even():
    assert filter_even([*range(5)]) == [0, 2]
