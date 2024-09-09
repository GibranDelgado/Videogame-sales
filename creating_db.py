import pandas as pd
import sqlite3 as sql

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

if __name__ ==  '__main__':
    path_file = 'C:\\Users\\Gibran\\Documents\\Videogame sales\\'
    df = pd.read_csv(f'{path_file}vgsales.csv')
    DB = 'VideoGame_Sales.db' 
    createDB(DB)
    create_and_fill_table(DB,df,'vgsales')