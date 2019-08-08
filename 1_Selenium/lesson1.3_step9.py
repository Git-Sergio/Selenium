# Задание: верстка веб-страницы
# В этой задаче вы опишете несколько элементов самостоятельно, чтобы еще лучше ориентироваться в устройстве HTML-странички. На минутку почувствовать себя фронтенд-разработчиком очень полезно!

# Предлагаем вам сверстать небольшую веб-страничку о своем питомце или о любом другом зверьке, которой вы хотели бы поделиться с миром.

# 1. Прямо под заголовком найдите элемент с тегом img. Это элемент, в котором будет отрисовываться картинка. Добавьте ему атрибут class со значением "picture". А существующему атрибуту src добавьте значение: вставьте в кавычки ссылку на изображение.

# 2. Прямо под элементом-картинкой вы найдете элемент-разделитель с тегом div. В этом блоке у нас будет имя и описание питомца. Добавьте этому элементу атрибут name со значением "about".

# 3. Добавьте этому элементу потомка. Это будет заголовок: добавьте элемент с тегом h3. Не забудьте открывающий и закрывающий тег. Добавьте этому элементу атрибут id со значением pet-name. Внутри тега напишите имя или название животного.

# 4. Добавьте еще одного потомка элементу div, на этот раз это будет текст, поэтому используйте тег p. Добавьте ему атрибут data-type со значением "description". Внутри тега напишите пару слов про своего питомца. Обратите внимание, что атрибут data-type не специализированный, мы его придумали сами.

# Если вы все сделали правильно, то все 5 галочек внизу должны стать зелеными, а в окошке вы увидите готовую веб-страничку. Нажмите кнопку "Отправить", чтобы получить свои заслуженные баллы.

# А еще можно запостить ваши старания на форум решений и заодно похвастаться своими домашними животными. :)

# P. S.: Этот тип задач экспериментальный для степика, поэтому пишите, пожалуйста, в комментариях ваши замечания,  если будут обнаружены какие-то странности.

# HTML
# <!DOCTYPE HTML>
# <html>
#  <body>
#   <h1>Look at my awesome pet:</h1>
#   <img class="picture" src="https://images.chesscomfiles.com/uploads/v1/images_users/tiny_mce/Suntina/phphyw2Kl.jpeg">
#   <div name="about">
# <h3 id="pet-name">
#     <p data-type="description"> <p>
#     <h3>
#   </div>
#  </body>
# </html>

# CSS
# .picture  {
#     width:100%;
#     max-width:200px;
# }
