import logging
import os
import pytest
from lurk import constants
from xprocess import ProcessStarter


@pytest.fixture(scope="session")
def app_path():
    """Fixture to get path of Streamlit app file."""
    # get current working dir
    cwd = os.path.dirname(os.path.abspath(__file__))

    # now work on it to get parent containing app
    return '/'.join(cwd.split('/')[:-1]) + '/' + 'app.py'


@pytest.fixture
def server_address():
    """Fixture for Streamlit server adress."""
    return 'http://127.0.0.1:8501'


@pytest.fixture
def board_names():
    """Fixture for returning all 4chan board names."""
    return constants.BOARDS


@pytest.fixture(scope="session")
def streamlit_server(xprocess, app_path):
    """Fixture to startup Streamlit server and run for entire session."""
    class Starter(ProcessStarter):
        # xprocess will now attempt to
        # clean up for you upon interruptions
        terminate_on_interrupt = True

        # will wait for 10 seconds before timing out
        timeout = 10

        # startup pattern
        pattern = "You can now view your Streamlit app in your browser."

        # log app path
        logging.info(f'App path: {app_path}')

        # command to start process
        args = [
            'streamlit',
            'run',
            app_path,
            '--logger.level=debug',
            '--server.fileWatcherType=none',
            '--client.caching=False'
        ]

    # ensure process is running and return its logfile
    xprocess.ensure("streamlit_app", Starter)

    # return xprocess object
    yield xprocess

    # clean up whole process tree afterwards
    xprocess.getinfo("streamlit_app").terminate()
