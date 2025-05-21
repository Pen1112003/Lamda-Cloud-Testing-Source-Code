FROM python:3.9-slim

WORKDIR /app

# Cài đặt dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy code
COPY . .

# Expose port
EXPOSE 8000

# Chạy ứng dụng
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app.app:app"] 