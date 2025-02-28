FROM python:3.9-slim

WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Create a volume for the database
VOLUME /app/data

# Set environment variable to use the volume for the database
ENV SQLALCHEMY_DATABASE_URI=sqlite:///data/tasks.db

# Expose the port the app runs on
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"] 