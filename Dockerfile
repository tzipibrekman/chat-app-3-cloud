# set base image (host OS)
FROM python:3.8-slim
RUN update-ca-certificates
# set the working directory in the container
WORKDIR /code
# copy the dependencies file to the working directory
COPY requirements.txt .
# install dependencies
RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt
# copy the content of the local src directory to the working directory
COPY . .
# Health check configuration
HEALTHCHECK --interval=10s --timeout=3s CMD curl -f http://localhost/health || exit 1

# Make port 80 available to the world outside this container
EXPOSE 80
ENV ROOMS_DIR='./rooms/'
# command to run on container start
CMD [ "python", "./chatApp.py" ] 

