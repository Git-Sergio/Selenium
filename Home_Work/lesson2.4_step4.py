from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/wait1.html")

time.sleep(1)
button = browser.find_element_by_id("check")
button.click()
message = browser.find_element_by_id("check_message")

assert "успешно" in message.text



# Давайте быстрее это починим: time.sleep()
# Теперь, когда мы уже знаем, что кнопка появляется с задержкой, мы можем добавить паузу до начала поиска элемента. Мы уже использовали библиотеку time ранее. Давайте применим ее и сейчас:

# from selenium import webdriver
# import time

# browser = webdriver.Chrome()
# browser.get("http://suninjuly.github.io/wait1.html")

# time.sleep(1)
# button = browser.find_element_by_id("check")
# button.click()
# message = browser.find_element_by_id("check_message")

# assert "успешно" in message.text
# Теперь тест проходит. Но что если элемент с сообщением тоже будет появляться с задержкой? Добавить еще один time.sleep() перед поиском сообщения? А если изменится время задержки при появлении кнопки? Увеличим длительность паузы? А еще на разных машинах с разной скоростью интернета кнопка может появляться через разные промежутки времени. Можно перед каждым действием добавить задержку, но тогда значительную часть времени прогона тестов будут занимать бесполезные ожидания, при этом с увеличением количества тестов эта проблема будет только расти. 