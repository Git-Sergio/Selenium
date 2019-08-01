from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration1.html"
browser = webdriver.Chrome()
browser.get(link)

input_1 = browser.find_element_by_css_selector(".first_block .first")
input_1.send_keys("James")
input_2 = browser.find_element_by_css_selector(".first_block .second")
input_2.send_keys("Bond")
input_3 = browser.find_element_by_css_selector(".first_block .third")
input_3.send_keys("jamesbond@gmail.com")


button = browser.find_element_by_css_selector("button.btn")
button.click()
time.sleep(5)

welcome_text_elt = browser.find_element_by_tag_name("h1")
welcome_text = welcome_text_elt.text
assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text