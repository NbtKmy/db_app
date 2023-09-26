#!/bin/sh

printenv | grep 'MYSQL_USER\|MYSQL_PASSWORD\|MYSQL_DATABASE' |awk '{print "export " $1}' > /scripts/env.sh