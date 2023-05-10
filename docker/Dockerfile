FROM python:3.11

ENV PYTHONUNBUFFERED 1
ENV PUTHONDONTWRITEBYTECODE 1

WORKDIR /django

COPY ./req.txt /django/req.txt
RUN pip install --upgrade pip && pip install -r /django/req.txt


EXPOSE 8000