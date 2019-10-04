FROM python:3.6
RUN mkdir -p /usr/src/django/src
ADD django/requirements.txt /usr/src/django/
ADD src /usr/src/django/src/
WORKDIR /usr/src/django
RUN pip install -r requirements.txt
WORKDIR /usr/src/django/src
CMD [ "gunicorn", "app.wsgi", "-b", "0.0.0.0:8080" ]