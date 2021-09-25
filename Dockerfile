# init a base image (Alpine is small Linux distro)
FROM python:3.7.1-alpine
# define the present working directory
WORKDIR /docker-flask-app
# copy the contents into the working dir
ADD . /docker-flask-app
# run pip to install the dependencies of the flask app
RUN pip install -r requirements.txt
# expose a port
EXPOSE 8080
# define the command to start the container
CMD ["python","app.py"]