# ==== Stage 1: Build ====
FROM python:3.10-slim AS builder

WORKDIR /main

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ==== Stage 2: Run ====
FROM python:3.10-slim

WORKDIR /main

COPY --from=builder /usr/local /usr/local
COPY . .

EXPOSE 8000

CMD ["python", "-m", "uvicorn", "main:main", "--host", "0.0.0.0", "--port", "8000"]