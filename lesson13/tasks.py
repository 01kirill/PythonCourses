orders = ["Заказ #1001", "Заказ #1002", "Заказ #1003"]

iterator = iter(orders)
try:
    while True:
        print(next(iterator))
except StopIteration:
    print("Все заказы обработаны")
