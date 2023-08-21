FROM python:3.11-alpine

WORKDIR /app

RUN pip install gunicorn==21.2.0

COPY requirements.production.txt .

RUN pip install -r requirements.production.txt --no-cache-dir

COPY . .

RUN chmod +x entrypoint.sh

CMD ["sh", "./entrypoint.sh"]
