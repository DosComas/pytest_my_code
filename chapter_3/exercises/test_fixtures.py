import pytest


@pytest.fixture(scope='module')
def dict_prices():
    """Returns a dictionary of prices that can be modified by functions"""
    return {'price1': 93, 'price2': 64, 'price3': 74}


@pytest.fixture()
def list_parts():
    """Yields a list of parts that cannot be modified by functions"""
    print('---Before the \'yield\'')
    yield ['part1', 'part2', 'part3']
    print('---After the \'yield\'')


def test_price1(dict_prices):
    assert dict_prices['price1'] == 93


def test_prices_total_before(dict_prices):
    assert sum(dict_prices.values()) == 231


def test_price1_change(dict_prices):
    dict_prices['price1'] = 193
    assert dict_prices['price1'] == 193


def test_prices_total_after(dict_prices):
    assert sum(dict_prices.values()) == 331


def test_part1_removal(list_parts):
    list_parts.remove('part1')
    assert len(list_parts) == 2


def test_parts_quantity(list_parts):
    assert len(list_parts) == 3
