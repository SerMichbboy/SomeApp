---
- 28.01.2025
Изменена конфигурация докера.
Убраны лишние моудли.
Проведён некоторый рефакторинг.
Устранена ошибка, при которой докер билдился с ошибкой.

- 25.12.2025
На текущий момент в проекте реализована сыро стартовая страница, страница регистрации и вход
за пользователя.
Добавлен frontend.
Реализован на Js.
Используются components, styles на нескольких страничках.
Реализованы анимации конпок и иконок.

---

- Django
- Docker
- RAbbitMQ
- PyTest
- PIL
- PyJWT
- Postgress

и др. Для большего списка откройте requirements.txt

---
Для запуска локально нужно в .env раскоментить:

DATABASE_HOST=localhost

для запуска Docker compose:

DATABASE_HOST=db

---

## database

postgres

---

### requirements.txt

Для работы с проектом локально выполните команду:

- cd backend/ pip install requirements.txt

команда установит необходимые зависимости на машину.

---

### Docker

Для запуска образа докер пишем в консоли:

docker compose up --build

---

### Тесты

Для запуска тестов в контейнере нужно провалится в контейнер web и внутри контейнера выполнить команду:

- pytest

Тесты сформированы для основных моделей и их для их вьюшек.
По отдельности можно запустить тесты для каждой модельки.

их реализовано 3:

- users
- authtorize
- images

---

### users

Модель users предусматривает полный CRUD:

- регистрация пользователя
- получение пользователя по id
- получение всех пользоваетелей
- редактирование
- удаление

Модель users - SomeApp/users/CustomUser

урла для обращения:

- api/users/

---

### images

для images также предусмотрет полный CRUD.
Работать с images может только авторизованный.
Методы позволяют:

- создавать файл картинки
- просматривать конкретное изображение(с передачей pk в запросе)
- получить все изображения
- редактировать
- удалить

Так же в работу с изображениями заложен функционал обработки (images/services.py).
При POST к api/images/ и передачей в него form-data, файл будет отформатирован до 
квадратного изображения по его наименьшей стороне, а само изображение сохранится в чб.

урла для обращения:

- api/images/

---

### authtorize

позволяет получать и обновлять авторизационные токены.
Получить и обновить токен может только зарегистрированный пользователь.

эндпоинты для создания/обновления/удаления токена:

- api/token/create/
- api/token/refresh/
- api/token/delete/

---
