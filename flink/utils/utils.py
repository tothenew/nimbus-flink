import pymysql
import psycopg2
import cx_Oracle

def get_postgres_col_with_datatype(cursor,table):
    '''This function will return column name with datatype from specified db_table
    param:cursor, that help to connect with db
    param:str table, get data for table. '''
    cursor.execute(f"select column_name, data_type,character_maximum_length from INFORMATION_SCHEMA.COLUMNS where table_name ='{table}';")
    data=cursor.fetchall()
    col_with_datatype=' '
    for i in range(len(data)):
        if i != len(data)-1:
            col_with_datatype = col_with_datatype+'`'+data[i][0]+'` '+data[i][1]+','
        else:
            col_with_datatype = col_with_datatype+'`'+data[i][0]+'` '+data[i][1]

    col_with_datatype = col_with_datatype.replace('text', 'varchar(100)')
    return col_with_datatype


def get_mysql_col_with_datatype(cursor,table):
    '''This function will return column name with datatype from specified db_table
    param:cursor, that help to connect with db
    param:str table, get data for table. '''
    col_wtih_datatype=' '
    cursor.execute(f"describe {table}")
    data=cursor.fetchall()
    for i in range(len(data)):
        if i != len(data)-1:
            col_wtih_datatype = col_wtih_datatype+'`'+data[i][0]+'` '+data[i][1]+','
        else:
            col_wtih_datatype = col_wtih_datatype+'`'+data[i][0] + '` ' + data[i][1]

    col_wtih_datatype=col_wtih_datatype.replace('text','varchar(100)')
    return col_wtih_datatype


def get_schema(input_json):
    '''This function will return the schema from the table
     param: dict input_json, that have database related config.'''
    source = input_json.get('source')
    host = input_json.get('host')
    user = input_json.get('user')
    password = input_json.get('password')
    database = input_json.get('database')
    table_name = input_json.get('table_name')
    port = int(input_json.get('port'))

    if source == 'mysql':
        db = pymysql.connect(host = host,
                             user = user,
                             password = password,
                             database=database,
                             port=int(port)
                    )
        cursor = db.cursor()
        col_schema = get_mysql_col_with_datatype(cursor, table_name)
        return col_schema

    elif source == 'postgresql':
        postgres_con = psycopg2.connect(dbname=database,
                                        user=user,
                                        password=password,
                                        host=host, port=int(port))
        cursor = postgres_con.cursor()
        return get_postgres_col_with_datatype(cursor,table_name)
    elif source == 'oracle':
        print(host)
        dsn_tns = cx_Oracle.makedsn(host, port, database)
        print(dsn_tns)
        conn = cx_Oracle.connect(user=user, password=password, dsn=dsn_tns)
        cursor = conn.cursor()
    else:
        print("Invalid engine")




