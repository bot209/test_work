import os
import shutil
import getpass

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

if __name__ == "__main__":
    create_files()
    shutil.make_archive('test_archive_file', 'zip', 'test_archive_file')
