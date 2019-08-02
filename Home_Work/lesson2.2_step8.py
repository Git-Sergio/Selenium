from selenium import webdriver
# import math
import os


# Открыть страницу http://SunInJuly.github.io/execute_script.html.
link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

# Ввести ответ в текстовое поле.
input1 = browser.find_element_by_css_selector('input:nth-child(2)')
input1.send_keys('Bob')
# Ввести ответ в текстовое поле.
input1 = browser.find_element_by_css_selector('input:nth-child(4)')
input1.send_keys('Jonson')
# Ввести ответ в текстовое поле.
input1 = browser.find_element_by_css_selector('input:nth-child(6)')
input1.send_keys('Bob.Jonson@gim.com')


# заполняем элемент путём до загружаемого файла
element = browser.find_element_by_css_selector('#file')
# element.click()

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
element.send_keys(file_path)

# Нажать на кнопку "Отправить".
button = browser.find_element_by_css_selector("button.btn")
button.click()

# current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
# file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
# element.send_keys(file_path).pressEnter().timesleep(3)
# element.should(exist).pressEnter()

# получаем путь к директории текущего исполняемого файла 
# current_dir = os.path.abspath(os.path.dirname(__file__))
# добавляем к этому пути имя файла     
# file_path = os.path.join(current_dir, 'file.txt')           
# element.send_keys(file_path)







# Задание: загрузка файла
# В этом задании в форме регистрации требуется загрузить текстовый файл.

# Напишите скрипт, который будет выполнять следующий сценарий:

# Открыть страницу http://suninjuly.github.io/file_input.html
# Заполнить текстовые поля: имя, фамилия, email
# Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
# Нажать кнопку "Отправить"
# Если все сделано правильно и быстро, вы увидете окно с числом. Отправьте полученное число в качестве ответа для этого задания.