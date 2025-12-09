FROM python:3.11-slim

WORKDIR /app

# Force rebuild when code changes
ARG CACHEBUST=1

COPY app.py /app/app.py

RUN pip install --no-cache-dir flask

EXPOSE 5001
CMD ["python", "app.py"]
