FROM python:3.14-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN addgroup --system tusya && adduser --system --ingroup tusya tusya

COPY pyproject.toml /app/pyproject.toml
COPY src /app/src
COPY scripts /app/scripts
COPY .env.example /app/.env.example

RUN pip install --no-cache-dir .

RUN mkdir -p /app/data /app/logs /app/backups && chown -R tusya:tusya /app

USER tusya

VOLUME ["/app/data", "/app/logs", "/app/backups"]

HEALTHCHECK --interval=30s --timeout=5s --retries=3 CMD python -m tusya_bot healthcheck --database-path /app/data/tusya.sqlite3

CMD ["python", "-m", "tusya_bot", "run"]
