import sqlite3

def load_to_sqlite(df, db_path):
    conn = sqlite3.connect(db_path)
    df.to_sql('weather', conn, if_exists='replace', index=False)
    conn.close()
