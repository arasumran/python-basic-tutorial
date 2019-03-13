import pandas as pd
list_=[]
df = pd.read_csv('hebele.csv',index_col=None,header=0,sep='?')
list_.append(df)
frame= pd.concat(list_,axis=0,ignore_index=False)
frame.to_csv("ger.csv",sep=',',index=False)