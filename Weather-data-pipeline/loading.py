import sqlite3

def load_to_sqlite(**kwargs):
    ti = kwargs['ti']
    df = ti.xcom_pull(task_ids='clean_and_transform')
    conn = sqlite3.connect(kwargs['db_path'])
    df.to_sql('weather', conn, if_exists='replace', index=False)
    conn.close()
