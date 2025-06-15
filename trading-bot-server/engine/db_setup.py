import os
from sqlalchemy import create_engine, Column, String, Float, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class OHLCV(Base):
    __tablename__ = 'ohlcv_data'
    id = Column(Integer, primary_key=True)
    symbol = Column(String)              # e.g., BTC-USD
    timestamp = Column(DateTime)         # Time of the OHLCV bar
    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    close = Column(Float)
    volume = Column(Float)

# DB Setup
def get_engine():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, '../storage/historical_data.db')
    return create_engine(f'sqlite:///{os.path.abspath(db_path)}')

def init_db():
    engine = get_engine()
    Base.metadata.create_all(engine)
    print("Database initialized.")

if __name__ == "__main__":
    init_db()
