#'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import os


listFiles = []
filePath = r"C:\HDD Partitions\NIU\Sem 3\ISYE 570\Exercises\Exercise Code\.venv2"
for file in os.listdir(filePath):
    if file.endswith('.csv'):
        df = pd.read_csv(file)
        listFiles.append(df)


print(listFiles[0].info())
print(listFiles)
print(type(listFiles))

for i in listFiles:
    print(i.head(0))

listFiles[0].compare(listFiles[1])

for i,j in range(len(listFiles),2):
    if i.columns != j.columns:
        print('colnames are not similar')

#compare 37 times
a = 0
for j in range(1,len(listFiles)):
    if listFiles[0].columns.equals(listFiles[j].columns):
        print('colnames same')
        a = a+1
        print(a)
    else:
        print('not same')
        a = a+1
        print(a)

print(listFiles[-1].head())

#now check for col data types
a = 0
for j in range(1,len(listFiles)):
    if listFiles[0].dtypes.equals(listFiles[j].dtypes):
        print('dtype same')
        a = a+1
        print(a)
    else:
        print('not same')
        a = a+1
        print(a)

#for differing dtypes for df1,df3,df33 now finding exact column for each
#just change the df number in second expression
for i in listFiles[0].columns:
    if listFiles[0][i].dtype != listFiles[1][i].dtype:
        print(i)

#merging the df into a single df
df = pd.concat(listFiles, ignore_index=True)
print(df.info())
print(df.head())

#find null values
print(df.isnull().sum())

#delete null values
df1 = df.dropna()
print(df1.isnull())

df2 = df1.drop(columns=['ride_id','start_station_id','end_station_id'])
print(df2.head(2))

#change data types of columns
df['started_at'] = pd.to_datetime(df['started_at'])
df['ended_at'] = pd.to_datetime(df['ended_at'])
print(df.info())

df[['started_at']] = df[['started_at']].dt.floor('s')
df[['ended_at']] = df[['ended_at']].dt.floor('s')

df['started_at'] = df['started_at'].astype('datetime64[s]')
df['ended_at'] = df['ended_at'].astype('datetime64[s]')

df[['rideable_type','start_station_name', 'end_station_name']] = df[['rideable_type','start_station_name', 'end_station_name']].astype('str')
print(df.info())

#create time duration
df['ride_duration'] = df['ended_at'] - df['started_at']
df['ride_duration'] = df['ride_duration'].dt.total_seconds().apply(lambda x: str(pd.to_timedelta(x, unit='s')))
df.info()

#save the cleaned data to a file
df.to_csv('file.csv', index= False)

df = pd.read_csv(file)
print(df.info())

print(df.isnull().sum())

df = df.dropna()
print(df.isnull().sum())

print(df.nunique())

print(df['rideable_type'].value_counts())

print(df['member_casual'].value_counts())

print(df.info())

df1 = df

df1 = df1.drop(columns='ride_id')

print(df1.info())

df1['start_station_id'] = pd.to_numeric(df['start_station_id'], errors='coerce')
print(df1.info())
print(df1.isnull().sum())
df1.dropna()

df1['start_station_id'] = df1['start_station_id'].fillna(0)
df1['start_station_id'] = df1['start_station_id'].astype(int)

print(df1.info())

df1['end_station_id'] = pd.to_numeric(df['end_station_id'], errors='coerce')
print(df1.isnull().sum())

df1['start_lat'] = df1['start_lat'].round(4)
print(df1.info())
df1['start_lng'] = df1['start_lng'].round(4)
print(df1.info())
df1['end_lng'] = df1['end_lng'].round(4)
print(df1.info())
df1['end_lat'] = df1['end_lat'].round(4)
print(df1.info())

