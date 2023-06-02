FROM python:3.9.6-slim

WORKDIR /app/backend/

ADD requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ADD . .

RUN chmod +x scripts/migrate.sh && \
    chmod +x scripts/collectstatic.sh && \
    chmod +x scripts/entrypoint.sh


