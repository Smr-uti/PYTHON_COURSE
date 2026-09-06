from threading import Thread, Semaphore
import time

sem_obj=Semaphore(3)

def display():
    sem_obj.acquire()
    time.sleep(1)
    print("Task is done")
    sem_obj.release()

Thread=[Thread(target=display) for _ in range(6)]
for t in Threads:
    t.start()