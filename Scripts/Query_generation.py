# import pandas as pd

# def number_of_queries(file_name):
#     queries = open(file_name).read().split('\n')
#     commentaries = list(filter(lambda x:x.startswith('--'), queries))
    
#     return len(commentaries)

# def specific_query(file_name, query_num):
#     queries = open(file_name).read().split('\n')
#     queries = list(filter(lambda x:len(x)!=0, queries))
#     queries = list(map(lambda x:x.replace('\t',''), queries))
#     queries = pd.DataFrame(queries, columns= ["rows"])
    
#     ind = queries[queries["rows"].str.slice(stop=2)=='--'].index
#     ind = pd.DataFrame(ind, columns=["positions"], index=range(1,len(ind)+1))
    
#     if query_num<len(ind):
#         specific_query = queries[ind.loc[query_num,"positions"]+1:ind.loc[query_num+1,"positions"]]
#     elif query_num==len(ind):
#         specific_query = queries[ind.loc[query_num,"positions"]+1:]
#     else:
#         raise ValueError('Invalid query number')
    
#     Result = ''
    
#     for i in specific_query.rows:
#         Result = Result + i + ' '
    
#     return Result


class GenerateQuery:
    def __init__(self, file):
        self.file = file
    
    def __split_txt_file(self):
        txtLines = open(self.file).read().split('\n')
        return list(filter(lambda x:len(x)!=0, txtLines))
    
    def __comments_index(self):
        txtLines = self.__split_txt_file()
        queriesIndex = []
        for i in range(len(txtLines)):
            if txtLines[i].startswith('--'):
                queriesIndex.append(i)
        return queriesIndex
    
    def number_of_queries(self):
        return len(self.__comments_index())
    
    def get_query(self, numQuery):
        totalQueries = self.number_of_queries()
        if numQuery <= 0 or numQuery > totalQueries:
            raise ValueError('Invalid query number')
        else:
            index = self.__comments_index()            
            txtLines = self.__split_txt_file()
            txtLines = list(map(lambda x:x.replace('\t', ''), txtLines))
            
            if numQuery < totalQueries:
                query = txtLines[index[numQuery-1]+1:index[numQuery]]
            else:
                query = txtLines[index[numQuery-1]+1:]
            
            return " ".join(query)