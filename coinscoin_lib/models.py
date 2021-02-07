from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, TIMESTAMP

Base = declarative_base()


class CoinpapricaTop100Coins(Base):
    __tablename__ = 'coinpaprica_top_100_coins_fct'
    __table_args__ = {'schema': 'data'}
    currect_day = Column(TIMESTAMP, primary_key=True)
    current_time = Column(TIMESTAMP)
    open_day_value = Column(Integer)
    high_value_current_day = Column(Integer)
    low_value_current_day = Column(Integer)
    current_value_current_day = Column(Integer)
    current_volume = Column(Integer)
    market_cap = Column(Integer)
    coin_id = Column(String)
