import time
from threading import Thread, RLock
import threading

rlock = RLock()

def inner_display(message):
    rlock.acquire()
    try:
        print(f"{threading.current_thread().name} entered inner_display")
        for i in range(3):
            print(message)
            time.sleep(1)
    finally:
        rlock.release()

def display(message):
    rlock.acquire()
    try:
        print(f"{threading.current_thread().name} entered display")
        # Calling another function that also acquires the same RLock
        inner_display(message)
    finally:
        rlock.release()

t1 = Thread(target=display, args=("Jai Ganesh",), name="Thread-1")
t2 = Thread(target=display, args=("Jai Shree Ganesh",), name="Thread-2")

t1.start()
t2.start()

t1.join()
t2.join()