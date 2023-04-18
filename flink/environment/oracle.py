'''By using this import we will get schema from table'''
from utils import utils


def get_data_from_json(user_input):
    '''this function will take data from json and return a input list
    param: dict user_input, contain config of the oracle.'''
    input_list=[]
    source = user_input['oracle']['source']
    flink_tbl = user_input['oracle']['flink_tbl']
    database = user_input['oracle']['database']
    table_name = user_input['oracle']['table_name']
    user = user_input['oracle']['user']
    password = user_input['oracle']['password']
    connector_type = user_input['oracle']['connector_type']
    host = user_input['oracle']['host']
    port = user_input['oracle']['port']
    driver = user_input["oracle"]["driver"]

    input_list=[source,flink_tbl,database,table_name,user,password,connector_type,host,port,driver]
    return input_list

def create_flink_table(input_list,tbl_env,table_schema):
    '''This function will create flink table
    param: list input_list, list that contain oracle config,
    param:env_obj tbl_env, this will help you to execute tables
    param: str table_schema, that contain column with datatype'''
    source_ddl = f"""
           create table {input_list[1]}({table_schema}
           ) WITH (
            'connector' = '{input_list[6]}',
            'url' = '{input_list[6]}:{input_list[0]}://{input_list[7]}:{input_list[8]}/{input_list[2]}',
            'username'='{input_list[4]}',
            'password' = '{input_list[5]}',
            'driver' = '{input_list[9]}'
            'table-name' = '{input_list[3]}')
        """
    print(source_ddl)
    r = tbl_env.execute_sql(source_ddl)

def start_ingestion(user_input,tbl_env):
    '''This function will start the ingestion
    param:dict user_input, that contain oracle config.
    param: env_obj tbl_env, this will help you to execute tables '''
    print("This is oracle")
    input_list=get_data_from_json(user_input)
    table_schema= utils.get_schema(user_input['oracle'])
    create_flink_table(input_list, tbl_env,table_schema)
