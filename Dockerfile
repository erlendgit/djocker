# Explicit is better then implicit... we use python 3.10.4. Period.
FROM python:3.10.4

# Update the apt system - build a list of available packages.
RUN apt update && apt upgrade -y

# Install some tools for debugging. I'm used to virtual machines, so at first installing vim
#   seemed a good idea. I never used it ;-) But I keep it here as a reminder about where I
#   come from.
RUN apt install iputils-ping redis-tools vim -y

# It always annois me if basic file listing functionality is not present at virtual machines.
# Since I probably still spend some time inside the container I prefer to have some eye candy
#   in place.
RUN echo "alias ls='ls --color'" >> /etc/bash.bashrc
RUN echo "alias ll='ls -l'" >> /etc/bash.bashrc
RUN echo "alias la='ls -la'" >> /etc/bash.bashrc

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