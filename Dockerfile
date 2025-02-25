# FROM python:3.11
# WORKDIR /app
# COPY . /app
# RUN pip install --no-cache-dir -r requirements.txt
# CMD ["python", "main.py"]
FROM python:3.11
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python3", "producer.py"]
