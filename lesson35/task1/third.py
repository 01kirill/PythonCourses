import time
from multiprocessing import Process

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def work(x: int):
    primes = []
    for i in range(2, x):
        if is_prime(i):
            primes.append(i)
    return primes

def proc_target(x):
    work(x)

if __name__ == "__main__":
    import os
    N = os.cpu_count()
    inputs = [75_000 + i * 1_000 for i in range(N)]

    procs = []
    start = time.time()

    for x in inputs:
        p = Process(target=proc_target, args=(x,))
        p.start()
        procs.append(p)

    for p in procs:
        p.join()

    end = time.time()
    print("Multiprocessing time:", end - start)
