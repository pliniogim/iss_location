import time
import requests
import smtplib
from datetime import datetime as dt
import key

# lat/long SBC -23.743323,-46.554158
MY_LAT = -23.743323
MY_LONG = -46.554158
MY_FORMAT = 0
MY_EMAIL = 'pliniogimenez@gmail.com'
MY_KEY = key.KEY


def send_email():
    conn = smtplib.SMTP("smtp.gmail.com", 587)
    conn.starttls()
    conn.login(user=MY_EMAIL, password=MY_KEY)
    conn.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg="Subject:Look up!\n\nThe ISS is above you in the sky.")


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    dataiss = response.json()["iss_position"]
    longitude = float(dataiss["longitude"])
    latitude = float(dataiss["latitude"])
    return latitude, longitude


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data_night = response.json()
    sunrise = int(data_night["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data_night["results"]["sunset"].split("T")[1].split(":")[0])
    time_now_night = dt.now()
    if time_now_night.hour >= sunset or time_now_night.hour <= sunrise:
        return True
    else:
        return False


while True:
    iss_position = is_iss_overhead()

    if MY_LAT - 5 <= iss_position[0] <= MY_LAT + 5 and MY_LONG - 5 <= iss_position[1] <= MY_LONG + 5:
        if is_night():
            send_email()
        else:
            print("The ISS is not visible in the sky in daylight.")
    else:
        print(f"The ISS is not near you in the sky. "
              f"\nIt is at {iss_position[0]}, {iss_position[1]}."
              f"\nYour position is {MY_LAT}, {MY_LONG}.")
    time.sleep(60)
