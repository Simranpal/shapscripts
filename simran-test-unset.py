import logging
logging.getLogger(__name__)
from shaptools import hana

h = hana.HanaInstance('prd', '00', 'YourPassword1234')

param_list_unset = [['system_replication', 'preload_column_tables'],['memorymanager', 'global_allocation_limit']]

database = 'SYSTEMDB'
file_name= 'global.ini'
layer = 'SYSTEM'
key_name='backupkey'
user_name='system'
user_password='YourPassword1234'

h.unset_ini_parameter(
            param_list_unset,
            database, file_name, layer,
            reconfig=True,
            user_name=user_name, user_password=user_password)