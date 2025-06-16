# engine/insert_historical.py

from engine.fetch_data import fetch_historical
from engine.data_writer import save_ohlcv
from engine.db_setup import get_engine_for_symbol
import os

symbols = ['BTC-USD', 'ETH-USD', 'MATIC-USD']
start_date = '2020-01-01'
end_date = '2025-01-01'

base_dir = os.path.dirname(os.path.abspath(__file__))
storage_dir = os.path.join(base_dir, '../storage')

os.makedirs(storage_dir, exist_ok=True)

for symbol in symbols:
    print(f"\n📥 Processing {symbol}...")

    engine = get_engine_for_symbol(symbol)

    df = fetch_historical(symbol, start_date, end_date)

    print(f"💾 Inserting {len(df)} rows into {symbol.lower().replace('-', '_')}.db")
    save_ohlcv(engine, symbol, df)

print("\n✅ Done: All symbols processed.")
