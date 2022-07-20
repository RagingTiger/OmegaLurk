import basc_py4chan
import typing


# declaring custom types
BoardGenerator = typing.Generator[basc_py4chan.Board, None, None]
BoardData = list[basc_py4chan.Thread]
IngestionGenerator = typing.Generator[BoardData, None, None]


def get_board_data(board_names: list[str]) -> BoardGenerator:
    """Take list of 4chan board names and yield Board objects."""
    # get board object
    for name in board_names:
        # get actual board object
        yield basc_py4chan.Board(name)


def ingestor(boards: BoardGenerator) -> IngestionGenerator:
    """Take generator of Board objects and yield lists of Thread objects."""
    # iterate through boards
    for data in boards:
        # now get all posts
        yield data.get_all_threads(expand=True)


def digestor(board_data: IngestionGenerator) -> basc_py4chan.Post:
    # for now just get first board
    sample_board = next(board_data)

    # now get first thread
    sample_thread = next(sample_board)

    # now get first post
    sample_post = sample_thread.all_posts.pop()

    # return first post
    return sample_post


def extractor(boards: list[str]) -> typing.Any:
    return digestor(ingestor(boards))
