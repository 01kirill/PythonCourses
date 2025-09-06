"""
Пункты задания:
0. Есть данные в формате JSON – взять с диска с
исходными данными.
1. Реализовать функцию, которая считает данные из
исходного JSON-файла и преобразует их в формат CSV
2. Реализовать функцию, которая сохранит данные в
CSV-файл (данные должны сохраняться независимо от их
количества – если добавить в исходный JSON-файл ещё
одного сотрудника, работа программы не должна
нарушаться).
3. Реализовать функцию, которая добавит информацию о
новом сотруднике в JSON-файл. Пошагово вводятся все
необходимые данные о сотруднике, формируются данные
для записи.
4. Такая же функция для добавления информации о
новом сотруднике в CSV-файл.
5. Реализовать функцию, которая выведет информацию
об одном сотруднике по имени. Имя для поиска вводится с
клавиатуры.
6. Реализовать функцию фильтра по языку: с клавиатуры
вводится язык программирования, выводится список всех
сотрудников, кто владеет этим языком программирования.
7. Реализовать функцию фильтра по году: ввести с
клавиатуры год рождения, вывести средний рост всех
сотрудников, у которых год рождения меньше заданного.
8. Программа должна представлять собой интерактив –
пользовательское меню с возможностью выбора
определённого действия (действия – функции из
предыдущих пунктов + выход из программы). Пока
пользователь не выберет выход из программы, должен
предлагаться выбор следующего действия.
"""

import csv
from datetime import datetime, date
import json
import re

csv_file_path = "employees.csv"
json_file_path = "employees.json"

json_data = []
csv_data = []

def read_json_file(json_file_path):
    with open(json_file_path, "r") as json_file:
        json_data = json.load(json_file)
    return json_data

def convert_json_to_csv(json_data):
    if len(json_data) > 0:
        csv_data = [[] for _ in range(len(json_data) + 1)]
        csv_data[0] = [key for key in json_data[0].keys()]
        for i in range(len(json_data)):
            csv_data[i + 1] = [value for value in json_data[i].values()]
        return csv_data
    else:
        return []

def write_csv_file(csv_data, csv_file_path):
    with open(csv_file_path, "w") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(csv_data)

def get_employee_info():
    print("\nВвод данных нового сотрудника")
    employee = dict()
    name = input("Введите имя и фамилию: ")
    if re.match(r"[A-Z][a-z]* [A-Z][a-z]*(-[A-Z][a-z]*)?", name):
        employee["name"] = name
    else:
        print("\nНекорректный ввод имени и фамилии")
        return None
    birthday = input("Введите дату рождения в формате ДД.ММ.ГГГГ: ")
    try:
        birthday = datetime.strptime(birthday, "%d.%m.%Y")
        if (datetime.now().year - birthday.year >= 18) and (birthday.year > 1900):
            employee["birthday"] = birthday.strftime("%d.%m.%Y")
        else:
            raise ValueError
    except ValueError:
        print("\nНеверный формат даты или неверный год рождения")
        return None
    try:
        height = int(input("Введите рост: "))
        if 140 < height < 250:
            employee["height"] = height
        else:
            raise ValueError
    except ValueError:
        print("\nНекорректный ввод роста")
        return None
    try:
        weight = round(float(input("Введите вес: ")), 1)
        if 40 < weight < 200:
            employee["weight"] = weight
        else:
            raise ValueError
    except ValueError:
        print("\nНекорректный ввод веса")
        return None
    car = input("Есть ли машина у сотрудника: ").capitalize()
    if car == "True" or car == "False":
        employee["car"] = car
    else:
        print("\nНекорректный ввод булевого значения")
        return None
    employee["languages"] = []
    print("Ввод языков программирования")
    print("Для окончания ввода нажмите enter, оставив поле ввода пустым")
    while True:
        language = input(f'Введите язык программирования: ')
        if language == "":
            break
        else:
            employee["languages"].append(language)
    return employee

