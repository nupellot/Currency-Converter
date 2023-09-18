# Используем базовый образ Python
FROM python:3.8

# Устанавливаем переменные среды
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы приложения и зависимости
COPY app.py requirements.txt /app/
COPY templates /app/templates
COPY static /app/static

# Устанавливаем зависимости
RUN pip install -r requirements.txt

# Открываем порт 5000
EXPOSE 5000

# Команда для запуска приложения
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]