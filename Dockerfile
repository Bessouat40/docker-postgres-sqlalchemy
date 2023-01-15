FROM ubuntu:20.04

RUN apt-get update
RUN apt-get install python3 python3-pip -y
RUN pip3 install --upgrade pip
RUN apt-get install libffi-dev libssl-dev
WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN apt-get install unixodbc-dev -y

RUN pip3 install -r requirements.txt

COPY ./test.py /app

CMD python3 test.py