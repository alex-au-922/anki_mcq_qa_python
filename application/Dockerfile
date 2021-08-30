FROM fadawar/docker-pyqt5:latest

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=America/Los_Angeles

RUN apt-get update && \
    apt-get install -y tmux wget net-tools tzdata nano vim \
    curl make python3-pip libxcb-xinerama0 libgl1-mesa-glx 

RUN python3 -m pip install --upgrade pip

ENV HOME=/home/user
WORKDIR ${HOME}

COPY utils/ utils/
COPY visual.py .
COPY logic.py .
RUN python3 -m pip install -r utils/requirements.txt 

CMD ["python3","visual.py"]