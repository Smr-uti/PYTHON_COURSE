
from threading import Thread, RLock
import time

RLock_obj=RLock()

def display():
    RLock_obj.acquire()
    time.sleep(1)
    print("Task done")
    RLock_obj.release()

Threads=[Thread(target=display) for _ in range(6)]
for t in Threads:
    t.start()