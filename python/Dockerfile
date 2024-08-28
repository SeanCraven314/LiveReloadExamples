FROM python:3

WORKDIR /server
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt --no-cache-dir

## This is optional
COPY ./app ./app

CMD ["uvicorn", "app.server:app", "--host", "0.0.0.0", "--port", "80", "--reload"]


