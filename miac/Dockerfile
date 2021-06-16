FROM python:latest

WORKDIR miac
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY . .


CMD ["bash", "django-entrypoint.sh"]
