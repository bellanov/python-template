
FROM python:3.10-alpine

COPY . /app
WORKDIR /app

# Install dependencies
RUN pip install -r requirements.txt

# Bootstrap application
ENTRYPOINT [ "scripts/entrypoint.sh" ]
