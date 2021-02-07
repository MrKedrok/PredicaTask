FROM mcr.microsoft.com/mssql/server:2019-latest
ENV ACCEPT_EULA=Y
ENV SA_PASSWORD=Test@12345
ENV MSSQL_PID=Developer
ENV MSSQL_TCP_PORT=1433

WORKDIR /opt/PredicaTask

RUN (/opt/mssql/bin/sqlservr --accept-eula & ) | grep -q "Service Broker manager has started"
#&&  /opt/mssql-tools/bin/sqlcmd -S127.0.0.1 -Usa -PTest@12345
#-Q"RESTORE DATABASE MyProductDB FROM DISK='/dbbackups/MyProductDB.bak';"