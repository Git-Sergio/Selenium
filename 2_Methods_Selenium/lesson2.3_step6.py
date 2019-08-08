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
browser.get('http://suninjuly.github.io/redirect_accept.html')

button = browser.find_element_by_css_selector(".btn")
button.click()

window_name = browser.window_handles[1]
browser.switch_to.window(window_name)

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

# # Нажать на кнопку "Отправить".
button = browser.find_element_by_css_selector("button.btn")
button.click()

## window_handles возвращает list
# windows = browser.window_handles
# current_window = browser.current_window_handle

# for win in windows:
#     if current_window == win:
#         print(win, " with current index: ", windows.index(win))
#     else:
#         print(win, " with index: ", windows.index(win))

# Если хотите узнать текущую вкладку, попробуйте сделать так. Ниже пример работы (текущая вкладка в данном случае первая, т.к. не было команды перейти на новые)
# https://ucarecdn.com/6f924ca1-3df4-4d4e-852f-d345b96b8bff/-/crop/719x166/0,0/-/preview/