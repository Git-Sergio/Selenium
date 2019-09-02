Добавление изменений на сервер (push)
Сейчас у вашего репозитория есть две разные копии — одна локальная, которая уже содержит изменения в файле, и удаленная — на гитхабе. Необходимо наши локальные коммиты положить в удаленный репозиторий. Для этого есть специальная команда git push <репозиторий><название ветки>.

Сейчас мы не будем вдаваться подробно в тему ветвления. Достаточно знать, что основная ветка, на которой вы находитесь по умолчанию — это master. Мы будем пушить в удаленный репозиторий origin — оригинальный репозиторий, откуда мы скопировали к себе на компьютер локальную версию.

Выполним команду:

git push origin master

Git попросит ввести ваш логин и пароль на GitHub, и покажет примерно следующее:
https://ucarecdn.com/b86c59b4-8b4d-40f4-b2a2-584352f61dfa/


Это сообщение о том, сколько данных откуда и куда отправились.

Теперь откройте свой репозиторий на гитхабе в браузере. Если вы все сделали правильно, то гитхаб подтянет описание проекта из файла и красиво отобразит на страничке:
https://ucarecdn.com/40059174-0133-4f0f-8326-e3ed403ca362/


Обратите внимание, что рядом с файлом появилась дополнительная информация: когда файл был последний раз модифицирован и какое было сообщение у этого коммита.

Можно, например, кликнуть на сообщение коммита и посмотреть, какие были изменения:

https://ucarecdn.com/23e1c1fc-139f-4de8-a2dd-389dde978aa4/

Зеленые строки — это те, которые добавились, а красные - те, которые были удалены.

Вот и все, вы молодец!


Разобрался. Не пушилось, тк не сработало добавление коммита, из-за отсутствия данный о email  и имени. Задал почту, имя:

 git config --global user.email "you@example.com"
 git config --global user.name "Your Name"

После чего коммит сохранился и запушился.

так если вы запушить хотите, надо git push origin master, а у вас коммит :) 

добавлять нужно каждый раз - так мы сообщаем какие именно измнения (в каких именнно файлах) мы хотим зафиксировать. Я рекомендую делать это руками на первых порах, потом когда освоитесь и поймете что нужно добавлять и как игнорировать файлы, можно использовать git commit -a : этот флаг автоматически добавляет все изменения в коммит. 