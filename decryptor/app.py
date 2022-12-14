import base64
import logging
import os
import subprocess
import sys
import time

from AesDecryptor import AesDecryptor
from RotDecryptor import RotDecryptor
from watchdog.events import PatternMatchingEventHandler
from watchdog.observers import Observer


def on_created(event):
    src_path = event.src_path

    if src_path.find("filekey") == -1:
        print("A file named '" + os.path.basename(src_path) + "' is received.")
        # aesDecrypt(src_path)

        key_path = "/var/sftp/files/filekey.key"
        with open(key_path, "rb") as filekey:
            key = filekey.read()

        # delete key file
        os.remove(key_path)

        # print("key: ", key)
        if key == "13":
            RotDecryptor.run(src_path)
        else:
            AesDecryptor.run(src_path, key)


if __name__ == "__main__":
    print("Server monitoring is running...")
    patterns = ["*"]
    ignore_patterns = None
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(
        patterns,
        ignore_patterns,
        ignore_directories,
        case_sensitive
    )

    my_event_handler.on_created = on_created

    path = "/var/sftp/"
    go_recursively = True
    my_observer = Observer()
    my_observer.schedule(my_event_handler, path, recursive=go_recursively)

    my_observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        my_observer.stop()
        my_observer.join()
