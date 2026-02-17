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
   
    def Univariate(dataset,quan):
        import pandas as pd
        import numpy as np
        descriptive=pd.DataFrame(index=["mean","median","mode","Q1:25%","Q2:50%","Q3:75%","Q:99%","Q4:100%","IQR","1.5rule","Lesser","Greater","Max","Min"],columns=quan)
        for columnName in quan:
            descriptive.loc["mean",columnName]=dataset[columnName].mean()
            descriptive.loc["median",columnName]=dataset[columnName].median()
            descriptive.loc["mode",columnName]=dataset[columnName].mode()[0]
            descriptive.loc["Q1:25%",columnName]=dataset.describe()[columnName]["25%"]
            descriptive.loc["Q2:50%",columnName]=dataset.describe()[columnName]["50%"]
            descriptive.loc["Q3:75%",columnName]=dataset.describe()[columnName]["75%"] 
            descriptive.loc["Q:99%",columnName]=np.percentile(dataset[columnName],99)  
            descriptive.loc["Q4:100%",columnName]=dataset.describe()[columnName]["max"]
            descriptive.loc["IQR",columnName]=descriptive.loc["Q3:75%",columnName]-descriptive.loc["Q1:25%",columnName]
            descriptive.loc["1.5rule",columnName]=1.5*descriptive.loc["IQR",columnName]
            descriptive.loc["Lesser",columnName]=descriptive.loc["Q1:25%",columnName]-descriptive.loc["1.5rule",columnName]
            descriptive.loc["Greater",columnName]= descriptive.loc["Q3:75%",columnName]+descriptive.loc["1.5rule",columnName]
            descriptive.loc["Max",columnName]=dataset[columnName].max()
            descriptive.loc["Min",columnName]=dataset[columnName].min()
        return descriptive
    def findoutliers(x,quan):
        less=[]         
        great=[]
        for colName in quan:   
            if(x.loc["Min",colName]<x.loc["Lesser",colName]):
                less.append(colName)
            if(x.loc["Max",colName]>x.loc["Greater",colName]):
                great.append(colName)
        return less,great
    def repoutliers(dataset,descriptive,less,great):
        for column in less:
            dataset[column][dataset[column]<descriptive.loc["Lesser",column]]=descriptive.loc["Lesser",column]
        for column in great:
            dataset[column][dataset[column]>descriptive.loc["Greater",column]]=descriptive.loc["Greater",column]
        return dataset
    def frequency(columnName,dataset):
        import pandas as pd
        freqTable=pd.DataFrame(columns=["Unique_values","Frequency","Relative_frequency","Cumulative"])
        freqTable["Unique_values"]=dataset[columnName].value_counts().index
        freqTable["Frequency"]=dataset[columnName].value_counts().values
        freqTable["Relative_frequency"]=(freqTable["Frequency"]/103)
        freqTable["Cumulative"]=freqTable["Relative_frequency"].cumsum()
        return freqTable