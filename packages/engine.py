import basc_py4chan
import typing

# declaring custom types
BoardData = list[basc_py4chan.Thread]
IngestionGenerator = typing.Generator[BoardData, None, None]


def ingestor(boards: list[str]) -> IngestionGenerator:
    # iterate through boards
    for name in boards:
        # get board data
        data = basc_py4chan.Board(name)

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
