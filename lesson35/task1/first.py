import time

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

if __name__ == "__main__":
    N = 12
    inputs = [70_000 + i * 1_000 for i in range(N)]

    start = time.time()
    for n in inputs:
        work(n)
    end = time.time()

    print("Sequential time:", end - start)
