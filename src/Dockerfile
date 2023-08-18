FROM python:3.9-alpine

WORKDIR /app

RUN pip install gunicorn==21.0.1

COPY requirements.production.txt .

RUN pip install -r requirements.production.txt --no-cache-dir

COPY . .

RUN chmod +x entrypoint.sh

CMD ["./entrypoint.sh"]
