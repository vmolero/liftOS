
FROM python:3

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

EXPOSE 80

CMD ["python3", "__main__.py"]