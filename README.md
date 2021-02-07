# PredicaTask
PredicaTask ETL process

Please look at the task described below. The approach, implementation (code quality) and response time will
be evaluated.

1. Prepare database and SSIS package or script or Azure Data Factory pipeline downloading data on
   average exchange rates from European Central Bank (https://exchangeratesapi.io/) or National Bank of
   Poland (http://www.nbp.pl/home.aspx?f=/kursy/instrukcja_pobierania_kursow_walut.html)
#Comments   
      - used coinpaprica api for colled data about crypto coins.
      - database is docker image SQL server "mcr.microsoft.com/mssql/server:2019-latest" running on ubuntu.
      - to process data using pandas dataframes.
      - to schedule task to queque used cellery on redis.

   a. Package or script must be able to run once a day to download the latest exchange rates, while the
   historical ones should be stored in the database.

- to trigger processing I used celery queque on redis and task type periodic.
  
main task is "data_dump_task", we can guide the firing time from "coinscoin.conf" file


   b. The choice of the communication interface and database schema is yours – of course, the simpler,
   the better
- I took sqlalchemy lib with pyodbc object to connect sql server database.


   c. List of currencies to download should be configurable (preferably in the database)
why from a database? when we have parametrized something it should be parametrized on the front app. Example in api client. Then our service do not need connect to other service to get config.
in my topic it is count of coins to collect. configurable it is in etc/coinscoin.conf file. 

   d. Creativity is very welcome
-----------
I have created 2 instance of application, 
- first for management for a task, it is management_lib, that instance has separate container to push tasks to queque
- second is worker for management task, it is coinscoin_lib, that instance has separate container to transform data from coinpaprica to sql server

extra stuff
- local sql server on a docker with open ports and autorestore database from backup file (/opt/PredicaTask/etc/coinscoin-dev.BAK).
- monitor container to monitor celery queue on flower, access below url 127.0.0.1:5555 when we start redis 

------------


2. Prepare simple SSAS (Multidimensional or Tabular) analytics cube based on collected
   data. The cube should be consist of at least:
   a. Dimensions: Time and Currency
   b. Facts: exchange rates by time with an aggregating measure
   c. Creativity is very welcome
3. Prepare simple report:
   a. Using Power BI, Reporting Services or Excel (one of those listed)
   b. The report should be based on data from the analytics cube or the database (in the absence of
   knowledge of DAX and MDX)
   c. The report should illustrate the change in the exchange rate of the selected currency over time
   d. It should be feasible to select a specific currency and the time period for which the data is displayed
   e. Creativity is very welcome
   Please send the resulting files with the code (complete Visual Studio project).
