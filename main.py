import os
import shutil
import getpass

# Создаем функцию create_files в которой указываем количество и размер файлов, имя файла, получение имени пк для дальнейшей установки наших файлов и архивирования.
# Используя условие if not проверяем нет ли такой такой папки. После создаем папку test_archive_files в которой будут храниться наши файлы
# В цикле for создаем файлы в нашей папке с +1 к названию в каждой иттерации
def create_files():
    number = int(input('Введите нужное количество файлов: '))
    size = int(input('Введите размер каждого файла в Kb: '))
    size = size * 1024
    file_name = 'file'
    user_name = getpass.getuser()

    if not os.path.exists(f'C:/Users/{user_name}/Desktop/test_archive_file'):
        os.makedirs(f'C:/Users/{user_name}/Desktop/test_archive_file')
    for i in range(number):
        with open(f'C:/Users/{user_name}/Desktop/test_archive_file/{i+1}-{file_name}.txt', '+w') as file:
            file.write("\0" * size)

# Запускаем файл как основную программу, в которой вызываем нашу функцию для создания файлов. 
# Архивируем нашу папку в формате .zip
if __name__ == "__main__":
    create_files()
    shutil.make_archive('test_archive_file', 'zip', 'test_archive_file')
