import os
import logging


def test_app_path_exists(app_path):
    """Checking to see if fixture is returning an actual file."""
    # log app path
    logging.info(f'App Path: {app_path}')

    # check if file
    assert os.path.isfile(app_path)
