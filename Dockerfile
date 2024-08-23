FROM python:3.10

RUN mkdir /code

WORKDIR /code/

RUN pip install --upgrade pip

COPY requirements.txt /code/

RUN pip install -r requirements.txt

COPY . /code/

WORKDIR /code/urlshortener

EXPOSE 8000

CMD ["gunicorn", "urlshortener.urlshortener.wsgi:application", "--bind", "0.0.0.0:8000"]