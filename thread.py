import threading
from time import sleep

def tarefa(tempo):
    sleep(tempo)
    print('finalizada')


t1 = threading.Thread(target=tarefa, args=(5,))
t1.start()

sleep(10)
print('Async')

t1.join()