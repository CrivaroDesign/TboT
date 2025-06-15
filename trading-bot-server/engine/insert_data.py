from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_setup import PriceData
from datetime import datetime

engine = create_engine('sqlite:///../data/market_data.db')
Session = sessionmaker(bind=engine)
session = Session()

def save_price_data(symbol, prices: list[dict]):
    for p in prices:
        record = PriceData(
            symbol=symbol,
            timestamp=datetime.fromisoformat(p['timestamp']),
            open=p['open'],
            high=p['high'],
            low=p['low'],
            close=p['close'],
            volume=p['volume']
        )
        session.merge(record)  # merge avoids duplicates
    session.commit()
