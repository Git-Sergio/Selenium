# Запуск браузера и первый скрипт
# Для всех:
# В нашем виртуальном окружении запустим интерпретатор python:  

# (selenium_env) alekspog@xenial:~/environments$ python 
# Теперь напишем скрипт, который откроет следующий шаг в данном уроке на Stepik и отправит правильное решение в задаче. Рекомендуем выполнять команды последовательно по одной, чтобы лучше понять, что происходит в каждой строчке. Не пугайтесь, если не понимаете, что делают те или иные команды, - подробнее мы их разберем в следующих уроках.

# import time

# # webdriver это и есть набор команд для управления браузером
# from selenium import webdriver

# # инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
# driver = webdriver.Chrome()

# # команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
# time.sleep(5)

# # Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
# driver.get("https://stepik.org/lesson/25969/step/8")
# time.sleep(5)

# # Метод find_element_by_css_selector позволяет найти нужный элемент на сайте, указав путь к нему. Способы поиска элементов мы обсудим позже
# # Ищем поле для ввода текста
# textarea = driver.find_element_by_css_selector(".textarea")

# # Напишем текст ответа в найденное поле
# textarea.send_keys("get()")
# time.sleep(5)

# # Найдем кнопку, которая отправляет введенное решение
# submit_button = driver.find_element_by_css_selector(".submit-submission")

# # Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
# submit_button.click()
# time.sleep(5)

# # После выполнения всех действий мы не должны забыть закрыть окно браузера
# driver.quit()

 

# Вы можете запустить этот же скрипт из файла. Скачайте файл get_method.py к себе в папку и запустите его. Для этого создадим папку selenium_course и скопируем в нее скачанный файл. Затем запустим файл в нашем виртуальном окружении.

# Пример для Windows

# (Вместо user везде подставляйте имя пользователя в системе) 

# При выполнении следующих команд не забудьте изменить путь к вашей пользовательской папке вместо C:\Users\user и к папке с загруженным файлом.

# Выполните следующие команды в командной строке Windows:

# c:\Users\user> mkdir selenium_course

# C:\Users\user> copy C:\Users\user\Downloads\get_method.py c:\Users\user\selenium_course

# C:\Users\user> environments\selenium_env\Scripts\activate.bat

# (selenium_env) C:\Users\user>python c:\Users\user\selenium_course\get_method.py
# Пример для Ubuntu

# Выполните следующие команды в консоли Ubuntu:

# mkdir ~/selenium_course
# mv ~/Downloads/get_method.py ~/selenium_course
# python ~/selenium_course/get_method.py
