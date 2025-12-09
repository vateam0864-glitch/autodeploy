FROM python:3.10-slim

# Change this folder first
WORKDIR /app

# Add cache invalidator BEFORE copying source
ARG CACHEBUST=1

# Copy source AFTER cache invalidator (forces rebuild)
COPY . /app/

RUN pip install --no-cache-dir flask

EXPOSE 5002
CMD ["python", "app.py"]
