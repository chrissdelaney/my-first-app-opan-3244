import pandas as pd

from app.weather import get_location_data, get_current_weather_data, display_weather_forecast


def test_weather():
    #test for getting location data
    assert isinstance(get_location_data("20007"), pd.Series) 
    assert isinstance(get_location_data("08540"), pd.Series) 

    #test for getting current weather data
    assert get_current_weather_data(latitude=38.9144, longitude=-77.074, postal_code="20007").status_code == 200

    #test for weather forecast
    r = get_current_weather_data(latitude=38.9144, longitude=-77.074, postal_code="20007")
    assert display_weather_forecast(r) == 7

    print()
    print("ALL TESTS PASS!")

