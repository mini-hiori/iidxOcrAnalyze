# ref:https://qiita.com/narista/items/a3d7d26ae50d54c2553a
FROM python:3.8-buster as builder

RUN pip install --upgrade pip

# Add the following line to get native library of OpenCV.
RUN apt-get update && apt-get install -y libopencv-dev 

WORKDIR /app
# Replace this line to copy requirements.txt inside the docker image.
ADD ./requirements.txt /app

RUN python3 -m pip install -r requirements.txt
CMD ["python3"]