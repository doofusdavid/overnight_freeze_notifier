from dotenv import load_dotenv
import json, os, requests, pytz
from datetime import datetime
from twilio.rest import Client


def format_date(date):
    return date.strftime("%-m/%-d/%y %-I:%M %p")

if __name__ == '__main__':
    load_dotenv()

    # Get the environment variables
    api_key = os.getenv("OPENWEATHERMAPAPIKEY")
    temp_threshold = os.getenv("TEMP_THRESHOLD")
    location_lat = os.getenv("LOCATION_LAT")
    location_lon = os.getenv("LOCATION_LON")
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    twilio_from_number = os.getenv('TWILIO_FROM_NUMBER')
    twilio_to_number = os.getenv('TWILIO_TO_NUMBER')


    if os.getenv("DEBUG") == "True":
        weather_data = json.loads(open("sample_response.json").read())
    else:
        base_url = "https://api.openweathermap.org/data/3.0/onecall"
        call_url = f"{base_url}?lat={location_lat}&lon={location_lon}&exclude=minutely,alerts&appid={api_key}&units=imperial"
        response = requests.get(call_url)
        weather_data = json.loads(response.text)

    timezone = pytz.timezone("America/Denver")
    current_date = timezone.localize(datetime.fromtimestamp(weather_data["current"]["dt"]))

    message = "Good Morning Sara! Here's your weather report for today:\n\n"
    message += f"Current Time: {format_date(current_date)}\n"
    message += f"Current Temperature: {weather_data['current']['temp']}°F\n"
    message += f"Your Current Temperature Threshold: {temp_threshold}°F"

    horsey_message = ""
    for hour in weather_data["hourly"]:
        hour_date = timezone.localize(datetime.fromtimestamp(hour["dt"]))
        if hour["temp"] <= float(temp_threshold):
            horsey_message += f"Cold 🐴 Warning!: {format_date(hour_date)} - {hour['temp']}°F\n"
    
    if len(horsey_message)  > 0:
        message += "\n" + horsey_message
    else:
        message += "\n\nNo need to worry about the horses today! The temperature is above your threshold."

    if os.getenv("DEBUG") == "True":
        print(message)
    else:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=message,
            from_=twilio_from_number,
            to=twilio_to_number )
        print( message.sid)
