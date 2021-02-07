from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, TIMESTAMP

Base = declarative_base()


class FlywaySchemaHistory(Base):
    __tablename__ = 'flyway_schema_history'
    installed_rank = Column(Integer, primary_key=True)
    version = Column(String)
    description = Column(String)
    installed_on = Column(TIMESTAMP)


class SurrogateKeyLkp(Base):
    __tablename__ = 'surrogate_key_lkp'
    __table_args__ = {'schema': 'data'}
    surrogate_key = Column(Integer, primary_key=True)
    natural_id = Column(String)
    table_name = Column(String)
    key_domain_data_provider_code = Column(String)
    natural_col_list = Column(String)
    app_key = Column(Integer)
    create_date = Column(String)
    secure_group_key = Column(Integer)
    process_run_key = Column(Integer)


class SurrogateKeyRangeLkp(Base):
    __tablename__ = 'surrogate_key_range_lkp'
    __table_args__ = {'schema': 'data'}
    table_name = Column(String, primary_key=True)
    range_seq_name = Column(String, primary_key=True)
    min_val = Column(Integer)
    max_val = Column(Integer)
    create_date = Column(TIMESTAMP)
    begin_date = Column(TIMESTAMP)
    end_date = Column(TIMESTAMP)
    active_range_ind = Column(String)


class SurrogateCompatibilityLkp(Base):
    __tablename__ = "surrogate_compatibility_lkp"
    __table_args__ = {'schema': 'data'}
    dimension_type_key = Column(Integer, primary_key=True)
    data_provider_key = Column(Integer, primary_key=True)
    object_type_key = Column(Integer, primary_key=True)
    table_name = Column(String)
    key_domain_data_provider_code = Column(String)


class ExecLog(Base):
    __tablename__ = "exec_log"
    __table_args__ = {'schema': 'log'}
    process_run_key = Column(Integer, primary_key=True)
    operation_type = Column(String, primary_key=True)
    operation_status = Column(String, primary_key=True)
    retention_flag = Column(String)
