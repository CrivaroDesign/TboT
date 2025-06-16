import requests
import pandas as pd
from datetime import datetime
from sqlalchemy.orm import sessionmaker
from engine.db_setup import OHLCV, get_engine

def fetch_historical(symbol: str, start: str, end: str):
    url = f"https://api.coindesk.com/v1/ohlcv/{symbol}/history"
    params = {'start': start, 'end': end}
    response = requests.get(url, params=params)
    
    if response.status_code != 200:
        print(f"Error fetching data: {response.status_code}")
        return []

    raw_data = response.json().get('prices', [])
    df = pd.DataFrame(raw_data)
    
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')  # adjust format if needed
    return df

def save_to_db(symbol, df):
    engine = get_engine()
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
        session.add(record)

    session.commit()
    session.close()
    print(f"Saved {len(df)} records to DB.")

if __name__ == "__main__":
    symbol = "BTC-USD"
    start = "2020-01-01"
    end = "2025-03-01"
    df = fetch_historical(symbol, start, end)
    if not df.empty:
        save_to_db(symbol, df)
