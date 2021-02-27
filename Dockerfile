FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential libmysqlclient-dev
RUN mkdir -p /home/app
COPY . /app
WORKDIR /app
#RUN pip install virtualenv
#RUN virtualenv runenv
#RUN /bin/bash -c "source runenv/bin/activate" 
RUN pip install pybuilder
RUN pyb install_dependencies
#RUN export PYTHONPATH="src/main/python"
ENTRYPOINT ["python"]
CMD ["src/main/scripts/start_system_analyzer"]