import pytest
from lurk import constants


@pytest.fixture
def board_names():
    """Fixture for returning all 4chan board names."""
    return constants.BOARDS
