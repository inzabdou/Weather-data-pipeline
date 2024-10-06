from extraction import extract_data_from_api
from transformation import clean_and_transform
from loading import load_to_sqlite
from visualization import plot_world_map
from config import API_KEY, API_URL, REQUEST_CITY, DB_PATH

def main():
    # Étape d'extraction
    raw_data = extract_data_from_api(API_URL, API_KEY, REQUEST_CITY)
    
    # Ajout manuel des coordonnées de la ville dans le DataFrame
    raw_data['coord'] = {'lat': 51.5074, 'lon': -0.1278}  # Coordonnées de Londres (latitude, longitude)
    
    # Étape de transformation
    transformed_data = clean_and_transform(raw_data)
    
    # Étape de chargement
    load_to_sqlite(transformed_data, DB_PATH)

    # Visualisation sur la carte
    transformed_data['lat'] = raw_data['coord']['lat']
    transformed_data['lon'] = raw_data['coord']['lon']
    
    plot_world_map(transformed_data)

if __name__ == "__main__":
    main()