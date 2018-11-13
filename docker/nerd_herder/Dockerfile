FROM python:3-stretch

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/nerd_herder

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY config ./config
COPY manage.py .
COPY nerd_herder ./nerd_herder
COPY wait-for-it.sh .
EXPOSE 8080
ENV DJANGO_SETTINGS_MODULE config.settings.docker

CMD [ "./wait-for-it.sh", "postgres:5432", "--", "gunicorn", "config.wsgi", "-b", "0.0.0.0:8080" ]
