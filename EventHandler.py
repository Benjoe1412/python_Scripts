# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 16:28:33 2020

@author: Benjoe
"""

import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler


def on_created(event):
    print(f"hey, {event.src_path[2:]} has been created!")
    #doiT.doDaWork(event.src_path[2:])
def on_modified(event):
    print(f"hey buddy, {event.src_path[2:]} has been modified")
    doiT.doDaWork(event.src_path[2:])
    
if __name__ == "__main__":
    patterns = "*.MP4"
    ignore_patterns = ""
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)
    print('fired!')
    my_event_handler.on_created = on_created
    my_event_handler.on_modified = on_modified
    path = "."
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
    



    