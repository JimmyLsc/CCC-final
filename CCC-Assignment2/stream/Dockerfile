FROM python:3.7 as prod

RUN mkdir /stream
WORKDIR /stream

ADD . /stream



ENV HTTP_PROXY "http://wwwproxy.unimelb.edu.au:8000/"
ENV HTTPS_PROXY "http://wwwproxy.unimelb.edu.au:8000/"
ENV NO_PROXY "localhost,127.0.0.1,localaddress,172.16.0.0/12,.melbourne.rc.nectar.org.au,.storage.unimelb.edu.au,.cloud.unimelb.edu.au"

RUN pip3 install TwitterAPI
RUN pip3 install vaderSentiment
RUN pip3 install couchdb

EXPOSE 8080
CMD [ "python3","stream.py"]