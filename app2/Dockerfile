FROM python:3.10-slim

WORKDIR /app

ARG CACHEBUST=1

COPY app.py /app/

RUN pip install flask --no-cache-dir

EXPOSE 5002
CMD ["python", "app.py"]
