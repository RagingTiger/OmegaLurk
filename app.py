import basc_py4chan
from multiprocessing import Queue, Process
import streamlit as st

# custom libs
from packages import constants

# funcs
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

def extractor(boards):
    return digestor(ingestor(boards))

def get_process_results(queue, func, **parameters):
    # now run inference and store result in IPC queue
    queue.put(func(**parameters))

def deploy_process(**parameters):
    # setup process queue
    proc_queue = Queue()

    # setup process
    deploy_proc = Process(
        target=get_process_results,
        args=[proc_queue, extractor],
        kwargs=parameters
    )

    # now start and wait
    deploy_proc.start()
    result = proc_queue.get()
    deploy_proc.join()

    # return contents of queue
    return result

# configuring page
st.set_page_config(
     initial_sidebar_state="collapsed"
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

# set title
st.title('Omega Lurk')

# run demo
st.write(f'Boards Selected: {"/".join(boards)}')
demo = st.button('Run Demo')

# now summarize
if demo:
    # start and wait for finish
    with st.spinner('Extracting information ...'):
        extraction_results = deploy_process(
            boards=boards
        )
        st.write(extraction_results)
