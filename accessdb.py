import sqlite3
import pandas as pd

# Connexion à la base de données SQLite
conn = sqlite3.connect('weather_data.db')

# Exécute une requête SQL pour récupérer toutes les données de la table 'weather'
query = "SELECT * FROM weather"
df = pd.read_sql_query(query, conn)

# Affiche le contenu de la table sous forme de DataFrame pandas
print(df)

# Fermeture de la connexion
conn.close()
