from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd

sc=StandardScaler()
df1=pd.read_csv('data/from_ics/raw_format/redwine.csv')
sc=StandardScaler()
df2=sc.fit_transform(df1)
np.savetxt("data/from_ics/raw_format/transformed.csv", df2, delimiter=",")


#df_transformed=sc.fit_transform(df1[[col for col in df1.columns if ]])

#df1.to_csv('data\from_ics\raw_format\redwineTransformed.csv',sep=',',index=False)