import requests
import datetime
from pprint import pprint

api_key = "74a5fda94c344940b6b115337202907"
#city = input("Enter your City :")
city = "Siliguri,WB,IN"

total_out = []
days = 3


url = f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&days={days}"


res = requests.get(url).json()
for data in res["forecast"]["forecastday"]:


    out = {}

    out["date"] = data["date"]
    out["avg_temp"] = data["day"]["avgtemp_c"]
    out["max_temp"] = data["day"]["maxtemp_c"]
    out["min_temp"] = data["day"]["mintemp_c"]
    out["totalprecip_in"] = data["day"]["totalprecip_in"] 
    out["daily_will_it_rain"] = data["day"]["daily_will_it_rain"]
    out["daily_will_it_snow"] = data["day"]["daily_will_it_snow"]
    
    total_out.append(out)


pprint(total_out)