# Stage 1: install dependencies
FROM python:3.12-slim AS builder
WORKDIR /install
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# Stage 2: final runtime image
FROM python:3.12-slim
WORKDIR /app
COPY --from=builder /install /usr/local
COPY app/ ./app/
RUN useradd -m appuser
USER appuser
EXPOSE 5000
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app.main:app"]