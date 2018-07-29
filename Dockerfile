# Pull base image.
FROM python:3.5.5-stretch

## make a local directory
RUN mkdir -p /opt/bambu

# set "bambu" as the working directory from which CMD, RUN, ADD references
WORKDIR /opt/bambu

# copy all files to WORKDIR
ADD . .

# pip install the local requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5000

# start the app server  
CMD ["python", "manage.py", "runserver"]