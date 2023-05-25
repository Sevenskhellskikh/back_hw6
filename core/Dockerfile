# Базовый образ, на основе которого будет создан локальный образ
FROM python:3.10.2-slim

# Копируем requirements.txt в контейнер в указанную директорию
COPY requirements.txt /tmp

# Запускаем requirements.txt из созданной директории
RUN pip install -r /tmp/requirements.txt

# Копируем содержимое проекта в указанную директорию
COPY . /opt/app

# Задаём директорию, из которой будут выполняться последующие команды (CMD, RUN, COPY)
WORKDIR /opt/app

# Запускаем наш сервер при старте контейнера
CMD ['python', 'manage.py', 'runserver', '0:8000']