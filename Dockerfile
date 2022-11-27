FROM python:3.10-alpine
RUN apk add --no-cache tzdata
ENV TZ=America/Denver
RUN pip install --upgrade pip
RUN pip install --upgrade python-dotenv twilio requests
WORKDIR /py_cronjob
COPY crontab /py_cronjob
COPY overnight_freeze_notifier.py /py_cronjob
RUN /usr/bin/crontab /py_cronjob/crontab
CMD ["/usr/sbin/crond", "-f", "-d", "0"]
