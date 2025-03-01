### DRF программа генерирует кассовый чек в формате PDF а так же QR код со ссылкой на него
1. установите зависимости (poetry install)
2. создайте базу данных
3. переименуйте .env.sample в .env и заполните данные
4. примените миграции к БД (python manage.py migrate)
5. загрузите тестовые фикстуры товаров
python manage.py loaddata items_fixture.json
6. запустите сервер (python manage.py runserver ваш_IP:ПОРТ)
7. проверьте запрос
***
- POST запрос на создание чека из 3х товаров

![post.png](png/post.png)
***
- чек PDF а так же QR код сохраняются в папке media

![img.png](png/img.png)
