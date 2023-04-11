'''By using this import we will get schema from table'''
from utils import utils


def get_data_from_json(user_input):
    '''this function will take data from json and return a input list
    param: dict ,user_input contain config of the postgresql.'''
    input_list = []
    source = user_input['postgresql']['source']
    flink_tbl = user_input['postgresql']['flink_tbl']
    database = user_input['postgresql']['database']
    table_name = user_input['postgresql']['table_name']
    user = user_input['postgresql']['user']
    password = user_input['postgresql']['password']
    connector_type = user_input['postgresql']['connector_type']
    host = user_input['postgresql']['host']
    port = user_input['postgresql']['port']
    input_list=[source,flink_tbl,database,table_name,user,password,connector_type,host,port]
    return input_list

def create_flink_table(input_list, tbl_env,table_schema):
    '''This function will create flink table
    param: list input_list, list that contain postgresql config,
    param:env_obj tbl_env, this will help you to execute tables
    param: str table_schema, that contain column with datatype'''
    input_table = f"""
           create table {input_list[1]}({table_schema}
           ) WITH (
            'connector' = '{input_list[6]}',
            'url' = '{input_list[6]}:{input_list[0]}://{input_list[7]}:{input_list[8]}/{input_list[2]}',
            'username'='{input_list[4]}',
            'password' = '{input_list[5]}',
            'table-name' = '{input_list[3]}' )
        """
    print(input_table)
    input_table = tbl_env.execute_sql(input_table)
    input_table.print()


def start_ingestion(user_input,tbl_env):
    '''This function will start the ingestion
    param:dict user_input, that contain postgresql config.
    param: env_obj tbl_env, this will help you to execute tables  '''
    input_list=get_data_from_json(user_input)
    table_schema= utils.get_schema(user_input['postgresql'])
    print(table_schema)
    create_flink_table(input_list, tbl_env,table_schema)
    print("Done")
