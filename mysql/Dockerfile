FROM mysql:8-debian

RUN apt-get update && apt-get -y install cron curl
RUN mkdir /tmp

# Add crontab file in the cron directory
ADD ./crons/crontask /etc/cron.d/crontask
# Add shell script for cronjob
ADD ./scripts/cron_injest.sh /scripts/cron_injest.sh

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/crontask
RUN chmod 0644 /scripts/cron_injest.sh

# Apply cron job
RUN crontab /etc/cron.d/crontask
# Create the log file to be able to run tail
RUN touch /var/log/cron.log

# For MySQL
EXPOSE 3306
ADD ./my.cnf /etc/mysql/conf.d/my.cnf

# Run the command on container startup
CMD ["mysqld"] && cron && tail -f /var/log/cron.log