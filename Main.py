import pandas as pd
import sys
import os

def set_config(main_script, scriptsFolder):
    mainPath = os.path.dirname(os.path.abspath(main_script))+'\\'
    sys.path.insert(0, os.path.join(os.path.dirname(sys.path[0]), f"{mainPath}{scriptsFolder}"))
    
    outPath = f'{mainPath}Queries_results\\'
    if not os.path.exists(outPath):
        os.makedirs(outPath)
    
    return mainPath, outPath

if __name__ ==  '__main__':
    mainPath, outPath = set_config(main_script='Main.py', scriptsFolder='Scripts')
    usedFilesPath = f'{mainPath}Used_files\\'
    
    database = f'{usedFilesPath}VideoGame_Sales.db'
    queries = f'{usedFilesPath}queries.txt'
    
    import Views_creation as VC
    
    dbMethods = VC.DatabaseMethods(database)
    dbMethods.createDB()
    
    df = pd.read_csv(f'{mainPath}Used_files\\vgsales.csv')
    file_name = f'{mainPath}Used_files\\queries.txt'
    
    table = VC.TablesDefinition(database)
    table.create_and_fill_table(df, 'vgsales')
    
    views = VC.CreatingViews(database, outPath)
    views.create_all_views(queries)