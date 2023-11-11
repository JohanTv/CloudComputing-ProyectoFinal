FROM tensorflow/tensorflow:2.11.0-jupyter

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV APP_HOME=/home/app/

RUN apt-get update && \
    apt-get install -y ffmpeg libsm6 libxext6 && \ 
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
    
RUN pip install --no-cache-dir opencv-python==4.6.0.66 tqdm==4.66.1

WORKDIR ${APP_HOME}