try:
   number = int(input("Enter a number: "))
   result = 100 / number
except (ValueError, ZeroDivisionError):
   print("Invalid input")
   
import requests

try:
    url = "https://jsonplaceholder.typicode.com/posts/1"
    session = requests.Session()
    response = session.get(url, timeout=5)
except requests.exceptions.Timeout:
    pass
except requests.exceptions.ConnectionError:
    pass
else:
    print("Все гуд")
    print(response.json())
finally:
    print("Конец")
    session.close()

def sqrt(x):
    assert x >= 0
    return x ** 0.5

print(sqrt(-4))
