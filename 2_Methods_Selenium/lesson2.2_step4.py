from selenium import webdriver
browser = webdriver.Chrome()
# browser.execute_script("alert('Robots at work');")

# browser.execute_script("document.title='Script executing';")

browser.execute_script("document.title='Script executing';alert('Robots at work');")

# browser.execute_script("alert(\"Robots at work\");") #экранировать обратным слэшем
# Вдруг будет кому-нибудь интересно. Выполнение JavaScript на странице - это неописанный в документации Selenium способ поиска элемента.
# Вместо встроенных find_element_by... можно использовать вот такую конструкцию:
# element = browser.execute_script('document.getElementsByName("name")')

# Так же есть конструкции:
# getElementById
# getElementsByTagName
# getElementsByClassName
# querySelector - для CSS
# querySelectorAll - для CSS (находит все совпадения)

# evaluate - для XPATH.

# Погуглите.




# Метод execute_script
# Рассмотрим еще один очень полезный и мощный метод, но он требует хотя бы минимальных знаний JavaScript. С помощью метода execute_script можно выполнить программу, написанную на языке JavaScript, как часть сценария автотеста в запущенном браузере. Зачем это может понадобиться, если в автотестах мы стараемся взаимодействовать с интерфейсом сайта как обычный пользователь, нажимая кнопки, выбирая пункты меню и вводя текст в текстовые поля?

# Дело в том, что стандартные методы, доступные в Selenium, не могут покрыть всех возможных ситуаций работы с веб-приложением. Сайты в интернете могут решать самые разные задачи, начиная от простого блога до сложных финансовых или графических приложений. Разработчики имеют доступ к огромному количеству различных библиотек для решения бизнес-сценариев, что приводит к появлению на веб-странице нестандартных редакторов текстов, уникальных меню, оригинальных видео-плееров и т.д. Порой это приводит к тому, что для нажатия вроде бы обычной кнопки тестировщику понадобится писать настоящий JavaScript-сценарий. Если вы столкнулись с такой ситуацией, то в первую очередь обратитесь за помощью к вашим фронтенд-разработчикам, чтобы они подсказали  пример нужного скрипта. Прежде чем использовать данный скрипт в тестах, вы можете проверить, как он работает прямо в браузере, выполнив код в консоли браузера. Затем можете добавить его в ваш автотест с помощью execute_script(javascript_code).

# Давайте попробуем вызвать alert в браузере с помощью WebDriver. Пример сценария:

# from selenium import webdriver
# browser = webdriver.Chrome()
# browser.execute_script("alert('Robots at work');")
# Обратите внимание, что исполняемый JavaScript нужно заключать в кавычки (двойные или одинарные). Если внутри скрипта вам также понадобится использовать кавычки, а для выделения скрипта вы уже используете двойные кавычки, то в скрипте следует поставить одинарные:

# browser.execute_script("document.title='Script executing';")
# Такой формат записи тоже будет работать:

# browser.execute_script('document.title="Script executing";')
# Можно с помощью этого метода выполнить сразу несколько инструкций, перечислив их через точку с запятой. Изменим сначала заголовок страницы, а затем вызовем alert:

# browser.execute_script("document.title='Script executing';alert('Robots at work');")