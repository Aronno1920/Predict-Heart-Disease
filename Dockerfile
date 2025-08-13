FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy files
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

# Run app
CMD ["uvicorn", "app.main:app", "--host", "127.0.0.1", "--port", "8000"]
