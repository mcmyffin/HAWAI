FROM python:3-onbuild

RUN apt-get -y update && pip install --upgrade pip

EXPOSE 8888

CMD ["python3", "./ping_bottle.py"]

