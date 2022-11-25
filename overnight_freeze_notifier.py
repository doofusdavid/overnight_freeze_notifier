from dotenv import load_dotenv
import json, os, twilio, requests, pytz
from datetime import datetime



if __name__ == '__main__':
    load_dotenv()

    # Get the environment variables
    api_key = os.getenv("OPENWEATHERMAPAPIKEY")
    temp_threshold = os.getenv("TEMP_THRESHOLD")
    location_lat = os.getenv("LOCATION_LAT")
    location_lon = os.getenv("LOCATION_LON")

    if os.getenv("DEBUG") == "True":
        weather_data = json.loads(open("sample_response.json").read())
    else:
        base_url = "https://api.openweathermap.org/data/3.0/onecall"
        call_url = f"{base_url}?lat={location_lat}&lon={location_lon}&exclude=current,minutely,alerts&appid={api_key}&units=imperial"
        response = requests.get(call_url)
        weather_data = json.loads(response.text)

    timezone = pytz.timezone("America/Denver")
    current_date = timezone.localize(datetime.fromtimestamp(weather_data["current"]["dt"]))
    print(f"Current date: {current_date}")

    message = "Good Morning Sara! Here's your weather report for today:\n\n"
    message += f"Current Time: {current_date}\n"
    message += f"Current Temperature: {weather_data['current']['temp']}°F\n"
    message += f"Your Current Temperature Threshold: {temp_threshold}°F\n"
    

