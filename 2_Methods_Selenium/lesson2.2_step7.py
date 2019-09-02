# Загрузка файлов
# ﻿Если нам понадобится загрузить файл на веб-странице, мы можем использовать уже знакомый нам метод send_keys. Только теперь нам нужно в качестве аргумента передать путь к нужному файлу на диске вместо простого текста.

# Чтобы указать путь к файлу, можно использовать стандартный модуль Python для работы с операционной системой - os. В этом случае ваш код не будет зависеть от операционной системы, которую вы используете. Добавление файла будет работать и на Windows, и на Linux.

# Пример кода, который позволяет указать путь к файлу 'file.txt', находящемуся в той же папке, что и скрипт, который вы запускаете:

# import os 

# current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
# file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
# element.send_keys(file_path)
# Попробуйте добавить в файл отдельно команды print(os.path.abspath(__file__)) и print(os.path.abspath(os.path.dirname(__file__))) и посмотрите на разницу. Подробнее о методах модуля os можете почитать самостоятельно в документации: https://docs.python.org/3/library/os.path.html.

# Элемент в форме, который выглядит, как кнопка добавления файла, имеет атрибут type="file". Мы должны сначала найти этот элемент с помощью селектора, а затем применить к нему метод send_keys(file_path).