FROM mcr.microsoft.com/mssql/server:2019-latest
ENV ACCEPT_EULA=Y
ENV SA_PASSWORD=cardano1dolek!
ENV MSSQL_PID=Developer
ENV MSSQL_TCP_PORT=1433

WORKDIR /opt/PredicaTask
ADD ./etc /opt/PredicaTask/etc


#RUN chmod +rwx /etc/ssl/openssl.cnf
#RUN sed -i 's/TLSv1.2/TLSv1/g' /etc/ssl/openssl.cnf
#RUN sed -i 's/SECLEVEL=2/SECLEVEL=1/g' /etc/ssl/openssl.cnf

RUN (/opt/mssql/bin/sqlservr --accept-eula & ) | grep -q "Service Broker manager has started" &&  /opt/mssql-tools/bin/sqlcmd -S127.0.0.1 -Usa -Pcardano1dolek! -Q"RESTORE DATABASE [coinscoin-dev] FROM  DISK = N'/opt/PredicaTask/etc/coinscoin-dev.BAK' WITH  FILE = 1,  MOVE N'coinscoin-dev' TO N'/var/opt/mssql/data/coinscoin-dev.mdf'"