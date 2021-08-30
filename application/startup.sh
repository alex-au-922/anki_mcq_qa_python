#!/bin/bash

sudo docker network create anki_mcq_pyqt 

sudo docker run --net anki_mcq_pyqt --name mongodb --env-file .env -v data:/data/db/ -d mongo:latest

sudo docker run --net anki_mcq_pyqt --name anki_application --env-file .env -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix -u qtuser anki 