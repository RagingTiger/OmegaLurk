import types
from lurk import engine


# mocking
class FakeThread(engine.basc_py4chan.Thread):
    """Mock 4chan thread."""
    def __init__(self, name):
        self.name = name
        self.id = hash(id)


def mock_get_all_threads(self, expand=False) -> engine.BoardData:
    """Mock list of threads i.e. BoardData type."""
    return [FakeThread(self.name)]


# tests
def test_get_board_data_return_type(board_names):
    """Test the return type for get_board_data function."""
    # get boards
    boards = engine.get_board_data(board_names)

    # assert type is Generator
    assert isinstance(boards, types.GeneratorType)

    # assert yield type is Board
    assert isinstance(next(boards), engine.basc_py4chan.Board)


def test_get_ingestor_return_type(mocker, board_names):
    """Test return type for ingestor function."""
    # time to mock get all threads in ingestor
    mocker.patch(
        'lurk.engine.basc_py4chan.Board.get_all_threads',
        mock_get_all_threads
    )

    # get ingestor
    ingestor = engine.ingestor(engine.get_board_data(board_names))

    # assert type is BoardGenerator
    assert isinstance(ingestor, types.GeneratorType)

    # assert yield type is Board
    board_data = next(ingestor)
    assert isinstance(board_data, list)

    # assert 4chan Thread type in board_data
    assert isinstance(board_data.pop(), FakeThread)
