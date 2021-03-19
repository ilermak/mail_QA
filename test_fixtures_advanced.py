import pytest

import random


@pytest.fixture(scope='session')
def session_fixture():
    return random.randint(0, 100)


@pytest.fixture(scope='function')
def func_fixture(session_fixture):
    return session_fixture // 2


@pytest.fixture(scope='function')
def func_fixture2(session_fixture):
    return session_fixture // 5


