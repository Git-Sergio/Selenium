# Поиск элементов с помощью составных CSS-селекторов
# Теперь предположим, что нам нужно найти элемент на странице, который нельзя найти, используя простой селектор. Ниже мы привели часть кода простой HTML-страницы, описывающей блог. Саму страницу вы можете посмотреть по ссылке.
# http://suninjuly.github.io/blog_example.html
# Вопрос: как нам найти селектор для подписи у второй картинки? Вот здесь нам поможет иерархическая структура страницы и возможность комбинировать CSS-селекторы. CSS-селекторы позволяют использовать одновременно любые селекторы, рассмотренные ранее, а также имеют некоторые дополнительные возможности для уточнения поиска.

# <div id="posts" class="post-list">
#   <div id="post1" class="item">
#     <div class="title">Как я провел лето</div>
#     <img src="./images/summer.png">
#   </div>
#   <div id="post2" class="item">
#     <div class="title second">Ходили купаться</div>
#     <img src="./images/bad_dog.jpg">
#   </div>
#   <div id="post3" class="item">
#     <div class="title">С друзьями</div>
#     <img src="./images/friends.jpg">
#   </div>
# </div>
# Использование потомков

# Попробуем найти элемент с текстом "Ходили купаться". Для решения этой задачи мы можем взять элемент, стоящий выше в иерархии нужного нам элемента,  и написать следующий селектор:

# "#post2 .title"

# Здесь знак "#" означает, что надо искать элемент с id "post2", а "." - что искать надо класс со значением "title".

# Элемент ".title" называется потомком (англ. descendant) элемента "#post2". Потомок может находиться на любом уровне вложенности - все элементы с селектором ".title" также являются и потомками элемента "#posts", хотя и расположены от него на два уровня ниже. "#posts .title" найдет все 3 элемента с классом "title".

# !Обратите внимание на пробел в записи селектора. Это важный символ, который разделяет описание предка и потомка. Если бы мы записали селектор "#post2.title" без пробела, то в данном примере не было найдено ни одного элемента. Такая запись означала бы, что мы хотим найти элемент, который одновременно содержит id "post2" и класс "title".

# Использование дочерних элементов

# Другой способ найти этот элемент:

# "#post2 > div.title"

# Здесь мы указали еще тег элемента div и уточнили, что нужно взять элемент с тегом и классом: "div.title", который находится строго на один уровень иерархии ниже чем элемент "#post2" (это задаёт символ ">").

# Элемент "#post2" в этом случае называется родителем (англ. parent) для элемента "div.title", а элемент "div.title" называется дочерним элементом (англ. child) для элемента "#post2". Если символа ">" нет, то будут выполнен поиск всех элементов "div.title" на любом уровне ниже первого элемента.

# !В данном случае символы пробела вокруг символа ">" не несут важного значения в отличие от предыдущего примера, и могут быть опущены. Запись "#post2>div.title" аналогична записи "#post2 > div.title".

# Использование порядкового номера дочернего элемента

# Еще один способ найти этот элемент:

# "#posts > .item:nth-child(2) > .title"

# Псевдо-класс :nth-child(2) - позволяет найти второй по порядку элемент среди дочерних элементов для "#posts". Затем с помощью "> .title" мы указываем, что нам нужен элемент ".title", родителем которого является найденный ранее элемент ".item".

# Использование нескольких классов

# Также мы можем использовать сразу несколько классов элемента, чтобы его найти. Для этого классы записываются подряд через точку: ".title.second"

# Мы рассмотрели базовые селекторы, которых будет достаточно для написания простых UI-тестов. Если вы захотите разобраться подробнее в css-селекторах, то мы рекомендуем вам посмотреть следующие статьи: 

# https://learn.javascript.ru/css-selectors

# https://www.w3schools.com/cssref/css_selectors.asp

# https://developer.mozilla.org/ru/docs/Web/CSS/CSS_%D0%A1%D0%B5%D0%BB%D0%B5%D0%BA%D1%82%D0%BE%D1%80%D...