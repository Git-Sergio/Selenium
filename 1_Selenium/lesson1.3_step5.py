# Атрибуты, которые влияют на отображение элемента
# Сейчас же мы рассмотрим основы основ, которые позволят вам писать код для автотестов.

# Поговорим чуть подробнее про атрибуты элементов. Некоторые атрибуты влияют на отрисовку элемента на странице, а другие не влияют напрямую, но могут использоваться в JavaScript-коде или быть нужными только для локации элемента в тестах. 

# Примеры атрибутов, которые повлияют на отображение и поведение элемента на странице: 

# <h1 style="color: blue;"> Заголовок будет синим, т.к. цвет задан в атрибуте style </h1>
# <p hidden> Атрибут hidden скрывает элемент на странице, элемент не будет показываться </p>
# <button disabled> Кнопка с атрибутом disabled будет заблокирована </button>
# Чуть ниже вы найдете интерактивную консоль, попробуйте добавить вышеуказанные атрибуты элементам и посмотрите, как изменится отображение элементов. Не забудьте отправить решение кнопкой "Отправить" ("Submit"), после того как весь чек-лист станет зеленым.

# P.S. Этот тип задач экспериментальный для степика, так что, если будут обнаружены какие-то странности, пишите, пожалуйста, в комментарии! 

# HTML
# <h1 style="color: blue;"> Заголовок будет синим, т.к. цвет задан в атрибуте style </h1>
# <p hidden> Атрибут hidden скрывает элемент на странице, элемент не будет показываться </p>
# <button disabled> Кнопка с атрибутом disabled будет заблокирована </button>

# CSS
# button {
#   background-color: #6c6; 
#   border: none;
#   color: white;
#   padding: 15px 30px;
#   text-align: center;
#   text-decoration: none;
#   display: inline-block;
#   font-size: 16px;
# }