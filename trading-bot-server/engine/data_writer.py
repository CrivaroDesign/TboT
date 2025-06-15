import pandas as pd
from sqlalchemy.orm import sessionmaker
from db_setup import Base, get_engine, OHLCV
from datetime import datetime

engine = get_engine()
Session = sessionmaker(bind=engine)
session = Session()

def save_ohlcv(symbol, price_list: list[dict]):
    for p in price_list:
        record = OHLCV(
            symbol=symbol,
            timestamp=datetime.fromisoformat(p['timestamp']),
            open=p['open'],
            high=p['high'],
            low=p['low'],
            close=p['close'],
            volume=p['volume']
        )
        session.merge(record)  # merge to avoid duplicates
    session.commit()
    print(f"Saved {len(price_list)} records for {symbol} to DB.")
def close_session():
    session.close()
    print("Session closed.")