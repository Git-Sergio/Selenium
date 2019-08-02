from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

opt = webdriver.ChromeOptions()
opt.add_experimental_option('w3c', False)
browser = webdriver.Chrome(chrome_options=opt)
browser.get("http://suninjuly.github.io/wait2.html")


# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "check"))
    )
button.click()
message = browser.find_element_by_id("check_message")

assert "успешно" in message.text

# Как вы видите, в этом случае нужно использовать поиск элементов с помощью класса By, который мы рассмотрели ранее. element_to_be_clickable вернет элемент, когда он станет кликабельным, или вернет False в ином случае.

# Обратите внимание, что в объекте WebDriverWait используется функция until, в которую передается правило ожидания, элемент, а так же значение, по которому мы будем искать элемент. В модуле expected_conditions есть много других правил, которые позволяют реализовать необходимые ожидания:

# title_is
# title_contains
# presence_of_element_located
# visibility_of_element_located
# visibility_of
# presence_of_all_elements_located
# text_to_be_present_in_element
# text_to_be_present_in_element_value
# frame_to_be_available_and_switch_to_it
# invisibility_of_element_located
# element_to_be_clickable
# staleness_of
# element_to_be_selected
# element_located_to_be_selected
# element_selection_state_to_be
# element_located_selection_state_to_be
# alert_is_present
# Описание каждого правила можно найти на сайте.

# Если мы захотим проверять, что кнопка становится неактивной после отправки данных, то можно задать негативное правило с помощью метода until_not:

# # говорим Selenium проверять в течение 5 секунд пока кнопка станет неактивной
# button = WebDriverWait(browser, 5).until_not(
#         EC.element_to_be_clickable((By.ID, "check"))
#     )

# https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.expected_conditions


# Explicit Waits (WebDriverWait и expected_conditions)
# В предыдущем шаге мы решили проблему с ожиданием элементов на странице. Однако методы find_element проверяют только то, что элемент появился на странице. В то же время элемент может иметь дополнительные свойства, которые могут быть важны для наших тестов. Рассмотрим пример с кнопкой, которая отправляет данные:

# Кнопка может быть неактивной, то её нельзя кликнуть;
# Кнопка может содержать текст, который меняется в зависимости от действий пользователя. Например, текст "Отправить" после нажатия кнопки поменяется на "Отправлено";
# Кнопка может быть перекрыта каким-то другим элементом или быть невидимой.
# Если мы хотим в тесте кликнуть на кнопку, а она в этот момент неактивна, то WebDriver все равно проэмулирует действие нажатия на кнопку, но данные не будут отправлены.

# Давайте попробуем запустить следующий тест:

# from selenium import webdriver

# browser = webdriver.Chrome()
# # говорим WebDriver ждать все элементы в течение 5 секунд
# browser.implicitly_wait(5)

# browser.get("http://suninjuly.github.io/wait2.html")

# button = browser.find_element_by_id("check")
# button.click()
# message = browser.find_element_by_id("check_message")

# assert "успешно" in message.text
# Мы видим, что WebDriver смог найти кнопку с id="сheck" и кликнуть по ней, но тест упал на поиске элемента "check_message" с итоговым сообщением:

# no such element: Unable to locate element: {"method":"id","selector":"check_message"}
# Это произошло из-за того, что WebDriver быстро нашел кнопку и кликнул по ней, хотя кнопка была еще неактивной. На странице мы специально задали программно паузу в 1 секунду после загрузки сайта перед активированием кнопки, но неактивная кнопка в момент загрузки — обычное дело для реального сайта.

# Чтобы тест был надежным, нам нужно не только найти кнопку на странице, но и дождаться, когда кнопка станет кликабельной. Для реализации подобных ожиданий в Selenium WebDriver существует понятие явных ожиданий (Explicit Waits), которые позволяют задать специальное ожидание для конкретного элемента. Задание явных ожиданий реализуется с помощью инструментов WebDriverWait и expected_conditions. Улучшим наш тест: