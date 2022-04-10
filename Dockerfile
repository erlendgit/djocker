# Explicit is better then implicit...
FROM python:3.10.4-alpine

# Update the package system - build a list of available packages.
RUN apk update && apk upgrade

# Include bash for a little comfort in shell scriptnig, and some debugging tools
RUN apk add bash iputils

# Add a user for security purposes.
RUN adduser www-data -h /home/www -s /bin/bash -G www-data -D

# Copy relevant (-only) project files.
COPY ./requirements.txt /
COPY ./project /project

# At build time, install the packages.
RUN pip install --no-cache-dir -r /requirements.txt

WORKDIR /project

# Serve at port 8000 - as common practice. For communication purpose only. It is expected
#   that at deployment this is taken care of at a docker-compose file or not at all depending
#   on how it is hosted.
EXPOSE 8000

# Don't run as root!
USER www-data
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]