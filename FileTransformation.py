# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 21:09:26 2019

@author: snagar
"""
import csv
from collections import defaultdict
import json
import pandas as pd 
with open("C:/Users/snagar/greenkeyinterview/calls-4.csv", 'r') as Filecsv:
    reader = csv.reader(Filecsv, delimiter=',')
    next(reader)
    my_list = list(reader)
dict_csv = {}

for i in my_list:
    values = i[1:5]
    key = i[0]
    if i[0] in dict_csv:
        dict_csv[i[0]].append(i[1:])
    else:
        value = list(i[1:])
        key = i[0]
        dict_csv.setdefault(key,[]).append(value)

mintime = {}
minvalue = {}
maxtime = {}
maxvalue ={}
for key, value in dict_csv.items():
    for item in value:
        if key in mintime:
            value=item[1]
            mintime[key].append(value) 
            maxval=item[2] 
            maxtime[key].append(maxval)
        else:
            mintime.setdefault(key, []).append(item[1])
            maxtime.setdefault(key, []).append(item[2])
            
        for key, value in mintime.items():
            print(min(set(mintime[key])))
            minval = min(set(mintime[key]))
            minvalue[key] = minval
        for key, value in maxtime.items():
            maxval = max(set(maxtime[key]))
            maxvalue[key] = maxval
        

list1 = list(maxvalue)
list2 = list(maxvalue.values())
list3 = list(minvalue.values())
dict_test = {}
item3 = {}     

for key in dict_csv.keys():
    item3[key] = dict_csv[key]
    dict_test[key]=item3
pd4 = list(dict_test.values())     

final_pd = pd.DataFrame({'call-id': list1,'start': list3,'end': list2, 'users':pd4 })
json_final = final_pd.to_json(orient='records')
text_file = open("Output.txt", "w")
text_file.write(json_final)
text_file.close()