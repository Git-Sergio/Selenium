from selenium import webdriver
import math


# Открыть страницу http://SunInJuly.github.io/execute_script.html.
link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

# Посчитать математическую функцию от x. 
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

#Считать значение для переменной x.
x_element = browser.find_element_by_css_selector("#input_value")
x = x_element.text
y = calc(x)
#Проскроллить страницу вниз.
button = browser.find_element_by_tag_name("button")
browser.execute_script("window.scrollBy(0, 120);")
# Ввести ответ в текстовое поле.
input1 = browser.find_element_by_css_selector('#answer')
input1.send_keys(y)
#Выбрать checkbox "Подтверждаю, что являюсь роботом"
Checkbox = browser.find_element_by_css_selector('#robotCheckbox')
Checkbox.click()
#Переключить radiobutton "Роботы рулят!".
Radiobutton = browser.find_element_by_css_selector('#robotsRule')
Radiobutton.click()

# Нажать на кнопку "Отправить".
button = browser.find_element_by_css_selector("button.btn")
button.click()

# 28.869760420567818









# Задание на execute_script
# В данной задаче вам нужно будет снова преодолеть капчу для роботов и справиться с ужасным и огромным футером, который дизайнер всё никак не успевает переделать. Вам потребуется написать код, чтобы:

# Открыть страницу http://SunInJuly.github.io/execute_script.html.
# Считать значение для переменной x.
# Посчитать математическую функцию от x.
# Проскроллить страницу вниз.
# Ввести ответ в текстовое поле.
# Выбрать checkbox "Подтверждаю, что являюсь роботом".
# Переключить radiobutton "Роботы рулят!".
# Нажать на кнопку "Отправить".
# Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени), вы увидите окно с числом. Отправьте полученное число в качестве ответа для этого задания.

# Для этой задачи вам понадобится использовать метод execute_script, чтобы сделать прокрутку в область видимости элементов, перекрытых футером.