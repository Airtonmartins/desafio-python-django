FROM python:3.7
RUN mkdir /code
WORKDIR /code
COPY djangochallenge/requirements.txt /code/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /code/