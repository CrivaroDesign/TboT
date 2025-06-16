# engine/data_writer.py

from sqlalchemy.orm import sessionmaker
from engine.db_setup import OHLCV

def save_ohlcv(engine, symbol, df):
    Session = sessionmaker(bind=engine)
    session = Session()

    for _, row in df.iterrows():
        record = OHLCV(
            symbol=symbol,
            timestamp=row['timestamp'],
            open=row['open'],
            high=row['high'],
            low=row['low'],
            close=row['close'],
            volume=row['volume']
        )
        session.merge(record)   # merge to avoid duplicates
    session.commit()
    session.close()
    print("Session closed.")