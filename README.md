Создание файлов с определенным размером и последующим архивированием.

### Опишите подробно какие действия необходимо выполнить, если в ОС Windows требуется получить(создать/сгенерировать) архивный файл, содержащий 800 файлов размером 120Кб каждый. Содержимое и имя файлов не важно.

## Первый вариант выполнения тестового задания с использованием Python
1. Установить Python - https://www.phon.org/, при установке обязательно ставим галочку "Add Python to PATH"
   Установить Git - https://git-scm.com/downloads, для работы с git репозиториями
2. Клонировать репозиторий "test_work".
        Для этого открываем командную строку (Win+R -> cmd -> ENTER), перейти в директорию куда хотим установить папку cd C:/Users/{PC_name}/Desktop), далее скачиваем папку git clone https://github.com/bot209/test_work.git
*{PC_name} - вводим название вашего пользователя

Либо качаем архив (<>Code -> Download ZIP)

3. Перейти в директорию с файлом main.py (cd test_work)

4. Запустить файл main.py (Для этого запускаем в командной строке: python main.py)

5. Вводим желаемое кол-во файлов и размер файла

6. Проверяем наличие папки на созданные файлы и их размер

7. Проверяем .zip файл


## Второй вариант выполнения тестового задания с использованием PowerShell
1. Открыть Пуск, в поиске найти PowerShell и запустить от имени администратора

2. Файлы будут сохраняться в папку test_archive_file. Для этого переходим в директорию диска С:/ ( cd / )

3. Создаем на диске C:/ папку test_archive_file, где будут храниться наши файлы
        
       New-Item -Path "C:\" -Name "test_archive_file" -ItemType "directory"
       Set-Location -Path C:\test_archive_file
        
4. Создаем файлы указав количество их количество -le 800, также указываем размер наших файлов в Kb (120Kb)
 
       $file = "file.txt"
       for ($i=1; $i -le 800; $i++) {
       $array = New-Object -TypeName Byte[] -ArgumentList 120kb
       $object = New-Object -TypeName System.Random
       $object.NextBytes($array)
       Set-Content -Path "$i-$file" -Value $array -Encoding Byte
       }
5. Архивируем нашу папку с помощью командлеты Compress-Archive

       Compress-Archive -LiteralPath 'C:\test_archive_file' -DestinationPath 'C:\test_archive_file.zip'
6. Проверяем наличие архивного файла
