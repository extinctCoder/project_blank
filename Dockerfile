FROM python:3.10

LABEL maintainer="write2shourov@gmail.com"\
    vendor="extinctCoder"

WORKDIR /app

RUN python3 -m pip install --upgrade --force-reinstall pip && \
    python3 -m pip install pipenv

COPY Pipfile .
COPY Pipfile.lock .
RUN pipenv install --system --deploy

COPY startup.sh .
RUN chmod +x ./startup.sh

ENTRYPOINT ["./startup.sh"]