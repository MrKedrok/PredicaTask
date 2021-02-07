FROM python:3.7
WORKDIR /opt/PredicaTask

RUN apt-get update \
    && apt-get -y install curl gcc g++

COPY ./requirements.txt /opt/PredicaTask
COPY ./development_requirements.txt /opt/PredicaTask
RUN pip3 install -r development_requirements.txt

ENV PYSPARK_PYTHON=python3
ENV PYSPARK_MAJOR_PYTHON_VERSION=3
ENV PYSPARK_DRIVER_PYTHON="python3"

ADD ./coinscoin_lib /opt/PredicaTask/coinscoin_lib
ADD ./management_lib /opt/PredicaTask/management_lib
ADD ./etc /opt/PredicaTask/etc
ADD ./tests /opt/PredicaTask/tests

ADD Containers/coinscoin-base/docker-entrypoint.sh /docker-entrypoint.sh
ADD Containers/coinscoin-base/tini /usr/bin/tini
RUN chmod +x /docker-entrypoint.sh /usr/bin/tini

RUN useradd -d /opt/PredicaTask -u 9999 coinscoin
USER coinscoin

ENTRYPOINT ["/docker-entrypoint.sh"]
