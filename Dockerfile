# Используем официальный образ Python
FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    curl \
    wget \
    unzip \
    gnupg \
    ca-certificates \
    lsb-release \
    libnss3 \
    libgdk-pixbuf2.0-0 \
    libatk-bridge2.0-0 \
    libx11-xcb1 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    libgtk-3-0 \
    libgbm-dev \
    libpq-dev gcc \
    redis-tools \
    libasound2


# Добавляем репозиторий Google Chrome
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list'

# Устанавливаем Google Chrome
RUN apt-get update && apt-get install -y google-chrome-stable

# Устанавливаем ChromeDriver с помощью webdriver-manager
RUN pip install webdriver-manager

# Устанавливаем рабочую директорию
WORKDIR /app/

# Устанавливаем alembic
RUN pip install alembic

RUN pip install flower


# Копируем проект и устанавливаем зависимости
COPY pyproject.toml poetry.lock* /app/
RUN pip install poetry && poetry install --no-root --only main

 
# Копируем код приложения
COPY . /app/

# Указываем команду по умолчанию
CMD ["poetry", "run", "python", "start.py"]

