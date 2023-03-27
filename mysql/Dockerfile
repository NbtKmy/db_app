FROM mysql:8-debian

RUN apt-get update && apt-get -y install cron curl
RUN mkdir /csv_temps



ADD ./csv/* /csv_temps/

ADD ./sqls/* /docker-entrypoint-initdb.d/
RUN chmod +x /docker-entrypoint-initdb.d/a_initialize.sh
RUN chmod +x /docker-entrypoint-initdb.d/b_ingest.sh


# Add crontab file in the cron directory
ADD ./crons/crontask /etc/cron.d/crontask
# Add shell script for cronjob
ADD ./scripts/cron_ingest.sh /scripts/cron_ingest.sh
ADD ./scripts/for_cron.sh /scripts/for_cron.sh


# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/crontask
RUN chmod +x /scripts/cron_ingest.sh
RUN chmod +x /scripts/for_cron.sh
# RUN chmod +x /scripts/start_container.sh

# Apply cron job
RUN crontab /etc/cron.d/crontask


# For MySQL
EXPOSE 3306
ADD ./my.cnf /etc/mysql/conf.d/my.cnf


# Run the command on container startup
CMD ["mysqld"]