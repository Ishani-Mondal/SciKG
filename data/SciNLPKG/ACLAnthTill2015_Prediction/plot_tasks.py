import os, glob, pickle
os.chdir("/mnt/c/Users/D.MONDAL/Downloads/tdm-kg-new/tdm-kg/ACLAnthTill2015_Prediction")

with open('important_tasks.pickle', 'rb') as handle:
    important_tasks = pickle.load(handle)
'''
with open('plots_tasks_year_after.pickle', 'rb') as handle:
    plots_tasks_year_after = pickle.load(handle)

with open('plots_tasks_year_before.pickle', 'rb') as handle:
    plots_tasks_year_before = pickle.load(handle)


final_dict={}
year_range=[]
year_range2=[]

for i in range(37):
    yr=1979+i
    year_range.append(str(yr))

#print(year_range)


for i in range(4):
    yr=2016+i
    year_range2.append(str(yr))

print(year_range, year_range2)

year_wide_dict={}

for key, values in similar_tasks.items():
    year_wide_dict[key]={}

for key, values in similar_tasks.items():
    for year in year_range:
        year_wide_dict[key][year]=[]
    for year in year_range2:
        year_wide_dict[key][year]=[]

    for k, v in plots_tasks_year_before[key].items():
        year_wide_dict[key][k].append(v)

    for k, v in plots_tasks_year_after[key].items():
        year_wide_dict[key][k].append(v)
        
    #print(key, plots_tasks_year_before[key], plots_tasks_year_after[key])
    #print("===============================")
    for value in values:
        #print(value, plots_tasks_year_before[value], plots_tasks_year_after[value])
        for k, v in plots_tasks_year_before[value].items():
            year_wide_dict[key][k].append(v)

        for k, v in plots_tasks_year_after[value].items():
            year_wide_dict[key][k].append(v)
        
print("===============================")
final_dict={}
for k, values in year_wide_dict.items():
    for k1, v1 in values.items():
        count1=sum(year_wide_dict[k][k1])
        final_dict[k]={}

#print(year_wide_dict['Rule-Based Machine Translation (RBMT)']) 

for k, values in year_wide_dict.items():
    i=0
    for k1, v1 in values.items():
        count1=sum(year_wide_dict[k][k1])
        if(i%2==0):
            final_dict[k][k1[2:]]=count1
            i=i+1
        else:
            i=i+1

#print(final_dict.keys())

import editdistance
related_tasks={}

for key, value in final_dict.items():
    for key1, value1 in final_dict.items():
        if(key1!=key):
            if(editdistance.eval(key, key1)/max(len(key1), len(key))<0.3):
                related_tasks[key]=[]

for key, value in final_dict.items():
    for key1, value1 in final_dict.items():
        if(key1!=key):
            if(editdistance.eval(key, key1)/max(len(key1), len(key))<0.3):
                related_tasks[key].append(key1)

#print(related_tasks)

new_final_dict={}
for key, values in related_tasks.items():
    #print("================")
    #print(key)
    new_final_dict[key]={}
    #print("================")
    year_elem={}
    for val in values:
        for key1, val1 in final_dict[val].items():
            #print(key1, val1)
            year_elem[key1]=[]

    for val in values:
        for key1, val1 in final_dict[val].items():
            #print(key1, val1)
            year_elem[key1].append(val1)
    for key1, val1 in final_dict[key].items():
            #print(key1, val1)
        year_elem[key1].append(val1)

    for k, v in year_elem.items():
        new_final_dict[key][k]=sum(v)

import numpy as np
import matplotlib.pyplot as plt
# X-axis values



important_tasks={}

for key, values in new_final_dict.items():
    sumval=[]
    for k, v in values.items():
        sumval.append(v)
    if(sum(sumval)>70):
        important_tasks[key]=values

        #print(key, values)

print(important_tasks)

import pickle
with open('/mnt/c/Users/D.MONDAL/Downloads/tdm-kg-new/tdm-kg/ACLAnthTill2015_Prediction/important_tasks.pickle', 'wb') as handle:
    pickle.dump(important_tasks, handle, protocol=pickle.HIGHEST_PROTOCOL)

'''


for key, values in important_tasks.items():
    #print(key)
    keys=list(values.keys())
    for i in range(len(keys)):
        if(values[keys[i]]-values[keys[i-1]]>20 and values[keys[i]]-values[keys[i-2]]>20 and values[keys[i]]-values[keys[i-3]]>20 and values[keys[i-1]]==0):
            print(key, keys[i], values[keys[i]], keys[i-1], values[keys[i-1]])

#print(important_tasks['information summarization'])

'''
x = important_tasks['machine translation'].keys()
  
# Y-axis values 
y = important_tasks['machine translation'].values()
y5 = important_tasks['coreference resolution'].values()
#y1 = important_tasks['natural language inference (nli)'].values()
#y2 = important_tasks['textual entailment (te)'].values()

y3 = important_tasks['transfer learning'].values()
#y4 = final_dict['Aspect Based Sentiment Analysis'].values()
# Function to plot  
plt.plot(x, y, label='machine translation')
plt.plot(x, y5, label='coreference resolution')
#plt.plot(x, y1, label='NLI')
#plt.plot(x, y2, label='textual entailment (te)')
plt.plot(x, y3, label='transfer learning')
#plt.plot(x, y4, label='Aspect Based Sentiment Analysis (ABSA)')
# Function add a legend  
plt.legend(ncol=1)
  
# function to show the plot
plt.savefig('plt.png')


for key, value in new_final_dict.items():
    print("==============")
    print(key)
    print("==============")
    for k, v in value.items():
        print(k, v)
'''