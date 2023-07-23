from main import add

import pytest
import sys


def test_add():
    assert add(1, 2) == 3


if __name__ == "__main__":
    # test_add()
    sys.exit(pytest.main(sys.argv[1:]))
