from hello import hello


def test_hello():
    assert hello() == 'hello'
    assert hello() != 'goodbye'


def test_pytest():
    assert 1 not in [2, 3, 4]
    assert 'a' < 'b'
    assert 'fizz' in 'fizzbuzz'
