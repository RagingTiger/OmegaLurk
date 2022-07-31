import streamlit as st

# custom libs
from lurk import constants
from lurk import engine
from lurk import process

# configuring page
st.set_page_config(
     initial_sidebar_state="collapsed",
     page_icon=':shark:',
     page_title='OmegaLurk'
)

# creating sidebar
with st.sidebar:
    # set title
    st.title('Configuration')

    # select boards for ingestion
    st.header('4Chan Boards')
    boards = st.multiselect(
        'Selected boards for ingestion',
        sorted(constants.BOARDS),
        ['pol']
    )

    # set ingestion frequency
    st.header('Ingestion Frequency')
    ingestion_frequency = st.selectbox(
        'Select frequency (in hours)',
        (1, 3, 6, 12, 24),
        4
    )
    ingestion_starttime = st.time_input('Select start time (in millitary time)')

    # set history storage length
    st.header('History Storage Size')
    history_size = st.number_input(
        'Max number of extraction results saved on disk',
        min_value=1,
        value=4
    )

# set title
st.title('Omega Lurk')

# run demo
st.write(f'Boards Selected: {"/".join(boards)}')
demo = st.button('Run Demo')

# now summarize
if demo:
    # start and wait for finish
    with st.spinner('Extracting information ...'):
        extraction_results = process.deploy(
            engine.extractor,
            boards=boards
        )
        st.write(extraction_results)
