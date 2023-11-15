import pgeocode
import requests
import json
import pandas as pd

DEGREE_SIGN = '\u00B0'

def get_location_data(zip_code:str):
    print(f"Getting data for postal code {zip_code}...")
    nomi = pgeocode.Nominatim("US")
    results = nomi.query_postal_code(zip_code)
    
    return results

def get_current_weather_data(longitude:float, latitude:float, postal_code:str):
    print("Fetching weather data for postal code 20007...")
    url = f"https://api.weather.gov/points/{latitude},{longitude}"
    parsed_response = {}
    try:
        response = requests.get(url)
        parsed_response = json.loads(response.text)
    except:
        print("Failed to Fetch Weather Data!")
        return "OOPS! Failed to Fetch Weather Data!"

    forecast_url = parsed_response["properties"]["forecast"]
    parsed_forecast_response = {}

    try:
        forecast_response = requests.get(forecast_url)

    except:
        return "OOPS! Failed to Fetch Forecast Data!"
    

    return forecast_response

def display_weather_forecast(response):
    parsed_response = json.loads(response.text)
    periods = parsed_response["properties"]["periods"]
    daytime_periods = [period for period in periods if period["isDaytime"] == True]

    print("YOUR 7 DAY FORECAST:")
    print("-------------")

    for period in daytime_periods:
        #print(period.keys())
        print("-------------")
        print(period["name"], period["startTime"][0:7])
        print(period["shortForecast"], f"{period['temperature']} {DEGREE_SIGN}{period['temperatureUnit']}")
        #print(period["detailedForecast"])

    return len(daytime_periods) #corect would be 7
        

if __name__ == "__main__":
    loc_data = get_location_data("20007")
    
    longitude = float(loc_data['longitude'])
    latitude = float(loc_data['latitude'])
    postal_code = loc_data['postal_code']

    forecast_response = get_current_weather_data(longitude=longitude, latitude=latitude, postal_code=postal_code)

    display_weather_forecast(forecast_response)


