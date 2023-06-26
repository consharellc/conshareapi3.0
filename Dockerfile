# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.9.6

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1

# create root directory for our project in the container
RUN mkdir /conshareapi3.0

# Set the working directory to /conshareapi
WORKDIR /conshareapi3.0

# Copy the current directory contents into the container at /conshareapi
ADD . /conshareapi3.0/

# Allows docker to cache installed dependencies between builds
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000  
# start server  
CMD python manage.py runserver 

