from decimal import Decimal
from sqlalchemy import DATE, DECIMAL, TIMESTAMP, Column, Integer, Numeric, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import MetaData

Base = declarative_base(metadata=MetaData(schema="securities"))

class Zerodha_Master_List(Base):
    __tablename__ = "zerodha_master_list"
    instrument_token = Column(String(15), primary_key = True)
    exchange_token = Column(String(10), primary_key = True)
    trading_symbol = Column(String(100), primary_key=True)
    security_name = Column(String(100))
    last_price = Column(Numeric(precision=10, scale=4, asdecimal=True))
    expiry = Column(DATE)
    strike_price = Column(Numeric(precision=10, scale=4, asdecimal=True))
    tick_size = Column(Numeric(precision=10, scale=4, asdecimal=True))
    lot_size = Column(Integer)
    instrument_type = Column(String(5))
    segment = Column(String(15))
    exchange = Column(String(3))
    insertion_timestamp = Column(TIMESTAMP(timezone=True))