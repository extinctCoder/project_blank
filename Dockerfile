FROM python:3.10

LABEL author=extinctCoder
LABEL email="write2shourov@gmail.com"

WORKDIR /app

COPY requirements.txt .
COPY src .
RUN pwd
RUN ls