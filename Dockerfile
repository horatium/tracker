FROM python:3.7.0

COPY . /tracker

WORKDIR /tracker

RUN pip install -e .

EXPOSE 5000
