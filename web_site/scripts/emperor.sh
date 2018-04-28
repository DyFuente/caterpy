#!/bin/sh
# Start new process of uwsgi and restart nginx.

PROC=`pgrep -fl uwsgi`
[ -n "${PROC}" ] && pkill -9 -af uwsgi; sleep 1

UWSGI="/usr/local/www/bin/uwsgi"
VASSALS="/usr/local/etc/nginx/uwsgi/vassals"
LOG="/var/log/uwsgi/emperor_caterpy.log"

$UWSGI --emperor $VASSALS --uid www --gid www --daemonize $LOG

service nginx restart
