FROM python:3.7 as prod

RUN mkdir /listening
WORKDIR /listening

ADD . /listening





ENV HTTP_PROXY "http://wwwproxy.unimelb.edu.au:8000/"
ENV HTTPS_PROXY "http://wwwproxy.unimelb.edu.au:8000/"
ENV NO_PROXY "localhost,127.0.0.1,localaddress,172.16.0.0/12,.melbourne.rc.nectar.org.au,.storage.unimelb.edu.au,.cloud.unimelb.edu.au"
ENV PYTHONUNBUFFERED 1

RUN pip3 install psutil
RUN pip3 install requests


CMD [ "python","get_information.py" ]
