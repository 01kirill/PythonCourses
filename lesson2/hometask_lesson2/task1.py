current_year = 2025
birth_year = ""
try:
    birth_year = int(input("Введите дату своего рождения: "))
    if birth_year > current_year:
        print("Некорректная дата рождения")
    else:
        print("Вам", current_year - birth_year, "лет")
except ValueError:
    print("Некорректный ввод")
