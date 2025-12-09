# app1 Dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY app.py /app/
RUN pip install --no-cache-dir flask
EXPOSE 5001
ENV PYTHONUNBUFFERED=1
CMD ["python", "-u", "app.py"]
