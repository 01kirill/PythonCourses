# net_proc.py
import time
import requests
from multiprocessing import Process

def fetch(url):
    return requests.get(url).status_code

def proc_target(url):
    fetch(url)

if __name__ == "__main__":
    N = 12
    urls = ["https://httpbin.org/get"] * N

    start = time.time()

    procs = []
    for u in urls:
        p = Process(target=proc_target, args=(u,))
        p.start()
        procs.append(p)

    for p in procs:
        p.join()

    end = time.time()
    print("Multiprocessing time:", end - start)
