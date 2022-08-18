#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
This Module is temporary for pushing data into influxdb when AD xApp starts. It will depreciated in future, when data will be coming through KPIMON
"""

import pandas as pd
from influxdb import DataFrameClient
import datetime


# In[2]:


class INSERTDATA:
    print('//////////////enter INSERDATA class in inser////////////')

    def __init__(self):
        print('//////////enter def __init__/////////////////')
        host = 'ricplt-influxdb.ricplt'
        print('host=', host)
        #self.client = DataFrameClient(host, '8086', 'root', 'root')
        self.client = DataFrameClient(host, '8086')
        print('self.client=', self.client)
        #print('self.client.get_list_database()=', self.client.get_list_database())
        self.dropdb('UEData')
        print('self.dropdb(UEData)=', self.dropdb('UEData'))
        self.createdb('UEData')
        print('self.createdb(UEData)=', self.createdb('UEData'))

    def createdb(self, dbname):
        print('//////////enter def createdb////////////////////')
        print("Create database: " + dbname)
        self.client.create_database(dbname)
        print('self.client.create_database(dbname)=', self.client.create_database(dbname))
        print('self.client.get_list_database()=', self.client.get_list_database())
        self.client.switch_database(dbname)
        print('self.client.switch_database(dbname)=', self.client.switch_database(dbname))

    def dropdb(self, dbname):
        print('//////////enter def dropdb/////////////////////')
        print("DROP database: " + dbname)
        self.client.drop_database(dbname)

    def dropmeas(self, measname):
        print('//////////enter def dropmeas////////////////')
        print("DROP MEASUREMENT: " + measname)
        self.client.query('DROP MEASUREMENT '+measname)
        print('self.client.query(DROP MEASUREMENT +measname)=', self.client.query('DROP MEASUREMENT '+measname))


def explode(df):
    print('//////////enter def explode(df)://////////////////')
    print('df=', df)
    print('df.columns=', df.columns)
    for col in df.columns:
        print('col=', col)
        print('df.iloc[0][col]=', df.iloc[0][col])
          print('isinstance(df.iloc[0][col], list)=', isinstance(df.iloc[0][col], list))
        if isinstance(df.iloc[0][col], list) and col != 'neighbourCellList':
            df = df.explode(col)
            print('df=', df)
        d = df[col].apply(pd.Series)
        print('d=', d)
        if col in list(range(5)):
            d.columns = d.columns + '_' + str(col)
            print('d.columns =d.columns + _ + str(col)=', d.columns)
        elif 'nbCellRfReport_' in col:
            d.columns = d.columns + '_nb_' + col[-1]
            print('d.columns = d.columns + _nb_ + col[-1]=', d.columns)
        df[d.columns] = d
        print('df[d.columns] = d=', df[d.columns])
        df = df.drop(col, axis=1)
        print('df=', df)
    return df


def jsonToTable(df):
    print('//////////enter def jsonToTable(df)://////////////////')
    df.index = range(len(df))
    print('df.index = range(len(df))=', df.index)
    cols = [col for col in df.columns if isinstance(df.iloc[0][col], dict) or isinstance(df.iloc[0][col], list)]
    print('cols=', cols)
    if len(cols) == 0:
        return df
    for col in cols:
        print('col in cols:=', col)
        d = explode(pd.DataFrame(df[col], columns=[col]))
        print('d = explode(pd.DataFrame(df[col], columns=[col]))=', d)
        d = d.dropna(axis=1, how='all')
        print('d = d.dropna(axis=1, how=all)=', d)
        df = pd.concat([df, d], axis=1)
        print('df = pd.concat([df, d], axis=1)=', df)
        df = df.drop(col, axis=1).dropna()
        print('df = df.drop(col, axis=1).dropna()=', df)
        print('jsonToTable(df)=', jsonToTable(df))
    return jsonToTable(df)


def time(df):
    print('//////////enter def time(df):////////////////////')
    df.index = pd.date_range(start=datetime.datetime.now(), freq='10ms', periods=len(df))
    print('df.index =',df.index )
    df['measTimeStampRf'] = df['measTimeStampRf'].apply(lambda x: str(x))
    print('df['measTimeStampRf']=', df['measTimeStampRf'])
    print('df=', df)
    return df


def populatedb():
    print('//////////enter def populatedb():///////////////////')
    data = pd.read_csv('mr/cells.csv')
    print('data = pd.read_csv(mr/cells.csv)=', data)
    data = time(data)
    print('data = time(data)=', data)

    # inintiate connection and create database UEDATA
    db = INSERTDATA()
    print('db = INSERTDATA()=', db )
    db.client.write_points(data, 'valid')
    print('db.client.write_points(data, valid)=', db.client.write_points(data, 'valid'))
    del data

    df = pd.read_json('mr/ue.json.gz', lines=True)
    print('df = pd.read_json(mr/ue.json.gz)=', df)
    df = df[['ueMeasReport']].dropna()
    print('df = df[[ueMeasReport]].dropna()=', df)
    df = jsonToTable(df)
    print('df = jsonToTable(df)=', df)
    df = time(df)
    print('df = time(df)=', df)

    db.client.write_points(df, 'train', batch_size=500,  protocol='line')
    db.client.write_points(df, 'liveUE', batch_size=500, protocol='line')
    print('db.client.write_points=', db.client.write_points(df, 'train', batch_size=500,  protocol='line'))


# In[ ]:




