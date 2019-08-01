from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


#epen link
link = "http://scrapstudio.com.ua/"
browser = webdriver.Chrome()
browser.get(link)

# log in to the store
input1 = browser.find_element_by_name(name="email")
input1.send_keys("sergij.grushkovyk@gmail.com")
input2 = browser.find_element_by_name(name="password")
input2.send_keys("1234567890123")
button = browser.find_element_by_class_name("button")
button.click()



# go to the category 'Блокноти'
link = "http://scrapstudio.com.ua/index.php?route=product/category&path=83&limit=100"
browser.get(link)


# we add the goods to the basket
# add_button = browser.find_element_by_css_selector("613 малюнок")
# add_button.click()

add_button = browser.find_element_by_id('prinf4842butid')
add_button.click()
try:
    WebDriverWait(browser, 1).until(EC.alert_is_present(),
                                   'Timed out waiting for PA creation ' +
                                   'confirmation popup to appear.')

    alert = browser.switch_to.alert
    alert.accept()
    print("alert accepted")
except TimeoutException:
    print("no alert")

add_button = browser.find_element_by_id('prinf4841butid')
add_button.click()
try:
    WebDriverWait(browser, 1).until(EC.alert_is_present(),
                                   'Timed out waiting for PA creation ' +
                                   'confirmation popup to appear.')

    alert = browser.switch_to.alert
    alert.accept()
    print("alert accepted")
except TimeoutException:
    print("no alert")

add_button = browser.find_element_by_id('prinf4840butid')
add_button.click()
try:
    WebDriverWait(browser, 1).until(EC.alert_is_present(),
                                   'Timed out waiting for PA creation ' +
                                   'confirmation popup to appear.')

    alert = browser.switch_to.alert
    alert.accept()
    print("alert accepted")
except TimeoutException:
    print("no alert")

add_button = browser.find_element_by_id('prinf4833butid')
add_button.click()
try:
    WebDriverWait(browser, 1).until(EC.alert_is_present(),
                                   'Timed out waiting for PA creation ' +
                                   'confirmation popup to appear.')

    alert = browser.switch_to.alert
    alert.accept()
    print("alert accepted")
except TimeoutException:
    print("no alert")

add_button = browser.find_element_by_id('prinf4832butid')
add_button.click()
try:
    WebDriverWait(browser, 1).until(EC.alert_is_present(),
                                   'Timed out waiting for PA creation ' +
                                   'confirmation popup to appear.')

    alert = browser.switch_to.alert
    alert.accept()
    print("alert accepted")
except TimeoutException:
    print("no alert")

add_button = browser.find_element_by_id('prinf4827butid')
add_button.click()
try:
    WebDriverWait(browser, 1).until(EC.alert_is_present(),
                                   'Timed out waiting for PA creation ' +
                                   'confirmation popup to appear.')

    alert = browser.switch_to.alert
    alert.accept()
    print("alert accepted")
except TimeoutException:
    print("no alert")

add_button = browser.find_element_by_id('prinf4815butid')
add_button.click()
try:
    WebDriverWait(browser, 1).until(EC.alert_is_present(),
                                   'Timed out waiting for PA creation ' +
                                   'confirmation popup to appear.')

    alert = browser.switch_to.alert
    alert.accept()
    print("alert accepted")
except TimeoutException:
    print("no alert")

add_button = browser.find_element_by_id('prinf4810butid')
add_button.click()
try:
    WebDriverWait(browser, 1).until(EC.alert_is_present(),
                                   'Timed out waiting for PA creation ' +
                                   'confirmation popup to appear.')

    alert = browser.switch_to.alert
    alert.accept()
    print("alert accepted")
except TimeoutException:
    print("no alert")


link = 'http://scrapstudio.com.ua/index.php?route=checkout/cart'
browser.get(link)

checkbox = browser.find_element_by_name(name="remove[]")
checkbox.click()


# add_button1 = browser.find_element_by_id('4838')
# add_button1.click()
# time.sleep(5)
# add_button2 = browser.find_element_by_id('4812')
# add_button2.click()
# time.sleep(5)
# add_button3 = browser.find_element_by_id('4810')
# add_button3.click()
# time.sleep(5)


# link = browser.find_element_by_link_text('увійти')
# link.click()

# input1 = browser.find_element_by_tag_name('email')
# input1.send_keys("sergij.grushkovyk@gmail.com")
# input1 = browser.find_element_by_tag_name('password')
# input1.send_keys("1234567890123")
# link = browser.find_element_by_link_text('увійти')
# link.click()

# link = browser.find_element_by_link_text('')
# link.click()
# input3.send_keys("Smolensk")
# input4 = browser.find_element_by_id('4841')
# input4.send_keys("Russia")
# button = browser.find_element_by_css_selector("button.btn")
# button.click()




# Поиск всех необходимых элементов с помощью find_elements_by
# Мы уже упоминали, что метод find_element_by возвращает только первый из всех элементов, которые подходят под условия поиска. Иногда возникает ситуация, когда у нас есть несколько одинаковых по сути объектов на странице, например, иконки товаров в корзине интернет-магазина. В тесте нам нужно проверить, что отображаются все выбранные для покупки товары. Для этого существуют методы find_elements_by, которые в отличие от find_element_by вернут список всех найденных элементов по заданному условию. Проверив длину списка, мы можем удостовериться, что в корзине отобразилось правильное количество товаров. Пример кода (код приведен только для примера, сайта fake-shop.com скорее всего не существует):

# # подготовка для теста
# # открываем страницу первого товара
# # данный сайт не существует, этот код приведен только для примера
# browser.get("https://fake-shop.com/book1.html")

# # добавляем товар в корзину
# add_button = browser.find_element_by_css_selector(".add")
# add_button.click()

# # открываем страницу второго товара
# browser.get("https://fake-shop.com/book2.html")

# # добавляем товар в корзину
# add_button = browser.find_element_by_css_selector(".add")
# add_button.click()

# # тестовый сценарий
# # открываем корзину
# browser.get("https://fake-shop.com/basket.html")

# # ищем все добавленные товары
# goods = browser.find_elements_by_css_selector(".good")

# # проверяем, что количество товаров равно 2
# assert len(goods) == 2
# Набор стратегий здесь такой же, как и в случае с find_element_by:

# find_elements_by_css_selector;
# find_elements_by_xpath;
# find_elements_by_name;
# find_elements_by_tag_name;
# find_elements_by_class_name;
# find_elements_by_link_text;
# find_elements_by_partial_link_text.
# Также для поиска нескольких элементов мы можем использовать универсальный метод find_elements вместе с атрибутами класса By:

# from selenium.webdriver.common.by import By


# driver.find_elements(By.CSS_SELECTOR, "button.submit")
# !Важно. Обратите внимание на важную разницу в результатах, которые возвращают методы find_element и find_elements. Если первый метод не смог найти элемент на странице, то он вызовет ошибку NoSuchElementException, которая прервёт выполнение вашего кода. Второй же метод всегда возвращает валидный результат: если ничего не было найдено, то он вернёт пустой список и ваша программа перейдет к выполнению следующего шага в коде.