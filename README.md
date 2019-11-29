Личная библиотека

Реализована возможность хранения и отображения названия, аннотации, информации об авторе и издательстве, изображение обложки и количество экземпляров.

Реализована возможность отслеживать информацию об одолженных друзьям книгах.

Установка и запуск.
Перед запуском севера нужно создать и наполнить базу данных. 
В файле data.xml данные для создания демонстрационной базы данных

Получить приложение 
git clone https://github.com/scherbininvladimir/HomeLibrary/tree/d6

Далее из каталога HomeLibrary нужно запустить команды:
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata data
python manage.py runserver


Пользователь админки - 
login: user_1 
passord:!Z#OAWp#0#Tf