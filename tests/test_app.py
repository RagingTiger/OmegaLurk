import os
import logging
import requests


def test_app_path_exists(app_path):
    """Checking to see if fixture is returning an actual file."""
    # log app path
    logging.info(f'App Path: {app_path}')

    # check if file
    assert os.path.isfile(app_path)


def test_server_up(streamlit_server):
    """Simple test to see if Streamlit Server is up."""
    assert streamlit_server.getinfo('streamlit_app').isrunning()


def test_server_reachable(streamlit_server):
    """Test if Streamlit server can be reached at http://localhost:8501."""
    # send streamlit server GET request
    response = requests.get('http://localhost:8501')

    # confirm 200 status code
    assert response.status_code == 200
