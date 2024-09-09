import pandas as pd
import sqlite3 as sql
from Getting_specific_query import specific_query, number_of_queries

def execute_query(databaseName, query):
    conn = sql.connect(databaseName)
    cursor = conn.cursor()

    for row in cursor.execute(query):
        print(row)
    print('')
    conn.close()

def generate_df(databaseName, query, file_name):
    conn = sql.connect(databaseName)
    df = pd.read_sql_query(query, conn)
    df.to_excel(file_name, index=False)

def creating_data(databaseName, file_name, output_path):
    n = number_of_queries(file_name)

    for i in range(1, n+1):
        out_file_name = f'{output_path}Query_'
        out_file_name += f'{i}.xlsx'
        generate_df(DB, specific_query(file_name,i), out_file_name)

if __name__ ==  '__main__':
    DB = 'VideoGame_Sales.db'
    path_file = 'C:\\Users\\Gibran\\Documents\\Videogame sales\\'
    output_path = 'C:\\Users\Gibran\\Documents\\Videogame sales\\Query_results\\'
    file_name = 'queries.txt'
    creating_data(DB, file_name, output_path)