FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt ./

RUN pip3 install -r requirements.txt --no-cache-dir

COPY . .

RUN python manage.py collectstatic --noinput
RUN python manage.py makemigrations --noinput
RUN python manage.py migrate --noinput

ENV PYTHONPATH=/app
# RUN python api_yamdb/create_superuser.py

CMD ["gunicorn", "api_yamdb.wsgi:application", "--bind", "0:8000" ]