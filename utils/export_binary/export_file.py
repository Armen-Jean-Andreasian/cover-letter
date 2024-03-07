from typing import Callable
import threading


def export_file(io_bound_function: Callable, *func_args, **func_kwargs) -> None:
    """
    Exports a binary file using threading
    :param io_bound_function: function to call
    """
    save_file_thread = threading.Thread(target=io_bound_function, args=func_args, kwargs=func_kwargs)
    save_file_thread.start()
    save_file_thread.join()
    return None
