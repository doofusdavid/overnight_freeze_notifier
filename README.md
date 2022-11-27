# Overnight Freeze Notifier

My wife has a horse being boarded outside, and wanted to know when she needed to run to him to cover him with a blanket.  
She needed to set a temperature limit and get notified. I created this with a few requirements.

- Docker image shown here: https://hub.docker.com/repository/docker/doofusdavid/overnightfreezenotifier
- Sample .env provided in the Repo. Temperature in Farenheit, Lat/Lng works to 4 decimal places. Running this manually will pull from a .env file, running in docker requires the environment variables set, or using a docker compose file with those variables set.
- SMS courtesy of [Twilio](https://www.twilio.com/) . You'll need to sign up for a account and get your own API key
- Weather courtesy of [Open Weather](https://openweathermap.org/). You'll need to sign up and get an API key.

Apollo says, "Thanks!"
![Apollo the horse](/img/Apollo.jpeg)
