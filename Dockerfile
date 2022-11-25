FROM python:3.10
RUN pip install --upgrade pip
RUN pip install --upgrade python-dotenv twilio requests json datetime pytz
WORKDIR /py_cronjob
COPY crontab /etc/cron.d/crontab
ADD overnight_freeze_notifier.py /py_cronjob
RUN crontab /etc/cron.d/crontab
CMD ["cron", "-f"]
