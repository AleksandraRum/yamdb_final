FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt ./

RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt --no-cache-dir

COPY . .

COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

ENV PYTHONPATH=/app

ENTRYPOINT ["/app/entrypoint.sh"]
