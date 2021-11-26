FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y
RUN apt-get install -y python3-pip

ADD ./SecureWebApp /Test_App
WORKDIR /Test_App

COPY requirements.txt requirements.txt

# RUN apt-get install -y python-dev default-libmysqlclient-dev libssl-dev
RUN apt-get install -y python-dev libssl-dev
RUN pip3 install --upgrade setuptools
RUN pip3 install django
RUN pip3 install -r requirements.txt


EXPOSE 8000
CMD [ "python3", "manage.py" , "runserver"]