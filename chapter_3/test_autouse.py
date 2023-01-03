import pytest
import time


@pytest.fixture(autouse=True, scope='session')
def footer_session_scope():
    """Report the time at the end of a session"""
    yield
    now = time.time()
    print('--\nfinished : {}\n----------------'.format(
        time.strftime('%d %b %X', time.localtime(now))))


@pytest.fixture(autouse=True)
def footer_function_scope():
    """Report test duration after each function"""
    start = time.time()
    yield
    stop = time.time()
    delta = stop - start
    print('\ntest duration : {:0.3} seconds'.format(delta))


def test_1():
    """Simulate long-ish running test"""
    time.sleep(1)


def test_2():
    """Simulate lightly longer test"""
    time.sleep(1.23)
