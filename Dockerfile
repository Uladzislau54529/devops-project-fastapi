# ===== Stage 1: build dependencies =====
FROM python:3.11-slim AS builder

WORKDIR /main

COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# ===== Stage 2: runtime =====
FROM python:3.11-slim

WORKDIR /main

# copy installed dependencies
COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH

# copy application code
COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:main", "--host", "0.0.0.0", "--port", "8000"]
