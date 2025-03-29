FROM python:3.12-slim

# Устанавливаем необходимые утилиты
RUN apt-get update && apt-get install -y wait-for-it && rm -rf /var/lib/apt/lists/*

# Устанавливаем Poetry
RUN pip install poetry

# Устанавливаем рабочую директорию в tg-bot (где pyproject.toml)
WORKDIR /tg-bot

# Копируем pyproject.toml и poetry.lock
COPY tg-bot/pyproject.toml tg-bot/poetry.lock ./

# Устанавливаем зависимости без виртуального окружения
RUN poetry config virtualenvs.create false && poetry install 

# Копируем весь код проекта
COPY tg-bot /tg-bot

# Оставляем рабочую директорию в tg-bot
WORKDIR /tg-bot

# Запускаем бота
CMD ["poetry", "run", "python3", "-m", "app.main"]
