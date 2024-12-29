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