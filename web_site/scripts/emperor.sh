#!/bin/sh
# Start new process of uwsgi and restart nginx.

PROC=`pgrep -fl uwsgi`
[ -n "${PROC}" ] && pkill -9 -f uwsgi; sleep 1

UWSGI="/usr/local/www/caterpy/bin/uwsgi"
VASSALS="/usr/local/etc/"
LOG="/var/log/uwsgi/emperor_caterpy.log"

$UWSGI --emperor $VASSALS --uid www-data --gid www-data --daemonize $LOG

service nginx restart
