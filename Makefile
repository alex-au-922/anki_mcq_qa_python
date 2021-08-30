build:
	cd application && \
	sudo docker build --tag anki . && \
	cd ..
_unknown: 
	@xhost +local:docker > /dev/null 2>&1
	@bash application/startup.sh > /dev/null 2>&1
down:
	@sudo docker rm -f anki_application mongodb > /dev/null 2>&1
	@sudo docker network rm anki_mcq_pyqt > /dev/null 2>&1
start: _unknown down