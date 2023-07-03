'''Running the flink-ingestion Flow.'''

import logging
from pyflink.table import *
from pyflink.table import EnvironmentSettings, TableEnvironment
import json
import sys
import os
import importlib
# from environment import mysql,postgresql,s3

def main():
    '''environment configuration'''
    env_settings = EnvironmentSettings.new_instance().in_batch_mode().build()
    tbl_env = TableEnvironment.create(env_settings)
    print(tbl_env)
    return tbl_env

if __name__ == '__main__':
    get_input = sys.argv[1]
    user_input = json.load(open(get_input, 'r'))
    tbl_env = main()
    for source in user_input:
        for value in user_input[source]:
            FLAG = False
            if not user_input[source][value]:
                FLAG = True
                break
        if not FLAG:
            module_name = f'environment.{source}'
            module = importlib.import_module(module_name, 'environment')
            func = getattr(module, 'start_ingestion')
            func(user_input,tbl_env)
        if FLAG:
            logging.error(f"INVALID config.JSON FILE \n Enter value for {user_input}")


















