import pytest
from lurk import constants
from xprocess import ProcessStarter


@pytest.fixture
def board_names():
    """Fixture for returning all 4chan board names."""
    return constants.BOARDS


@pytest.fixture(scope="session")
def streamlit_server(xprocess):
    """Fixture to startup Streamlit server and run for entire session."""
    class Starter(ProcessStarter):
        # xprocess will now attempt to
        # clean up for you upon interruptions
        terminate_on_interrupt = True

        # will wait for 10 seconds before timing out
        timeout = 10

        # startup pattern
        pattern = "You can now view your Streamlit app in your browser."

        # command to start process
        args = ['streamlit', 'run', '/OmegaLurk/app.py']

    # ensure process is running and return its logfile
    xprocess.ensure("streamlit_app", Starter)

    # return xprocess object
    yield xprocess

    # clean up whole process tree afterwards
    xprocess.getinfo("streamlit_app").terminate()
