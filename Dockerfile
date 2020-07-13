# STEP 1: Install base image. Optimized for Python.
FROM python:3.7-slim-buster

# Step 2: Install build-essential for it's C compiler needed for portaudio
RUN apt-get update && apt-get -y install portaudio19-dev python-pyaudio gcc g++ alsa-utils

# Step 4: Add requirements.txt file
COPY requirements.txt /requirements.txt

# Step 5:  Install required pyhton dependencies from requirements file
RUN pip install pyaudio
RUN pip install -r requirements.txt

# Step 6: Copy source code in the current directory to the container
ADD . /app

# Step 7: Set working directory to previously added app directory
WORKDIR /app

# Step 8: Expose the port Flask is running on
EXPOSE 8000

# Step 9: Run Flask
CMD ["flask", "run", "--host=0.0.0.0", "--port=8000"]
