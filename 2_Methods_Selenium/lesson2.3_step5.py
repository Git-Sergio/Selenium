# Переход на новую вкладку браузера
# При работе с веб-приложениями приходится переходить по ссылкам, которые открываются в новой вкладке браузера. WebDriver может работать только с одной вкладкой браузера. При открытии новой вкладки WebDriver продолжит работать со старой вкладкой. Для переключения на новую вкладку надо явно указать, на какую вкладку мы хотим перейти. Это делается с помощью команды switch_to.window:

# browser.switch_to.window(window_name)
# Чтобы узнать имя новой вкладки, нужно использовать метод window_handles, который возвращает массив имён всех вкладок. Зная, что в браузере теперь открыто две вкладки, выбираем вторую вкладку:

# new_window = browser.window_handles[1]
# Также мы можем запомнить имя текущей вкладки, чтобы иметь возможность потом к ней вернуться:

# first_window = browser.window_handles[0]
# После переключения на новую вкладку поиск и взаимодействие с элементами будут происходить уже на новой странице.


# Текущую вкладку можно узнать так:

# current_window = browser.current_window_handle

# > Зная, что в браузере теперь открыто две вкладки, выбираем вторую вкладку:

# new_window = browser.window_handles[1]

# window_handles возвращает lis

# windows = browser.window_handles
# current_window = browser.current_window_handle

# for win in windows:
#     if current_window == win:
#         print(win, " with current index: ", windows.index(win))
#     else:
#         print(win, " with index: ", windows.index(win))

# Если хотите узнать текущую вкладку, попробуйте сделать так. Ниже пример работы (текущая вкладка в данном случае первая, т.к. не было команды перейти на новые)
# https://ucarecdn.com/6f924ca1-3df4-4d4e-852f-d345b96b8bff/-/crop/719x166/0,0/-/preview/