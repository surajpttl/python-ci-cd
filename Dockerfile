FROM python:3.10.7

ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8001

CMD ["python3","manage.py","configurator" ]