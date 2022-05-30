FROM python:3.9

RUN mkdir /app/

WORKDIR /app/

COPY . .

RUN pip install -r requirements.txt

RUN apt-get update

RUN apt-get install ffmpeg libsm6 libxext6  -y

RUN apt-get install gstreamer1.0-tools -y

RUN apt-get install -y gstreamer1.0-plugins-good -y

RUN apt-get install -y gstreamer1.0-plugins-ugly

RUN apt install -y gstreamer1.0-plugins-bad

CMD ["python", "main.py", "docker"]