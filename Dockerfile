FROM python:3.9

RUN mkdir /app
WORKDIR /app

RUN apk update && \
    apk upgrade && \
	apk add --no-cache bash git openssh \
	postgresql-dev gcc python3-dev musl-dev \
	libffi-dev openssl-dev cargo\
	&& rm -rf /var/cache/apk/* \
	&& pip3 install --upgrade pip \
	&& pip3 install --upgrade setuptools\
	&& pip3 install psycopg2 \
	&& pip3 install gunicorn \
	&& pip3 install fastapi \

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

LABEL maintainer="Maximilien Pelletier <maximilien.pelletier@strades.app>"

CMD ./scripts/start.sh 

EXPOSE 8000
