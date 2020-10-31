from multiprocessing import Process
import os
import time


def sq_nums():
    for i in range(100):
        i**2
        time.sleep(0.1)


processes = []
num_processes = os.cpu_count()

for _ in range(num_processes):
    p = Process(target=sq_nums)
    processes.append(p)

for p in processes:
    p.start()

for p in processes:
    p.join()

print("End Main")