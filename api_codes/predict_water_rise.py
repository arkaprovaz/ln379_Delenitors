from weather_api import get_forecast
from rainfall_model import Rainfall_Model


def get_pred_water_level(city, days=3):
    total_forecast = get_forecast(city, days)

    predicted_water_level = []
    r_model = Rainfall_Model()
    for precip in total_forecast:
        data = {}
        data = precip
        pred_wlevel = round(r_model.dam1_rainfall_rise(
            precip["totalprecip_in"])[0], 3)
        data["pred_wlevel"] = pred_wlevel if pred_wlevel > 0 else 0
        predicted_water_level.append(data)
    return predicted_water_level
