import threading
from typing import Callable


def set_interval(func: Callable, sec: int):
    def func_wrapper():
        func()
        set_interval(func, sec)

    t = threading.Timer(sec, func_wrapper)
    t.start()

    return t