def add_employee_to_json_file(json_data, json_file_path):
    employee = get_employee_info()
    if employee is not None:
        json_data = read_json_file(json_file_path)
        json_data.append(employee)
        with open(json_file_path, "w") as json_file:
            json.dump(json_data, json_file, indent=4)
    return json_data

def add_employee_to_csv_file(csv_data, csv_file_path):
    employee = get_employee_info()
    if employee is not None:
        with open(csv_file_path, "r") as csv_file:
            reader = csv.reader(csv_file, delimiter=",")
            csv_data = [row for row in reader]
        csv_element = [value for value in employee.values()]
        csv_data.append(csv_element)
        with open(csv_file_path, "w") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(csv_data)
    return csv_data

def get_employee_info_by_name(json_file_path):
    name = input("\nВведите имя и фамилию: ")
    if re.match(r"[A-Z][a-z]* [A-Z][a-z]*(-[A-Z][a-z]*)?", name):
        json_data = read_json_file(json_file_path)
        for employee in json_data:
            if employee["name"] == name:
                print(f"Информация о сотруднике {name}:")
                print(f"birthday: {employee['birthday']}")
                print(f"height: {employee['height']}")
                print(f"weight: {employee['weight']}")
                print(f"car: {employee['car']}")
                print(f"languages: {employee['languages']}")
                return
        print("\nТакого сотрудника не существует")
    else:
        print("\nНекорректный ввод имени и фамилии")

def filter_employees_by_prog_lang(json_file_path):
    prog_lang = input("\nВведите язык программирования: ")
    json_data = read_json_file(json_file_path)
    employees = []
    for employee in json_data:
        if prog_lang in employee["languages"]:
            employees.append(employee["name"])
    print("Список сотрудников, программирующих на введеном ЯП-е:")
    for employee in employees:
        print(employee)

def filter_employees_by_birthyear(json_file_path):
    try:
        year = int(input("\nВведите год рождения: "))
        if not (1900 <= year <= date.today().year):
            raise ValueError
    except ValueError:
        print("Некорректный ввод года")
        return
    json_data = read_json_file(json_file_path)
    avg = 0
    count = 0
    for employee in json_data:
        if int(employee["birthday"].split(".")[2]) < year:
            avg += employee["height"]
            count += 1
    print(f"Средний рост сотрудников, чей год рождения меньше указанного: {round(avg / count, 2)}")

while True:
    print("Главное меню.")
    print("Вам доступные следующие дейстия:")
    print("0. Выход из программы")
    print("1. Прочитать данные из json")
    print("2. Преобразовать json в csv")
    print("3. Сохранить данные в csv-файл")
    print("4. Добавить информацию о новом сотруднике в json-файл")
    print("5. Добавить информацию о новом сотруднике в csv-файл")
    print("6. Вывести информацию о сотруднике по имени")
    print("7. Отфильтровать сотрудников по языку программирования")
    print("8. Вывести средний рост сотрудников, отфильтрованных по году")
    choice = -1
    try:
        choice = int(input("Выберите дейстие(0-8): "))
    except ValueError:
        pass
    if choice == -1:
        print("\nНекорректный ввод")
    elif choice == 0:
        print("\nОсуществляется выход из программы")
        break
    elif choice < 1 or choice > 8:
        print("\nВыбрана несуществующая опция")
    elif choice == 1:
        json_data = read_json_file(json_file_path)
    elif choice == 2:
        csv_data = convert_json_to_csv(json_data)
    elif choice == 3:
        write_csv_file(csv_data, csv_file_path)
    elif choice == 4:
        json_data = add_employee_to_json_file(json_data, json_file_path)
    elif choice == 5:
        csv_data = add_employee_to_csv_file(csv_data, csv_file_path)
    elif choice == 6:
        get_employee_info_by_name(json_file_path)
    elif choice == 7:
        filter_employees_by_prog_lang(json_file_path)
    else:
        filter_employees_by_birthyear(json_file_path)
    print()
