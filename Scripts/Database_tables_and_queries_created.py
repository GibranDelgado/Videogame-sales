import pandas as pd
import sqlite3 as sql
from Getting_specific_query import number_of_queries, specific_query

def createDB(databaseName):
    conn = sql.connect(databaseName)
    conn.commit()
    conn.close()

def create_and_fill_table(databaseName, df, tableName):
    conn = sql.connect(databaseName)
    cursor = conn.cursor()
    cursor.executescript( """ DROP TABLE IF EXISTS vgsales; 
                             \nCREATE TABLE vgsales(
                             Rank INTEGER, Name TEXT, Platform TEXT, Year INTEGER, 
                             Genre TEXT, Pulisher TEXT, NA_Sales NUMERIC, EU_Sales NUMERIC, 
                             JP_Sales NUMERIC, Global_Sales NUMERIC) """ )

    df.to_sql(tableName, conn, if_exists='replace', index=False)
    conn.commit()
    conn.close()

def execute_query(databaseName, query):
    conn = sql.connect(databaseName)
    cursor = conn.cursor()

    for row in cursor.execute(query):
        print(row)
    print('')
    conn.close()

def creating_data(databaseName, file_name, output_path):
    def generate_df(databaseName, query, file_name):
        conn = sql.connect(databaseName)
        df = pd.read_sql_query(query, conn)
        df.to_excel(file_name, index=False)
    
    n = number_of_queries(file_name)
    for i in range(1, n+1):
        out_file_name = f'{output_path}Query_'
        out_file_name += f'{i}.xlsx'
        generate_df(databaseName, specific_query(file_name,i), out_file_name)