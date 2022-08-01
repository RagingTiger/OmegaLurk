import requests


def test_server_up(streamlit_server):
    """Simple test to see if Streamlit Server is up."""
    assert streamlit_server.getinfo('streamlit_app').isrunning()


def test_server_reachable(server_address):
    """Test if Streamlit server can be reached at server_address."""
    # send streamlit server GET request
    response = requests.get(server_address)

    # confirm 200 status code
    assert response.status_code == 200
