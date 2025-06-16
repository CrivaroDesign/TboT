import os
from sqlalchemy import create_engine, Column, String, Float, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class OHLCV(Base):
    __tablename__ = 'ohlcv'
    id = Column(Integer, primary_key=True)
    symbol = Column(String)              # e.g., BTC-USD
    timestamp = Column(DateTime)         # Time of the OHLCV bar
    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    close = Column(Float)
    volume = Column(Float)

# DB Setup - Function to get a specific DBs paired with symbols
def get_engine_for_symbol(symbol):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_name = symbol.lower().replace("-", "_") + ".db"
    db_path = os.path.join(base_dir, '../storage/{db_name}')
    engine = create_engine(f"sqlite:///{os.path.abspath(db_path)}")
    Base.metadata.create_all(engine)
    print("Database initialized. Pair:{symbol}")
    return engine
