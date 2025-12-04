import time
import requests

def fetch(url):
    return requests.get(url).status_code

if __name__ == "__main__":
    N = 12
    urls = ["https://httpbin.org/get"] * N

    start = time.time()
    for u in urls:
        fetch(u)
    end = time.time()

    print("Sequential time:", end - start)
