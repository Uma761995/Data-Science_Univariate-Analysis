class univariate():
    def quanQual(dataset):
        qual=[]
        quan=[]
        for columnName in dataset.columns:
            if(dataset[columnName].dtype=='O'):
                #print("Qual")
                qual.append(columnName)     #append is to add into the list of columnname
            else:
               # print("Quan")
                quan.append(columnName)
        return quan,qual