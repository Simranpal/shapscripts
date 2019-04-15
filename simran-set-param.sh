#!/bin/bash
# A simple script

sudo salt-call --local -m /srv/salt/_modules hana.set_ini_parameter \
ini_parameter_values='[["system_replication","preload_column_tables","False"],["memorymanager","global_allocation_limit","28000"]]' \
database=SYSTEMDB \
file_name=global.ini \
layer=SYSTEM \
reconfig=True \
user_name=system \
key_name='"backupkey"' \
user_password=YourPassword1234 \
sid=prd \
inst='"00"' \
password=pass