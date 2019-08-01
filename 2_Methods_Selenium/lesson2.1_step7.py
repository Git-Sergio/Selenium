from selenium import webdriver
import time
import math



link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

# Ваш код, который заполняет обязательные поля

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


x = browser.find_element_by_xpath('//*[@id="treasure"]').get_attribute('valuex')
print(x)
y = calc(x)

input1 = browser.find_element_by_css_selector('#answer')
input1.send_keys(y)

Checkbox = browser.find_element_by_css_selector('#robotCheckbox')
Checkbox.click()
Radiobutton = browser.find_element_by_css_selector('#robotsRule')
Radiobutton.click()


# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")
button.click()

# 28.82383845999407

# Проверяем, что смогли зарегистрироваться
# ждем загрузки страницы
# time.sleep(1)

# находим элемент, содержащий текст
# welcome_text_elt = browser.find_element_by_tag_name("h1")

# записываем в переменную welcome_text текст из элемента welcome_text_elt
# welcome_text = welcome_text_elt.text

# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
# assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text

# 28.82288296286888




# Задание: кликаем по checkboxes и radiobuttons (капча для роботов)
# Продолжим использовать силу роботов 🤖 для решения повседневных задач. На данной странице мы добавили капчу для роботов, то есть тест, являющийся простым для компьютера, но сложным для человека.
# http://suninjuly.github.io/math.html
# Ваша программа должна выполнить следующие шаги:

# Открыть страницу http://suninjuly.github.io/math.html.
# Считать значение для переменной x.
# Посчитать математическую функцию от x (код для этого приведён ниже).
# Ввести ответ в текстовое поле.
# Отметить checkbox "Подтверждаю, что являюсь роботом".
# Выбрать radiobutton "Роботы рулят!".
# Нажать на кнопку Отправить.
# Для этой задачи вам понадобится использовать атрибут .text для найденного элемента. Обратите внимание, что скобки здесь не нужны:

# x_element = browser.find_element_by_*(selector)
# x = x_element.text
# y = calc(x)
# Атрибут text возвращает текст, который находится между открывающим и закрывающим тегами элемента. Например, text для данного элемента <div class="message">У вас новое сообщение.</div> вернёт строку: "У вас новое сообщение".

# Используйте функцию calc(), которая рассчитает и вернет вам значение функции, которое нужно ввести в текстовое поле. Не забудьте добавить этот код в начало вашего скрипта:

# import math

# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))
# Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени), вы увидите окно с числом. Скопируйте его в поле ниже. 