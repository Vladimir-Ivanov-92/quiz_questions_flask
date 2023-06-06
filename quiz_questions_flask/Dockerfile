FROM python:3.11-alpine

# Инициализация проекта
WORKDIR /app

# PYTHONUNBUFFERED отвечает за отключение буферизации вывода (output).
# То есть непустое значение данной переменной среды гарантирует,
# что мы можем видеть выходные данные нашего приложения в режиме реального времени.
ENV PYTHONUNBUFFERED 1
#PYTHONDONTWRITEBYTECODE означает, что Python не будет пытаться создавать файлы .pyc.
ENV PYTHONDONTWRITEBYTECODE 1

# copy requirements file
COPY ./requirements.txt /app

# install dependencies
RUN pip install --upgrade pip setuptools wheel \
    && pip install -r /app/requirements.txt \
    && rm -rf /root/.cache/pip

# весь проект просто копируется внутрь контейнера, в WORKDIR.
COPY . .

# Приложение запускается на внутреннем порту 5050
EXPOSE 5050


#CMD ["python", "run.py"]
#CMD [ "flask", "run","--host","0.0.0.0","--port","5050"]
