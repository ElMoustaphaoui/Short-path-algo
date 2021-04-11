# set base image (host OS)
FROM python:3.7

# set the working directory in the container
COPY . /app

WORKDIR /app


# install dependencies
RUN apt-get update && apt-get install -y python3 python3-pip

RUN apt-get -y install python3.7-dev

RUN apt-get install gcc python3-dev musl-dev




# command to run on container start
CMD python ./ShortPathAlgo.py