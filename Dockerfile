# Build stage
FROM python:3.13-slim as builder

WORKDIR /app

RUN apt-get update && \
    apt-get install -y curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip install poetry

COPY poetry.lock pyproject.toml .

# ИСПРАВЛЕНИЕ: --without dev вместо --no-dev
RUN poetry config virtualenvs.create false && \
    poetry install --no-root --no-interaction --no-ansi --without dev

# Runtime stage
FROM python:3.13-slim as runtime

WORKDIR /app

# Копируем только установленные пакеты из builder stage
COPY --from=builder /usr/local/lib/python3.13/site-packages/ /usr/local/lib/python3.13/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/

# Копируем исходный код
COPY . .

ENV CELERY_BROKER_URL="redis://redis:6379"
ENV CELERY_BACKEND="redis://redis:6379"

RUN mkdir -p /app/media /app/staticfiles

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]