from selenium import webdriver

link = "http://suninjuly.github.io/find_xpath_form"
browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element_by_tag_name('input')
input1.send_keys("Ivan")
input2 = browser.find_element_by_name(name="last_name")
input2.send_keys("Petrov")
input3 = browser.find_element_by_class_name("form-control.city")
input3.send_keys("Smolensk")
input4 = browser.find_element_by_id('country')
input4.send_keys("Russia")
button = browser.find_element_by_xpath("//Button[text()='Отправить']")
button.click()

#25.213830348191443



# Задание: поиск элемента по XPath
# На этот раз воспользуемся возможностью искать элементы по XPath. 

# На странице http://suninjuly.github.io/find_xpath_form вы найдете такую же форму регистрации, как в шаге 3, при этом в нее добавилась куча одинаковых кнопок отправки. Но сработает только кнопка с текстом "Отправить", и наша задача нажать в коде именно на неё. 

# Ваши шаги: 

# В коде из шага 3 замените ссылку на  http://suninjuly.github.io/find_xpath_form.
# Подберите уникальный XPath-селектор так, чтобы он находил только кнопку с русским текстом. XPath можете формулировать как угодно (по тексту, по структуре, по атрибутам) - главное, чтобы он работал.
# Модифицируйте код из шага 3 таким образом, чтобы поиск кнопки происходил с помощью XPath.
# Запустите ваш код.
# Если вы подобрали правильный селектор и все прошло хорошо, то вы получите код, который нужно отправить в качестве ответа на это задание.

