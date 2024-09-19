import pandas as pd
import sys
import os

if __name__ ==  '__main__':
    path = os.path.dirname(os.path.abspath('main.py'))+'\\'
    sys.path.insert(0, os.path.join(os.path.dirname(sys.path[0]),f"{path}Scripts"))
    import Database_tables_and_queries_created as create
    
    output_path = f'{path}Query_results\\'
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    
    df = pd.read_csv(f'{path}Used_files\\vgsales.csv')
    file_name = f'{path}Used_files\\queries.txt'
    DB = f'{path}Used_files\\VideoGame_Sales.db'
    
    create.createDB(DB)
    create.create_and_fill_table(DB,df,'vgsales')
    create.creating_data(DB, file_name, output_path)