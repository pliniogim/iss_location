import requests
from datetime import datetime as dt

# lat/long SBC -23.743323,-46.554158
MY_LAT = -23.743323
MY_LONG = -46.554158
MY_FORMAT = 0


# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# # if response.status_code == 404:
# #     raise Exception("Resource not found!")
# # elif response.status_code == 401:
# #     raise Exception("Resource not authorized!")
# # print(response)
# # print(response.json())
#
# response.raise_for_status()
# print(response.json())
#
# data = response.json()["iss_position"]
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
# iss_position = (latitude, longitude)
# print(iss_position)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": MY_FORMAT,
}
response2 = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
# response2 = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response2.raise_for_status()
data = response2.json()
print(data)
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
time_now = dt.now()
print(sunrise, sunset)
print(time_now.hour)

