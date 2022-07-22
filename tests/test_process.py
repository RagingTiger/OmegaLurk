from lurk import process


# tests
def test_queue():
    """Make sure multiprocessing.Queue works as it should."""
    # run deploy func on simple builtin pow func
    results = process.deploy(
        pow,
        base=2,
        exp=2,
    )

    # confirm returned results match
    assert results == pow(2, 2)
