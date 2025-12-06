FROM python:3.10-slim

WORKDIR /app

# Install system deps
RUN apt-get update && apt-get install -y sqlite3 gcc && apt-get clean

# Copy dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Django uses port 8000
EXPOSE 8000

# Migrate automatically (SQLite file will be created in container)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]