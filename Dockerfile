
FROM python:3.10-alpine
COPY . /app
WORKDIR /app
CMD [ "python", "/app/python_package/hello.py" ]