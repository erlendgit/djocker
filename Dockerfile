FROM python:3.10.4

RUN apt update && apt upgrade -y
RUN apt install iputils-ping redis-tools vim -y

RUN echo "alias ls='ls --color'" >> ~/.bashrc
RUN echo "alias ll='ls -l'" >> ~/.bashrc
RUN echo "alias la='ls -la'" >> ~/.bashrc

COPY ./requirements.txt /
COPY ./project /project
WORKDIR /project

RUN pip install --no-cache-dir -r /requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]