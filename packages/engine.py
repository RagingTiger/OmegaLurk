import basc_py4chan

def ingestor(boards: list[str]):
    # iterate through boards
    for name in boards:
        # get board data
        data = basc_py4chan.Board(name)

        # now get all posts
        yield data.get_all_threads(expand=True)

def digestor(board_data: list[list[basc_py4chan.Thread]]):
    # for now just get first board
    sample_board = next(board_data)

    # now get first thread
    sample_thread = next(sample_board)

    # now get first post
    sample_post = sample_thread.all_posts.pop()

    # return first post
    return sample_post

def extractor(boards: list[str]):
    return digestor(ingestor(boards))
