from selenium import webdriver


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/cats.html")

button = browser.find_element_by_id("button")

# selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"css selector","selector":"[id="button"]"}
#

# Задание: Про Exceptions
# Теперь мы знаем, как настроить ожидание поиска элемента. Во время поиска WebDriver каждые 0.5 секунды проверяет, появился ли нужный элемент в DOM-модели браузера (Document Object Model — «объектная модель документа», интерфейс для доступа к HTML-содержимому сайта). Если произойдет ошибка, то WebDriver выбросит одно из следующих исключений (exceptions):

# Если элемент не был найден за отведенное время, то мы получим NoSuchElementException.
# Если элемент был найден в момент поиска, но при последующем обращении к элементу DOM изменился, то получим StaleElementReferenceException. Например, мы нашли элемент Кнопка и через какое-то время решили выполнить с ним уже известный нам метод click. Если кнопка за это время была скрыта скриптом, то метод применять уже бесполезно — элемент "устарел" (stale) и мы увидим исключение.
# Если элемент был найден в момент поиска, но сам элемент невидим (например, имеет нулевые размеры), и реальный пользователь не смог бы с ним взаимодействовать, то получим ElementNotVisibleException.
# Знание причин появления исключений помогает отлаживать тесты и понимать, где находится баг в случае его возникновения.

# Задание:

# Какую ошибку вы увидите в консоли, если попытаетесь выполнить команду browser.find_element_by_id("button") после открытия страницы http://suninjuly.github.io/cats.html?