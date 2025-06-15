# trading-bot-server/engine/init_db.py

from sqlalchemy import create_engine
from db_setup import Base

engine = create_engine('sqlite:///../data/market_data.db')  # Or use PostgreSQL URL
Base.metadata.create_all(engine)
print("Database initialized and tables created.")