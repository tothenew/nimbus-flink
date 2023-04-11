'''By using this import we will get schema from table'''
from utils import utils


def get_data_from_json(user_input):
    '''this function will take data from json and return a input list
    param: dict user_input contain config of the hdfs.'''
    input_list=[]
    hdfs_connector_type=user_input['hdfs']['hdfs_connector_type']
    path=user_input['hdfs']['path']
    format=user_input['hdfs']['format']
    hdfs_tbl=user_input['hdfs']['hdfs_tbl']
    flink_tbl = user_input['hdfs']['flink_tbl']
    input_list=[hdfs_connector_type,path,format,hdfs_tbl,flink_tbl]
    return input_list

def create_hdfs_sync_table(tbl_env,input_list,table_schema):
    '''This function will create hdfs sync table
    param:env_obj tbl_env, this will help you to execute tables
    param: list input_list, list that contain hdfs config,
    param: str table_schema, that contain column with datatype'''
    hdfs_ddl=f'''create table {input_list[3]}(
     {table_schema}
     )
     WITH
     ( 'connector' = '{input_list[0]}',
     'path' = '{input_list[1]}',
     'format' = '{input_list[2]}'
      );
    '''
    table_status=tbl_env.execute_sql(hdfs_ddl)
    table_status.print()

def insert_data_into_hdfs(tbl_env,output_table,flink_table):
    '''This function will store the data into the hdfs file system
    param: env_obj tbl_env, this will help you to execute tables
    param: str output_table , this is the storage table name for output
    param: str flink_table, this is the flink table name.'''

    insert_ddl=f'''
    insert OVERWRITE {output_table} select * from {flink_table};
    '''
    table_status=tbl_env.execute_sql(insert_ddl)
    table_status.print()

def start_ingestion(user_input,tbl_env):
    '''This function will start the ingestion
    param:dict user_input, that contain hdfs config.
    param: env_obj tbl_env, this will help you to execute tables '''
    print("This is hdfs")
    input_list=get_data_from_json(user_input)
    print(list(user_input.keys())[0])
    table_schema = utils.get_schema(user_input[f'{list(user_input.keys())[0]}'])
    create_hdfs_sync_table(tbl_env, input_list,table_schema)
    insert_data_into_hdfs(tbl_env,input_list[3],input_list[4])