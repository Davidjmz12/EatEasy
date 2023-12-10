# pull official base image
FROM python:3
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /usr/src/app

# install dependencies
# RUN pip install --upgrade pip
COPY ./requirements.txt .
# copy project
COPY . .

RUN pip install -r requirements.txt