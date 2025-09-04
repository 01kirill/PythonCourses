"""
Есть папка, в которой лежат файлы с разными расширениями.
Программа должна:
● Вывести имя вашей ОС
● Вывести путь до папки, в которой вы находитесь
● Рассортировать файлы по расширениям, например, для
текстовых файлов создается папка, в неё перемещаются
все файлы с расширением .txt, то же самое для остальных
расширений
● После рассортировки выводится сообщение типа «в папке
с текстовыми файлами перемещено 5 файлов, их
суммарный размер - 50 гигабайт»
Продолжение ->
Задания
● Как минимум один файл в любой из получившихся
поддиректорий переименовать. Сделать вывод
сообщения типа «Файл data.txt был переименован в
some_data.txt»
● Программа должна быть кроссплатформенной – никаких
хардкодов с именем диска и слэшами.
"""

import os
from random import randint

def get_os_name():
    name = os.name
    if name == "posix":
        return "Unix/Linux/MacOS"
    elif name == "nt":
        return "Windows"
    return "Jython"

def sort_files_by_extension(path):
    files_list = []
    for root, _, files in os.walk(path):
        for file in files:
            files_list.append(
                [os.path.join(file),
                 os.path.join(file).split(".")[1]]
            )
    files_list.sort(key=lambda x: (x[1], x[0]))
    return files_list

def get_extension_set(files):
    extension_set = set()
    for file in files:
        extension_set.add(file[1])
    return extension_set

def create_folders(extension_set):
    for extension in extension_set:
        if not os.path.exists(
            os.path.join(
                path_to_sorted_files,
                extension
            )
        ):
            os.mkdir(
                os.path.join(
                    path_to_sorted_files,
                    extension
                )
            )

path_to_files = "files"
path_to_sorted_files = "sorted_files"

print(f"Имя операционной системы: {get_os_name()}")
print(f"Путь к папке, в которой мы находимся: {os.getcwd()}")
files = sort_files_by_extension(path_to_files)
extension_set = get_extension_set(files)
create_folders(extension_set)
extension_dict = {key : [0, 0] for key in extension_set}
count = 0
size_sum = 0
for file in files:
    extension_dict[file[1]][0] += 1
    extension_dict[file[1]][1] += os.stat(
        os.path.join(
            path_to_files,
            file[0]
        )
    ).st_size
    os.replace(
        os.path.join(
            path_to_files,
            file[0]
        ),
        os.path.join(
            path_to_sorted_files,
            file[1],
            file[0]
        )
    )
if len(files) > 0:
    for key, value in extension_dict.items():
        print(f"В папку {key} было перемещено {value[0]} файлов,"
            f" их суммарный размер - {value[1]} байт")
    index = randint(0, len(files) - 1)
    print(f"Файл {files[index][0]} был переименован в файл renamed_{files[index][0]}")
    os.rename(
        os.path.join(
            path_to_sorted_files,
            files[index][1],
            files[index][0],
        ),
        os.path.join(
            path_to_sorted_files,
            files[index][1],
            "renamed_" + files[index][0]
        )
    )
else:
    print("Файл(ы) не был(и) перемещен(ы)")
    print("Никакой файл не был переименован")
