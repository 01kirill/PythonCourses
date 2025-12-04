import time
import threading

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

def thread_target(x):
    work(x)

if __name__ == "__main__":
    N = 12
    inputs = [70_000 + i * 1_000 for i in range(N)]

    threads = []
    start = time.time()

    for x in inputs:
        t = threading.Thread(target=thread_target, args=(x,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    end = time.time()
    print("Threading time:", end - start)
