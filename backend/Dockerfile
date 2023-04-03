FROM python:3.7-slim

# For Crontask
RUN apt-get update && apt-get -y install cron gcc
# Add crontab file in the cron directory
ADD ./crons/task/crontask /etc/cron.d/crontask
RUN chmod 0644 /etc/cron.d/crontask
ADD ./crons/cronscripts/restart_flask.sh /scripts/restart_flask.sh
RUN chmod +x /scripts/restart_flask.sh

# Apply cron job
RUN crontab /etc/cron.d/crontask


ARG project_dir=/src/
ADD ./requirements.txt $project_dir

WORKDIR $project_dir
RUN pip install -r requirements.txt

CMD ["gunicorn", "-c", "gunicorn_conf.py", "app:app"]