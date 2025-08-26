"""
Сделать декоратор, который измеряет время,
затраченное на выполнение декорируемой функции.
"""

import time

def func_time_check(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"Время выполнения функции: {end - start:.6f} секунд.")
    return wrapper

@func_time_check
def count_to_billion_and_sleep_3s():
    count = 0
    for _ in range(1000000):
        count += 1
    time.sleep(3)

count_to_billion_and_sleep_3s()
