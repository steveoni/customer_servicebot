
FROM python:3.7-slim-stretch

RUN apt-get update && apt-get install -y git python3-dev gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --upgrade -r requirements.txt

COPY bots/models /bots/models/
COPY bots/config.py /bots/
COPY bots/pred.py /bots/
COPY bots/customer.py /bots/
COPY bots/sendmail.py /bots/

WORKDIR /bots
CMD ["python", "customer.py"]