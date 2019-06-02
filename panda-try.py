# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print("Hello")

import pandas as pd
s = pd.Series([3, -5, 7, 4],  index=['a',  'b',  'c',  'd'])
print(s)

data = {'Country': ['Belgium',  'India',  'Brazil'], 'Capital': ['Brussels',  'New Delhi',  'Brasilia'],'Population': [11190846, 1303171035, 207847528]}

print(data)

df = pd.DataFrame(data,columns=['Country',  'Capital',  'Population'])

print(df)

iris = pd.read_csv("D:\python\iris_sample.csv")

print(iris)

iris[1:10]


print(iris[1:10].rank())
iris.shape
iris.columns
iris.index
iris.info()
len(iris)
iris.shape[0]

iris.count()
iris.sum()
iris.cumsum()

iris.describe()

iris.mean()
iris.median()


sample = iris[1:6]


sample

sample.apply(lambda x:x*10)


sample.drop('species',axis=1)




