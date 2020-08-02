import requests
import datetime

api_key = "74a5fda94c344940b6b115337202907"
city = ""

total_forecast = []


def get_forecast(city, days):
    url = f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&days={days}"
    res = requests.get(url).json()
    for data in res["forecast"]["forecastday"]:
        forecast = {}
        forecast["date"] = data["date"]
        forecast["avg_temp"] = data["day"]["avgtemp_c"]
        forecast["max_temp"] = data["day"]["maxtemp_c"]
        forecast["min_temp"] = data["day"]["mintemp_c"]
        forecast["totalprecip_in"] = data["day"]["totalprecip_in"]
        forecast["daily_will_it_rain"] = data["day"]["daily_will_it_rain"]
        forecast["daily_chance_of_rain"] = data["day"]["daily_chance_of_rain"]
        forecast["daily_will_it_snow"] = data["day"]["daily_will_it_snow"]
        forecast["daily_chance_of_snow"] = data["day"]["daily_chance_of_snow"]
        total_forecast.append(forecast)
    return total_forecast


if __name__ == "__main__":
    print(get_forecast("Siliguri,WB,IN", 3))
