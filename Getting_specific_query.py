import pandas as pd

def number_of_queries(file_name):
    queries = open(file_name).read().split('\n')
    commentaries = list(filter(lambda x:x.startswith('--'), queries))
    
    return len(commentaries)

def specific_query(file_name, query_num):
    queries = open(file_name).read().split('\n')
    queries = list(filter(lambda x:len(x)!=0, queries))
    queries = list(map(lambda x:x.replace('\t',''), queries))
    queries = pd.DataFrame(queries, columns= ["rows"])
    
    ind = queries[queries["rows"].str.slice(stop=2)=='--'].index
    ind = pd.DataFrame(ind, columns=["positions"], index=range(1,len(ind)+1))
    
    if query_num<len(ind):
        specific_query = queries[ind.loc[query_num,"positions"]+1:ind.loc[query_num+1,"positions"]]
    elif query_num==len(ind):
        specific_query = queries[ind.loc[query_num,"positions"]+1:]
    else:
        raise ValueError('Invalid query number')
    
    Result = ''
    
    for i in specific_query.rows:
        Result = Result + i + ' '
    
    return Result