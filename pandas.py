#!/bin/python3
import pandas as pd

table= pd.read_csv('./car.csv')
print (table.head(7))
print (table.shape)
print(table.columns)
