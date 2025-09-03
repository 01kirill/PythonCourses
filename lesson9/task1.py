import os

print(os.getcwd())
if not os.path.exists('test_folder'):
    os.mkdir('test_folder')
if not os.path.exists('test_folder/inner'):
    os.mkdir('test_folder/inner')
open('test_folder/data.txt', "w", encoding="utf-8").write("")
os.rename('test_folder/data.txt', 'test_folder/info.txt')
print(list(os.walk('test_folder')))
print(os.stat('test_folder/info.txt').st_size, "|", os.stat('test_folder/info.txt').st_mtime)
os.replace('test_folder/info.txt', 'test_folder/inner/info.txt')
os.remove('test_folder/inner/info.txt')
os.removedirs("test_folder/inner")
