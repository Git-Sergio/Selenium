from selenium import webdriver
# from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import math
import time
# import os


browser = webdriver.Chrome()
# browser.implicitly_wait(12)

# Открыть страницу http://suninjuly.github.io/explicit_wait2.html.
browser.get('http://suninjuly.github.io/explicit_wait2.html')

# ждать и найти подходящую суму для бронирования дома
button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '10000')
    )
# Нажать на кнопку "Забронировать"
button = browser.find_element_by_css_selector("#book")
button.click()

#Проскроллить страницу вниз.
# button = browser.find_element_by_tag_name("button")
# browser.execute_script("return arguments[0].scrollIntoView(true);", button)
# button.click()
button = browser.find_element_by_tag_name("button")
browser.execute_script("window.scrollBy(0, 120);")

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
button = browser.find_element_by_css_selector("#solve")
button.click()

# 28.95742197088181


# Задание: ждем нужный текст на странице
# Попробуем теперь написать программу, которая будет бронировать нам дом для отдыха по строго заданной цене. Более высокая цена нас не устраивает, а по более низкой цене объект успеет забронировать кто-то другой.

# В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:

# Открыть страницу http://suninjuly.github.io/explicit_wait2.html
# Дождаться, когда цена дома уменьшится до 10000 RUR (ожидание нужно установить не меньше 12 секунд)
# Нажать на кнопку "Забронировать"
# Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
# Чтобы определить момент, когда стоимость дома уменьшится до 10000 RUR, используйте метод text_to_be_present_in_element из библиотеки expected_conditions.

# Если все сделано правильно и быстро, то вы увидите окно с числом. Отправьте его в качестве ответа на это задание.

# Итоги урока
# В этом уроке мы изучили способы сделать наши тесты менее зависимыми от внешних условий, на которые мы не можем влиять: например, особенности работы JavaScript и непредсказуемая длительность сетевых запросов. Также узнали, почему надо избегать использования time.sleep() в автотестах, стали пользоваться неявными и явными ожиданиями WebDriver (Implicit и Explicit Waits) и научились разбираться в исключениях WebDriver.