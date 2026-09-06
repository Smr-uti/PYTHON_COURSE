import time
from threading import Thread

def display(message):
    for i in range(5):
        print(message)
        time.sleep(1)

t1=Thread(target=display,args=("Jai Ganesh",))
t2=Thread(target=display,args=("Jai Shree Ganesh",))

t1.start()
t2.start()