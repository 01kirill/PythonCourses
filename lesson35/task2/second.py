import time
import requests
import threading

def fetch(url):
    return requests.get(url).status_code

def thread_target(url):
    fetch(url)

if __name__ == "__main__":
    N = 12
    urls = ["https://httpbin.org/get"] * N

    start = time.time()

    threads = []
    for u in urls:
        t = threading.Thread(target=thread_target, args=(u,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    end = time.time()
    print("Threading time:", end - start)
