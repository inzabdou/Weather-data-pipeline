import pandas as pd
from datetime import datetime

def clean_and_transform(data):
    # Extraire les informations pertinentes dans un DataFrame
    # Extraction du timestamp UNIX et conversion en format lisible
    timestamp = data['dt']
    date_time = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
    df = pd.DataFrame({
        'city': ['London'],
        'temperature_kelvin': [data['main']['temp']],
        'humidity': [data['main']['humidity']],
        'pressure': [data['main']['pressure']],
        'date_time': [date_time]  # Ajout de la date et heure
    })

    # Conversion des unités (Kelvin à Celsius)
    df['temperature_celsius'] = df['temperature_kelvin'] - 273.15
    
    # Suppression des lignes avec des valeurs manquantes (si nécessaire)
    df.dropna(subset=['temperature_celsius', 'humidity'], inplace=True)
    return df