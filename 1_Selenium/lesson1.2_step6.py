# Установка драйвера для браузера
# В этом курсе мы будем работать с драйвером для Chrome, так как на данный момент это самый популярный браузер, и в первую очередь следует убедиться, что веб-приложение работает для большинства пользователей.

# http://gs.statcounter.com/browser-market-share/desktop/worldwide/#monthly-201801-201808-bar
# http://gs.statcounter.com/browser-market-share/desktop/worldwide/#monthly-201801-201808-bar

# Драйвер для Chrome разрабатывается командой браузера и носит название ChromeDriver. Для установки откройте сайт https://sites.google.com/a/chromium.org/chromedriver/downloads и скачайте ту версию ChromeDriver, которая соответствует версии вашего браузера. Чтобы узнать версию браузера, откройте новое окно в Chrome, в поисковой строке наберите: chrome://version/ и нажмите Enter. В верхней строчке вы увидите информацию про версию браузера.

# Для Linux:

# Давайте установим и настроим ChromeDriver с помощью команд в терминале. Укажем нужную нам версию ChromeDriver для загрузки. Для получения ссылки перейдите в браузере на нужную вам версию драйвера по ссылке на https://sites.google.com/a/chromium.org/chromedriver/downloads. На открывшейся странице нажмите на файле для Linux правой кнопкой и скопируйте путь к файлу. Замените в примере ниже путь к файлу для команды wget вашей ссылкой:

# $ wget https://chromedriver.storage.googleapis.com/75.0.3770.8/chromedriver_linux64.zip
# $ unzip chromedriver_linux64.zip
# Переместите разархивированный файл с СhromeDriver в нужную папку и разрешите запускать chromedriver как исполняемый файл:

# $ sudo mv chromedriver /usr/bin/chromedriver
# $ sudo chown root:root /usr/bin/chromedriver
# $ sudo chmod +x /usr/bin/chromedriver
# Настройки для Linux готовы. Переходите к следующему шагу.

# Для Windows:

# Скачайте с сайта https://sites.google.com/a/chromium.org/chromedriver/downloads драйвер для вашей версии браузера. Разархивируйте скачанный файл.
# Создайте на диске C: папку chromedriver и положите разархивированный ранее файл chromedriver.exe в папку C:\chromedriver.
# Добавьте в системную переменную PATH папку C:\chromedriver. Как это сделать в разных версиях Windows, описано здесь: https://www.computerhope.com/issues/ch000549.htm. 
# Пример: как добавить путь в системную переменную PATH на Windows10

# 1. Откройте настройки системы.

# 2. В настройках откройте вкладку About, затем System info:



# 3. Выберите Advanced system settings:



# 4. Выберите Environment Variables:



# 5. Кликните два раза на строчке Path в System variables:



# 6. Нажмите кнопку New. Введите в новую строку путь к ChromeDriver - C:\chromedriver. Нажмите Enter. У вас должна появится строка с указанным путем:



# 7. Если у вас была открыта командная строка Windows, не забудьте ее закрыть. Затем откройте новую командную строку, чтобы изменения переменной окружения стали доступны. Активируйте снова виртуальное окружение selenium_env, которое мы создали в предыдущих шагах.

# В следующем шаге мы запустим браузер с помощью Selenium WebDriver и выполним простые команды.