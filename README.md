# Weather Data Pipeline
This project demonstrates a scalable ETL (Extract, Transform, Load) pipeline that processes real-time weather data from the OpenWeather API. It fetches weather data, cleans and transforms it, stores it in a SQLite database, and visualizes the data on a world map.

## Features
* Data Extraction: Retrieves real-time weather data (temperature, humidity, pressure, etc.) from the OpenWeather API for a specified city.
* Data Transformation: Cleans and processes the raw data, converting temperatures from Kelvin to Celsius and formatting the date and time.
* Data Storage: Stores the cleaned data in a SQLite database for persistent storage and easy access.
* Data Visualization: Displays the weather conditions on a world map, with markers indicating the temperature and humidity for the chosen city.
* Scalability: The project is designed to be easily extended to support more cities and advanced analytics.

## Project Structure
* extraction.py: Handles the API call to extract weather data.
* transformation.py: Cleans and transforms the extracted data into a pandas DataFrame.
* loading.py: Loads the cleaned data into a SQLite database.
* visualization.py: Visualizes the weather data on a world map, showing the location of the city along with temperature and humidity.
* config.py: Stores configuration variables such as API key, database path, and city details.
* main.py: Orchestrates the entire ETL process and runs the pipeline.
* requirements.txt: Lists all required Python packages.


## Future Improvements

- Automate data extraction using Airflow or cron jobs
- Migrate to a cloud-based database like PostgreSQL or BigQuery
- Handle large data volumes using Apache Spark
