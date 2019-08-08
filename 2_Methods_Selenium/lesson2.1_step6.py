




# Метод get_attribute
# Мы уже знаем, как найти нужный элемент на странице и как получить видимый пользователю текст. Для более детальных проверок в тесте нам может понадобиться узнать значение атрибута элемента. Атрибуты могут быть стандартными свойствами, которые понимает и использует браузер для отображения и вёрстки элементов или для хранения служебной информации, например, name, width, height, color и многие другие. Также атрибуты могут быть созданы разработчиками проекта для задания собственных стилей или правил.

# Значение атрибута представляет собой строку. Если значение атрибута отсутствует, то это равносильно значению атрибута равному "false". Давайте еще раз взглянем на страницу http://suninjuly.github.io/math.html. На ней есть radiobuttons, для которых выбрано значение по умолчанию. В автотесте нам может понадобиться проверить, что для одного из radiobutton по умолчанию уже выбрано значение. Для этого мы можем проверить значение атрибута checked у этого элемента. Вот HTML-код элемента:

# <input class="check-input" type="radio" name="ruler" id="humanRule" value="human" checked>
# Найдём этот элемент с помощью WebDriver:

# human_radio = browser.find_element_by_id("humanRule")
# Найдём атрибут "checked" с помощью встроенного метода get_attribute и проверим его значение:

# human_checked = human_radio.get_attribute("checked")
# print("value of human radio: ", human_checked)
# assert human_checked is not None, "Human radio is not selected by default"
# Т.к. у данного атрибута значение не указано явно, то метод get_attribute вернёт "true". Возможно, вы заметили, что "true" написано с маленькой буквы, — все методы WebDriver взаимодействуют с браузером с помощью JavaScript, в котором булевы значения пишутся с маленькой буквы, а не с большой, как в Python.

# Мы можем написать проверку другим способом, сравнив строки::

# assert human_checked == "true", "Human radio is not selected by default"
# Если атрибута нет, то метод get_attribute вернёт значение None. Применим метод get_attribute ко второму radiobutton, и убедимся, что атрибут отсутствует.

# robots_radio = browser.find_element_by_id("robotsRule")
# robots_checked = robots_radio.get_attribute("checked")
# assert robots_checked is None
# Так же мы можем проверять наличие атрибута disabled, который определяет, может ли пользователь взаимодействовать с элементом. Например, в предыдущем задании на странице с капчей для роботов JavaScript устанавливает атрибут disabled у кнопки "Отправить", когда истекает время, отведенное на решение задачи.

# <button type="submit" class="btn btn-default" disabled>Отправить</button>
