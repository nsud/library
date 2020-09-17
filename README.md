# Моя библиотека

Для запуска проекта необходимо: 

1. Клонировать проект командой ```git clone https://github.com/nsud/lib2.git```
2. Создать окружение ```python -m venv django```
3. Активировать окружение ```django\Scripts\activate.bat```
4. Установить пакеты ```pip install -r requirements.txt```
5. Запустить миграцию ```python manage.py makemigrations```
6. Мигрировать ```python manage.py migrate```
7. Загрузить данные ```python manage.py loaddata data.json```
8. Запустить проект командой ```python manage.py runserver```
9. Друзья будут доступны по ссылке http://127.0.0.1:8000/friends/
10. Библиотека с возможностью одолжить http://127.0.0.1:8000/index/
Админская УЗ: admin/admin



