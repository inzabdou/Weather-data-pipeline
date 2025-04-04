import requests

# Fait appel à l'API pour extraire les données en temps réel
def extract_data_from_api(api_url, api_key, request_city):
    print(f'{api_url}{request_city}&APPID={api_key}')
    response = requests.get(f'{api_url}{request_city}&APPID={api_key}')
    data = response.json()
    return data
