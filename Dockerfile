FROM resin/rpi-raspbian:latest

# Install dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    python \
    python-dev \
    python-pip \
    python-virtualenv

ADD . /

RUN pip install --upgrade -r requirements.txt

RUN chmod +x build_image.sh

# Define default command
CMD ["python", "main.py"]
