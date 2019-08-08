
from selenium import webdriver
import math
from selenium.webdriver.support.ui import Select

# Открыть страницу
# link = ' http://suninjuly.github.io/selects2.html'
link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

# Посчитать сумму заданных чисел
x = browser.find_element_by_xpath('//*[@id="num1"]').text
y = browser.find_element_by_xpath('//*[@id="num2"]').text

z = int(x) + int(y)

# Выбрать в выпадающем списке значение равное расчитанной сумме
select = Select(browser.find_element_by_tag_name("select"))
browser.find_element_by_tag_name("select").click()
select.select_by_value(str(z))

# Нажать кнопку "Отправить"
button = browser.find_element_by_css_selector("button.btn")
button.click()

# print(z)
# print(x)
# print(y)


# 28.868395962536116

# # browser.find_element_by_tag_name("select").click()
# browser.find_element_by_css_selector("option:nth-child(2)").click()

# browser.find_element_by_css_selector("[value='1']").click()

# find_element_by_id
# find_element_by_name
# find_element_by_xpath
# find_element_by_link_text
# find_element_by_partial_link_text
# find_element_by_tag_name
# find_element_by_class_name
# find_element_by_css_selector



# Задание: работа с выпадающим списком
# Для этой задачи мы придумали еще один вариант капчи для роботов. Придется немного переобучить нашего робота, чтобы он справился с новым заданием.

# Напишите код, который реализует следующий сценарий:

# Открыть страницу http://suninjuly.github.io/selects1.html
# Посчитать сумму заданных чисел
# Выбрать в выпадающем списке значение равное расчитанной сумме
# Нажать кнопку "Отправить"
# Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени), вы увидите окно с числом. Отправьте полученное число в качестве ответа для этого задания.

 

# Когда ваш код заработает, попробуйте запустить его на странице http://suninjuly.github.io/selects2.html. Ваш код и для нее тоже ﻿должен пройти успешно.

# Подсказка: если вы получаете ошибку в духе "argument of type 'int' is not iterable", перепроверьте тип переменной, которую вы передаете в функцию поиска. Нужно передать строку! 