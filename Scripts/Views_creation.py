import sqlite3 as sql
import pandas as pd
import Query_generation as QG

class DatabaseMethods:
    def __init__(self, dbName):
        self.dbName = dbName
    
    def connect_to_db(self):
        return sql.connect(self.dbName)
    
    def create_cursor(self, conn):
        return conn.cursor()
        
    def createDB(self):
        conn = self.connect_to_db()
        conn.commit()
        conn.close()
    
    def execute_query(self, query):
        conn = self.connect_to_db()
        cursor = self.create_cursor(conn)
        for row in cursor.execute(query):
            print(row)
        conn.close()
        
class TablesDefinition(DatabaseMethods):
    def __init__(self, dbName):
        DatabaseMethods.__init__(self, dbName)
    
    def __table_definition(self, df, tableName):
        sqlDatatypes = []
        datatypes = {
            'object':'text',
            'bool':'text',
            'int64':'integer',
            'float64':'numeric'
        }
        for i in df.dtypes:
            i = str(i)
            dtype = datatypes[i] if i in datatypes.keys() else 'numeric'
            sqlDatatypes.append(dtype)
            
        columnsDef = ''
        for col, dtype in zip(df.columns, sqlDatatypes):
            columnsDef += col + ' ' + dtype + ',\n'
        columnsDef =  columnsDef[:-2]
    
        return f""" DROP TABLE IF EXISTS {tableName};
                     CREATE TABLE {tableName}(
                         {columnsDef}
                    )
                """

    def create_and_fill_table(self, df, tableName):
        conn = self.connect_to_db()
        cursor = self.create_cursor(conn)
        cursor.executescript(self.__table_definition(df, tableName))
        df.to_sql(tableName, conn, if_exists='replace', index=False)
        conn.commit()
        conn.close()
    
class CreatingViews(DatabaseMethods):
    def __init__(self, dbName, outputPath):
        DatabaseMethods.__init__(self, dbName)
        self.outputPath = outputPath
    
    def __query_to_excel(self, query, outputFileName):
        conn = self.connect_to_db()
        df = pd.read_sql_query(query, conn)
        df.to_excel(outputFileName, index=False)
    
    def create_all_views(self, file):
        genQuery = QG.GenerateQuery(file)
        numberOfQueries = genQuery.number_of_queries()
        for i in range(1, numberOfQueries+1):
            outputFileName = f'{self.outputPath}query_{i}.xlsx'
            self.__query_to_excel(genQuery.get_query(i), outputFileName)
            print(f'File query_{i}.xlsx generated')
