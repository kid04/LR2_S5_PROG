import requests
import json
from owm_key import owm_api_key


def get_weather_data(place, api_key=None):
    if api_key:
        with requests.get(
                f'https://api.openweathermap.org/data/2.5/weather?q={place}&appid={api_key}'
        ) as f:
            res = f.json()
            if res['cod'] != 200:
                return None
            res_json = {"name": res["name"], "country": res["sys"]["country"], "coord": res["coord"]}
            tz = int(res["timezone"])
            if tz < 0:
                res_json["timezone"] = "UTC"+str(int(tz/3600))
            else:
                res_json["timezone"] = "UTC+"+str(int(tz/3600))
            res_json["feels_like"] = res["main"]["feels_like"]

        return json.dumps(res_json, indent=4)
