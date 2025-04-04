import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

def plot_world_map(df):
    """
    Affiche une carte du monde avec les villes marquées,
    accompagnées de la température et de l'humidité, avec des couleurs améliorées.
    """
    # Créer une figure et définir la carte avec Basemap
    plt.figure(figsize=(12, 8))
    m = Basemap(projection='mill',
                llcrnrlat=-60, urcrnrlat=90,
                llcrnrlon=-180, urcrnrlon=180,
                resolution='c')

    # Ajouter des couleurs pour la carte
    m.drawcoastlines()
    m.drawcountries(linewidth=1.5, color='black')
    m.drawmapboundary(fill_color='aqua')  # Colorer l'océan
    m.fillcontinents(color='lightgreen', lake_color='aqua')  # Colorer la terre et les lacs

    # Ajouter les parallèles et les méridiens
    m.drawparallels(range(-90, 91, 30), labels=[1, 0, 0, 0], fontsize=10, color='gray')
    m.drawmeridians(range(-180, 181, 60), labels=[0, 0, 0, 1], fontsize=10, color='gray')

    # Boucler sur les données des villes dans le DataFrame
    for index, row in df.iterrows():
        # Récupérer les coordonnées géographiques (latitude et longitude)
        lat = row['lat']
        lon = row['lon']
        city = row['city']
        temp = row['temperature_celsius']
        humidity = row['humidity']

        # Convertir les coordonnées latitude/longitude en coordonnées X/Y pour Basemap
        x, y = m(lon, lat)

        # Afficher un point sur la carte à la position de la ville
        m.plot(x, y, 'ro', markersize=5)

        # Annoter la carte avec les informations de température et d'humidité
        plt.text(x, y, f'{city}\nTemp: {temp:.1f}°C\nHumidity: {humidity}%',
                 fontsize=9, ha='left', va='bottom', color='black',
                 bbox=dict(facecolor='white', alpha=0.8, edgecolor='gray'))

    # Afficher la carte
    plt.title('World Weather Map with Temperature and Humidity', fontsize=16)
    plt.show()