# mssql-python-pyodbc
# Python runtime with pyodbc to connect to SQL Server
FROM ubuntu:16.04

# apt-get and system utilities
RUN apt-get update && apt-get install -y \
    curl apt-utils apt-transport-https debconf-utils gcc build-essential g++-5\
    && rm -rf /var/lib/apt/lists/*

# adding custom MS repository
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list > /etc/apt/sources.list.d/mssql-release.list

# install SQL Server drivers
RUN apt-get update && ACCEPT_EULA=Y apt-get install -y msodbcsql unixodbc-dev

# install SQL Server tools
RUN apt-get update && ACCEPT_EULA=Y apt-get install -y mssql-tools
RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc
RUN /bin/bash -c "source ~/.bashrc"

# python libraries
RUN apt-get update && apt-get install -y \
    python-pip python-dev python-setuptools \
    --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# install necessary locales
RUN apt-get update && apt-get install -y locales \
    && echo "en_US.UTF-8 UTF-8" > /etc/locale.gen \
    && locale-gen
RUN pip install --upgrade pip

# install SQL Server Python SQL Server connector module - pyodbc
WORKDIR /opt/PredicaTask
COPY ./requirements.txt /opt/PredicaTask
COPY ./development_requirements.txt /opt/PredicaTask

#RUN apt-get update \
#    && apt-get -y install g++ unixodbc-dev
RUN apt-get update && apt-get -y install python3-pip

RUN pip3 install pyodbc

# install additional utilities
RUN apt-get update && apt-get install gettext nano vim -y

WORKDIR /opt/PredicaTask
COPY ./requirements.txt /opt/PredicaTask
COPY ./development_requirements.txt /opt/PredicaTask

#RUN apt-get update \
#    && apt-get -y install g++ unixodbc-dev

#RUN pip3 install -r development_requirements.txt

#ENV PYSPARK_PYTHON=python3
#ENV PYSPARK_MAJOR_PYTHON_VERSION=3
#ENV PYSPARK_DRIVER_PYTHON="python3"


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

