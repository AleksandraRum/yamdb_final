FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt ./

RUN pip3 install -r requirements.txt --no-cache-dir

COPY . .

# RUN python manage.py collectstatic --noinput
# RUN python manage.py makemigrations --noinput
# RUN python manage.py migrate --noinput
RUN chmod +x /app/entrypoint.sh

ENV PYTHONPATH=/app
# RUN python api_yamdb/create_superuser.py

ENTRYPOINT ["/app/entrypoint.sh"]

# CMD ["gunicorn", "api_yamdb.wsgi:application", "--bind", "0:8000" ]
# CMD ["sh", "-c", "python manage.py collectstatic --noinput && \
#                   python manage.py migrate --noinput && \
#                   gunicorn api_yamdb.wsgi:application --bind 0.0.0.0:8000"]