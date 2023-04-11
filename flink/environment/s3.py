'''By using this import we will get schema from table'''
from utils import utils

def get_data_from_json(user_input):
    '''this function will take data from json and return a input list
    param: dict ,user_input contain config of the s3.'''
    input_list=[]
    s3_connector_type=user_input['s3']['s3_connector_type']
    path=user_input['s3']['path']
    format=user_input['s3']['format']
    s3_tbl=user_input['s3']['s3_tbl']
    flink_tbl = user_input['s3']['flink_tbl']

    input_list=[s3_connector_type,path,format,s3_tbl,flink_tbl]
    return input_list

def create_s3_sync_table(tbl_env,input_list,table_schema):
    '''This function will create s3 sync table
    param:env_obj tbl_env, this will help you to execute tables
    param: list input_list, list that contain s3 config,
    param: str table_schema, that contain column with datatype'''

    s3_ddl=f'''create table {input_list[3]}(
     {table_schema}
     )
     WITH
     ( 'connector' = '{input_list[0]}',
     'path' = '{input_list[1]}',
     'format' = '{input_list[2]}'
      );
    '''
    table_status=tbl_env.execute_sql(s3_ddl)
    table_status.print()

def insert_data_into_s3(tbl_env,output_table,flink_table):
    '''This function will store the data into the s3 location
    param: env_obj tbl_env, this will help you to execute tables
    param: str output_table , this is the storage table name for output
    param: str flink_table, this is the flink table name.'''
    insert_ddl=f'''
    insert OVERWRITE {output_table}  select * from {flink_table};
    '''
    table_status=tbl_env.execute_sql(insert_ddl)
    table_status.print()

def start_ingestion(user_input,tbl_env):
    '''This function will start the ingestion
    param:dict user_input, that contain s3 config.
    param: env_obj tbl_env, this will help you to execute tables '''
    print("This is s3")
    input_list=get_data_from_json(user_input)
    print(list(user_input.keys())[0])
    table_schema = utils.get_schema(user_input[f'{list(user_input.keys())[0]}'])
    create_s3_sync_table(tbl_env, input_list,table_schema)
    insert_data_into_s3(tbl_env,input_list[3],input_list[4])
