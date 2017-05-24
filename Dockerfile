FROM python:3.5
ADD . /app
WORKDIR /app

RUN apt-get update
RUN apt-get --assume-yes install apt-utils
RUN apt-get --assume-yes upgrade
RUN apt-get --assume-yes install libpq-dev libsnappy-dev
RUN pip install --no-cache -r requirements.txt
