"""
установить библиотеку SQLAlchemy, она понадобится нам в следующих уроках
найти путь до этой библиотеки
pip show sqlalchemy
"""
import os
import random
from time import perf_counter

sqlalchemy_folder = r'/Users/irinamilekhina/python_practice/teaching/venv/lib/python3.9/' \
                    r'site-packages/sqlalchemy'

py_files = [item for item in os.listdir(sqlalchemy_folder) if
            item.lower().endswith('.py')]

full_py_files = [os.path.join(sqlalchemy_folder, item) for item in os.listdir(sqlalchemy_folder) if
                 item.lower().endswith('.py')]
print(py_files)

curr_folder = os.path.curdir
print(curr_folder, type(curr_folder))
dirs = [item for item in os.listdir(curr_folder) if os.path.isdir(os.path.join(curr_folder, item))]
print(dirs)


# генерим рандомные файлы
folder = 'some_data'
# letters = [chr(code) for code in range(ord('a'), ord('z') + 1)]
# for _ in range(10 ** 3):
#     f_name = ''.join(random.sample(letters, random.randint(5, 10)))
#     f_content = bytes(random.randint(0, 255) for _ in range(random.randrange(10 ** 5)))
#     with open(os.path.join(folder, f'{f_name}.bin'), 'wb') as f:
#         f.write(f_content)


# start = perf_counter()
# size_threshold = 15 * 2 ** 10
# small_files = [item for item in os.listdir(folder) if os.stat(os.path.join(folder, item)).st_size < size_threshold]
# print(len(small_files), perf_counter() - start)
# start = perf_counter()
# small_files_2 = [item.name for item in os.scandir(folder) if item.stat().st_size < size_threshold]
# print(len(small_files_2), perf_counter() - start)
# print(small_files == small_files_2)

# Этот код не получится запустить, необходимо прочитать и озвучить что он делает
# root = r'C:\Python3.8\Lib\site-packages\django'
# folder = r'C:\Python3.8\Lib\site-packages\django\contrib\admin'
# django_admin_dirs = [
# os.path.relpath(item, root)
# for item in os.scandir(folder)
# if item.is_dir() and not item.name.startswith('_')
# ]
# print(django_admin_dirs)

# curr_file = r'C:\Python3.8\Lib\site-packages\django\http\request.py'
# print('exists', os.path.exists(curr_file))
# # exists ok True
# f_dir, f_name = os.path.split(curr_file)
# print(f_dir, f_name, sep=' | ')
# # C:\Python3.8\Lib\site-packages\django\http | request.py
# print('dirname ok', f_dir == os.path.dirname(curr_file))
# # dirname ok True
# print('basename ok', f_name == os.path.basename(curr_file))
# # basename ok True
# print('abspath ok', curr_file == os.path.abspath(curr_file))
# # abspath ok True
# curr_file_rel = os.path.relpath(curr_file, root)
# print(curr_file_rel)
# #http\request.py
# print('relpath ok', curr_file == os.path.join(root, curr_file_rel))
# # relpath ok True

