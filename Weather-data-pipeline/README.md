# Weather Data Pipeline

This project demonstrates a scalable ETL (Extract, Transform, Load) pipeline that processes real-time weather data from the OpenWeather API. It fetches weather data, cleans and transforms it, stores it in a SQLite database, and visualizes the data on a world map.

## Features

* **Data Extraction**: Retrieves real-time weather data (temperature, humidity, pressure, etc.) from the OpenWeather API for a specified city.
* **Data Transformation**: Cleans and processes the raw data, converting temperatures from Kelvin to Celsius and formatting the date and time.
* **Data Storage**: Stores the cleaned data in a SQLite database for persistent storage and easy access.
* **Data Visualisation**: Displays the weather conditions on a world map, with markers indicating the temperature and humidity for the chosen city.
* **Scalability**: The project is designed to be easily extended to support more cities and advanced analytics.

## Project Structure

* `extraction.py`: Handles the API call to extract weather data.
* `transformation.py`: Cleans and transforms the extracted data into a pandas DataFrame.
* `loading.py`: Loads the cleaned data into a SQLite database.
* `config.py`: Stores configuration variables such as API key, database path, and city details.
* `weather_pipeline_dag.py`: Defines the Airflow DAG for automating the ETL pipeline.
* `visualization.py`: Visualizes the weather data on a world map, showing the location of the city along with temperature and humidity.
* `requirements.txt`: Lists all required Python packages.

## Setup and Installation

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/weather-data-pipeline.git
cd weather-data-pipeline
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Initialize Apache Airflow
```bash
export AIRFLOW_HOME=$(pwd)/airflow
airflow db init
```

### 5. Start Apache Airflow
```bash
airflow webserver --port 8080 &
airflow scheduler &
```

### 6. Run the DAG
You can run the DAG through the Airflow web interface (http://localhost:8080/) or manually using the following command:
```bash
airflow dags trigger weather_data_pipeline
```

## Future Improvements

- Migrate to a cloud-based database like PostgreSQL or BigQuery.
- Extend visualization capabilities by creating a dashboard using Power BI or Tableau.