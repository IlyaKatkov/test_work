Онлайн платформа торговой сети электроники

Это веб-приложение представляет собой онлайн-платформу для торговой сети электроники. Приложение позволяет управлять иерархической структурой сети по продаже электроники, включая заводы, розничные сети и индивидуальных предпринимателей. Вы можете создавать, редактировать и удалять объекты сети, а также управлять продуктами, контактами и задолженностью перед поставщиком.

Возможности проекта
CRUD пользователей.
CRUD продуктов.
CRUD торговых сетей.
CRUD поставщиков.
Отслеживание задолженности перед поставщиком.
Админ-панель с возможностью добавления ссылки на "Поставщика", фильтрации по названию города и "admin action" для очистки задолженности перед поставщиком.

Запуск проекта
Склонируйте репозиторий
Установите и активируйте виртуальное окружение.
Установите зависимости:
установка pip -r requirements.txt
Создайте файл .env в корневой директории и заполните необходимые переменные окружения по шаблону .env.sample.

Примените миграции:
python manage.py перенести
Запустите сервер:
python manage.py runserver
Используйте команду для создания суперпользователя для доступа в административную панель:
управление на python.py createsuperuser

Права доступа
Доступ к API имеют только активные сотрудники.
