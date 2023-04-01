import pandas as pd
import numpy as np

df1 = pd.read_csv('dataset_generate/DataAnalyse_client.csv')
df2 = pd.read_csv('dataset_generate/DataAnalyse_collectdata.csv')

df = pd.concat([df1, df2])

df['cloths'] = df2['cloths'] 
df['underwear'] = df2['underwear'] 
df['sportswear'] = df2['sportswear'] 
df['accessories'] = df2['accessories'] 

df.to_csv('dataset_generate/concat_client_collect.csv', index=False)