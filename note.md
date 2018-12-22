# PIP

    pip install --upgrade pip
    pip install --upgrade setuptools
    pip install virtualenv
    virtualenv env
      
    env\Scripts\activate.bat
    pip install django
    
## Зависимости

Сохранить

    pip freeze > requirements.txt   
 
Установить 
зне   
    pip install -r requirements.txt

# Создать приложение

    django-admin startproject app
    python manage.py runserver
    
    python manage.py createsuperuser
    python manage.py startapp firstapp

# Миграции

Команда __makemigrations__ создаёт (но не применяет) миграции для всех приложений, которые установлены в ваш проект (вы так же можете указать в конце имя конкретного приложения, чтобы создать миграции только для него). Это даёт вам возможность проверить код перед тем, как их применить — когда вы станете хорошо разбираться в Django, то сможете даже менять их!

Команда __migrate__ применяет созданные миграции к базе (Django отслеживает, какие миграции были созданы для данной базы).

    python manage.py showmigrations

По manage.py show migrations можно глянуть примененные и непримененные миграции. 
Указав номер, можно откатиться на предыдущую миграцию

    manage.py migrate <модель> <номер миграции>
    
или

    python3 manage.py migrate --fake APPNAME zero