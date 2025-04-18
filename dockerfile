FROM python:3.9-slim

WORKDIR /app

COPY . .

ENV PYTHONPATH=/app

RUN pip install pytest pytest-cov

CMD ["pytest", "--cov=.", "--cov-report=term-missing"]
