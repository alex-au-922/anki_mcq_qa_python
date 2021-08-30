FROM mongo:latest

RUN apt-get update && apt-get install -y tmux wget net-tools nano vim curl make python3-pip 
RUN python3 -m pip3 upgrade install pip3

ENV HOME=/home/user
WORKDIR ${HOME}

COPY utils/requirements.txt .
RUN pip3 install -r requirements.txt