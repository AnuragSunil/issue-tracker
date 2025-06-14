# Use the official lightweight Python image
FROM python:3.10-slim

#Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONNUNBUFFERED=1

# Set working director inside the container
WORKDIR /app

# Copy project files
COPY . .

# Install Dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose port 5000
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]