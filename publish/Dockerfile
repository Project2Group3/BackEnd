From python:3

ENV PYTHONUNBUFFERED 1

Run mkdir /new_app

WORKDIR /new_app

ADD . /new_app/

#Install packages from requirements
RUN pip install -r requirements.txt

CMD python manage.py runserver 0.0.0.0:$PORT