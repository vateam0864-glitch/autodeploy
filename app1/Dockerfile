FROM python:3.10-slim

WORKDIR /app

ARG CACHEBUST=1

COPY app.py /app/

RUN pip install --no-cache-dir flask

EXPOSE 5001
CMD ["python", "app.py"]
