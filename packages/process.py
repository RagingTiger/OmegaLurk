import multiprocessing
import typing


def get_process_results(queue: multiprocessing.Queue,
                        func: typing.Callable,
                        **parameters: dict[str, typing.Any]) -> None:
    # now run inference and store result in IPC queue
    queue.put(func(**parameters))


def deploy(func: typing.Callable,
           **parameters: dict[str, typing.Any]) -> typing.Any:
    # setup process queue
    proc_queue = multiprocessing.Queue()

    # setup process
    deploy_proc = multiprocessing.Process(
        target=get_process_results,
        args=[proc_queue, func],
        kwargs=parameters
    )

    # now start and wait
    deploy_proc.start()
    result = proc_queue.get()
    deploy_proc.join()

    # return contents of queue
    return result
