from selenium import webdriver
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException
import math
# import time
# import os


# Открыть страницу http://SunInJuly.github.io/execute_script.html.
browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/alert_accept.html')

button = browser.find_element_by_css_selector(".btn")
button.click()

confirm = browser.switch_to.alert
confirm.accept()

# Посчитать математическую функцию от x. 
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

#Считать значение для переменной x.
x_element = browser.find_element_by_css_selector("#input_value")
x = x_element.text
y = calc(x)

# Ввести ответ в текстовое поле.
input1 = browser.find_element_by_css_selector('#answer')
input1.send_keys(y)

# Нажать на кнопку "Отправить".
button = browser.find_element_by_css_selector("button.btn")
button.click()

# 28.913231956884687


# Задание: принимаем alert


# В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:

# Открыть страницу http://suninjuly.github.io/alert_accept.html
# Нажать на кнопку
# Принять confirm
# На новой странице решить капчу для роботов, чтобы получить число с ответом
# Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени), вы увидите окно с числом. Отправьте полученное число в качестве ответа на это задание.


