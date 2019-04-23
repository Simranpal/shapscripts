import logging
logging.getLogger(__name__)
from shaptools import hana

h = hana.HanaInstance('prd', '00', 'YourPassword1234')

params=[['system_replication', 'preload_column_tables', 'true'], ['memorymanager', 'global_allocation_limit', '28000']]
database = 'SYSTEMDB'
file_name= 'global.ini'
layer = 'SYSTEM'
key_name='backupkey'
user_name='system'
user_password='YourPassword1234'

h.set_ini_parameter(
            params,
            database, file_name, layer,
            user_name=user_name, user_password=user_password)
