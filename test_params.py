import random

import pytest

@pytest.fixture(scope='function', param=list(range(10)))
def fixture(request):
    if re
    return random.randint(0, 100)


@pytest.mark.parametrize('i', list(range(10)))
def test(i, fixture):
    print(fixture)
    assert i % 2 == 0
