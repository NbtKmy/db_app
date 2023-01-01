FROM mysql:8-debian

RUN apt-get update && apt-get -y install cron curl
RUN mkdir /csv_temps
ADD ./sqls/* /docker-entrypoint-initdb.d/
RUN chmod +x -R /docker-entrypoint-initdb.d/b_ingest.sh


# Add crontab file in the cron directory
ADD ./crons/crontask /etc/cron.d/crontask
# Add shell script for cronjob
ADD ./scripts/cron_ingest.sh /scripts/cron_ingest.sh

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/crontask
RUN chmod 0644 /scripts/cron_ingest.sh

# Apply cron job
RUN crontab /etc/cron.d/crontask
# Create the log file to be able to run tail
RUN touch /var/log/cron.log

# For MySQL
EXPOSE 3306
ADD ./my.cnf /etc/mysql/conf.d/my.cnf
# RUN /scripts/2_injest.sh

# Run the command on container startup
CMD ["mysqld"] && cron && tail -f /var/log/cron.log