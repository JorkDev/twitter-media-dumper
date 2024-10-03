# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make sure the .env file is not included in the image
RUN rm -f .env

# Define environment variables (You can set default values here)
ENV TWITTER_API_KEY=your_api_key \
    TWITTER_API_SECRET=your_api_secret \
    TWITTER_ACCESS_TOKEN=your_access_token \
    TWITTER_ACCESS_SECRET=your_access_secret

# Run main.py when the container launches
CMD ["python", "src/main.py"]
