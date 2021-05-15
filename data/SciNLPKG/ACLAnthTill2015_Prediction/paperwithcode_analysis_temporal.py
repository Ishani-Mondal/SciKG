
f=open('paperwithcode.tsv')
content=f.read()

tasks=[]
for line in content.split("\n"):
    tasks.append(line.split("\t")[0].lower())

tasks_set=list(set(tasks))
print(tasks_set)

'''
import os, glob, pickle
os.chdir("/mnt/c/Users/D.MONDAL/Downloads/tdm-kg-new/tdm-kg/ACLAnthTill2015_Prediction")

names=[]
time_dict={}

for name in glob.glob('*'):
    if(name.startswith("A") or name.startswith("D") or name.startswith("E")
    or name.startswith("J") or name.startswith("N") or name.startswith("P") or name.startswith("S") or name.startswith("W")):
        #print(name)
        if(int(name[1:][0])>=6):
            names.append(int("19"+str(name[1:])))
            year="19"+str(name[1:])
            time_dict[year]=[]
            os.chdir("/mnt/c/Users/D.MONDAL/Downloads/tdm-kg-new/tdm-kg/ACLAnthTill2015_Prediction/"+str(name))
            #for f in glob.glob('*'):
                #print(f)
        else:
            names.append(int("20"+str(name[1:])))
            time_dict["20"+str(name[1:])]=[]

os.chdir("/mnt/c/Users/D.MONDAL/Downloads/tdm-kg-new/tdm-kg/ACLAnthTill2015_Prediction")

for name in glob.glob('*'):
    if(name.startswith("A") or name.startswith("D") or name.startswith("E")
    or name.startswith("J") or name.startswith("N") or name.startswith("P") or name.startswith("S") or name.startswith("W")):
        if(int(name[1:][0])>=6):
            names.append(int("19"+str(name[1:])))
            year="19"+str(name[1:])
            time_dict[year]=[]
            os.chdir("/mnt/c/Users/D.MONDAL/Downloads/tdm-kg-new/tdm-kg/ACLAnthTill2015_Prediction/"+str(name))
            for f in glob.glob('*'):
                time_dict["19"+str(name[1:])].append("/mnt/c/Users/D.MONDAL/Downloads/tdm-kg-new/tdm-kg/ACLAnthTill2015_Prediction/"+name+"/"+f)
        else:
            os.chdir("/mnt/c/Users/D.MONDAL/Downloads/tdm-kg-new/tdm-kg/ACLAnthTill2015_Prediction/"+str(name))
            names.append(int("20"+str(name[1:])))
            for f in glob.glob('*'):
                time_dict["20"+str(name[1:])].append("/mnt/c/Users/D.MONDAL/Downloads/tdm-kg-new/tdm-kg/ACLAnthTill2015_Prediction/"+name+"/"+f)



names.sort(reverse = True)
import collections
od = collections.OrderedDict(sorted(time_dict.items()))
i=1
for key, value in od.items():
    if(i%3==0):
        print("=============")
    print(key, len(value))
    i=i+1

print("+==================")

year_range=[]
s_yr=1979

for i in range(37):
    yr=1979+i
    year_range.append(str(yr))

print(year_range)

content_file={}
import json
import collections
for key, value in time_dict.items():
    #print(key) 
    time_tasks=[]
    time_datasets=[]
    time_metrics=[]
    for files in value:
        f=open(files)
        try:
            data = json.load(f)
            
            sentences=[]
            #print("==================")
            for sentence in data['abstractContent']:
                sentences.append(sentence['text'].lower())

            for sentence in data['introductionContent']:
                sentences.append(sentence['text'].lower())

            for sentence in data['datasetContent']:
                sentences.append(sentence['text'].lower())
            content_file[str(key)+"\t"+files.split("/")[-1]]="".join(sentences)
        except:
            pass

f.close()

os.chdir('/mnt/c/Users/D.MONDAL/Downloads/tdm-kg-new/tdm-kg/ACLAnthTill2015_Prediction/')
#f1=open('paperwithcode_task_year_frequency.txt','w')
tasks_set.remove('')
tasks_set.remove('task')

tasks_frequency={}

for task in tasks_set:
    tasks_frequency[task]={}

for key, value in content_file.items():
    for task in tasks_set:
        tasks_frequency[task][str(key.split("\t")[0])]=[]

for key, value in content_file.items():
    for task in tasks_set:
        if(task in value):
           tasks_frequency[task][str(key.split("\t")[0])].append('hello')

import pickle
with open('/mnt/c/Users/D.MONDAL/Downloads/tdm-kg-new/tdm-kg/ACLAnthTill2015_Prediction/tasks_frequency_paperwithcode.pickle', 'wb') as handle:
    pickle.dump(tasks_frequency, handle, protocol=pickle.HIGHEST_PROTOCOL)


import pickle

with open('tasks_frequency_paperwithcode.pickle', 'rb') as handle:
    tasks_frequency_paperwithcode = pickle.load(handle)

final_tasks=[]
for key, value in tasks_frequency_paperwithcode.items():
    print("=============")
    final_v={}
    totalv=[]
    for k, v in value.items():
        final_v[k]=len(v)
        totalv.append(len(v))
        #print(k, v)
    if(sum(totalv)>10):
        final_tasks.append(key)
        print(key, final_v)

print(len(final_tasks))

#######################################################################
import os, glob
year_range=[]

for i in range(4):
    yr=2016+i
    year_range.append(str(yr))

print(year_range)

os.chdir("/mnt/c/Users/D.MONDAL/Downloads/tdm-kg-new/tdm-kg/ACLAnth2016to2019_Prediction")
plots_tasks_year_after={}
names=[]
time_dict={}
for name in glob.glob('*'):
    if(name.startswith("A") or name.startswith("D") or name.startswith("E")
    or name.startswith("J") or name.startswith("N") or name.startswith("P") or name.startswith("S") or name.startswith("W")):
        if(int(name[1:][0])>=6):
            names.append(int("19"+str(name[1:])))
            year="19"+str(name[1:])
            time_dict[year]=[]
            os.chdir("/mnt/c/Users/D.MONDAL/Downloads/tdm-kg-new/tdm-kg/ACLAnth2016to2019_Prediction/"+str(name))
            #for f in glob.glob('*'):
                #print(f)
        else:
            names.append(int("20"+str(name[1:])))
            time_dict["20"+str(name[1:])]=[]

os.chdir("/mnt/c/Users/D.MONDAL/Downloads/tdm-kg-new/tdm-kg/ACLAnth2016to2019_Prediction")

for name in glob.glob('*'):
    if(name.startswith("A") or name.startswith("D") or name.startswith("E")
    or name.startswith("J") or name.startswith("N") or name.startswith("P") or name.startswith("S") or name.startswith("W")):
        if(int(name[1:][0])>=6):
            names.append(int("19"+str(name[1:])))
            year="19"+str(name[1:])
            time_dict[year]=[]
            os.chdir("/mnt/c/Users/D.MONDAL/Downloads/tdm-kg-new/tdm-kg/ACLAnth2016to2019_Prediction/"+str(name))
            for f in glob.glob('*'):
                time_dict["19"+str(name[1:])].append("/mnt/c/Users/D.MONDAL/Downloads/tdm-kg-new/tdm-kg/ACLAnth2016to2019_Prediction/"+name+"/"+f)
        else:
            os.chdir("/mnt/c/Users/D.MONDAL/Downloads/tdm-kg-new/tdm-kg/ACLAnth2016to2019_Prediction/"+str(name))
            names.append(int("20"+str(name[1:])))
            for f in glob.glob('*'):
                time_dict["20"+str(name[1:])].append("/mnt/c/Users/D.MONDAL/Downloads/tdm-kg-new/tdm-kg/ACLAnth2016to2019_Prediction/"+name+"/"+f)


content_file={}
import json
import collections
for key, value in time_dict.items():
    #print(key) 
    time_tasks=[]
    time_datasets=[]
    time_metrics=[]
    for files in value:
        f=open(files)
        try:
            data = json.load(f)
            
            sentences=[]
            #print("==================")
            for sentence in data['abstractContent']:
                sentences.append(sentence['text'].lower())

            for sentence in data['introductionContent']:
                sentences.append(sentence['text'].lower())

            for sentence in data['datasetContent']:
                sentences.append(sentence['text'].lower())
            content_file[str(key)+"\t"+files.split("/")[-1]]="".join(sentences)
        except:
            pass

f.close()

os.chdir('/mnt/c/Users/D.MONDAL/Downloads/tdm-kg-new/tdm-kg/ACLAnth2016to2019_Prediction/')
#f1=open('paperwithcode_task_year_frequency.txt','w')
tasks_set.remove('')
tasks_set.remove('task')

tasks_frequency={}

for task in tasks_set:
    tasks_frequency[task]={}

for key, value in content_file.items():
    for task in tasks_set:
        tasks_frequency[task][str(key.split("\t")[0])]=[]

for key, value in content_file.items():
    for task in tasks_set:
        if(task in value):
           tasks_frequency[task][str(key.split("\t")[0])].append('hello')

import pickle
with open('/mnt/c/Users/D.MONDAL/Downloads/tdm-kg-new/tdm-kg/ACLAnthTill2015_Prediction/tasks_frequency_paperwithcode_after2015.pickle', 'wb') as handle:
    pickle.dump(tasks_frequency, handle, protocol=pickle.HIGHEST_PROTOCOL)

'''
import pickle, os
os.chdir('/mnt/c/Users/D.MONDAL/Downloads/tdm-kg-new/tdm-kg/ACLAnthTill2015_Prediction/')

with open('tasks_frequency_paperwithcode.pickle', 'rb') as handle:
    tasks_frequency_paperwithcode = pickle.load(handle)

final_tasks_before_2015=[]
for key, value in tasks_frequency_paperwithcode.items():
    print("=============")
    final_v={}
    totalv=[]
    for k, v in value.items():
        final_v[k]=len(v)
        totalv.append(len(v))
        #print(k, v)
    if(sum(totalv)>10):
        final_tasks_before_2015.append(key)
        print(key, final_v)



import pickle

with open('tasks_frequency_paperwithcode_after2015.pickle', 'rb') as handle:
    tasks_frequency_paperwithcode_after = pickle.load(handle)

final_tasks_after_2015=[]
for key, value in tasks_frequency_paperwithcode_after.items():
    print("=============")
    final_v={}
    totalv=[]
    for k, v in value.items():
        final_v[k]=len(v)
        totalv.append(len(v))
        #print(k, v)
    if(sum(totalv)>10):
        final_tasks_after_2015.append(key)
        print(key, final_v)

final_dict={}
for key, value in tasks_frequency_paperwithcode_after.items():
    final_dict[key]={}
    for k, v in tasks_frequency_paperwithcode[key].items():
        #print(k, len(v))
        final_dict[key][k]=len(v)
    for k, v in value.items():
        #print(k, len(v))
        final_dict[key][k]=len(v)

print(final_dict['stance detection'])

import collections

for key, value in final_dict.items():
    total=[]
    #print(key)
    od = collections.OrderedDict(sorted(value.items()))
    i=1
    for k, v in od.items():
        #if(i%1==0):
        #print("=============")
        total.append(v)
        #print(k, v)
        i=i+1
    keys=list(od.keys())
    #print(keys)
    values=list(od.values())

    #print("================Reborn Tasks and Turning Points======================")
    for i in range(len(values)):
        if((values[i]-values[i-1])>10 and (values[i]-values[i-2])>10 and (values[i]-values[i-3])>10 and values[i-1]==0):
            print(keys[i], values[i], keys[i-1], values[i-1], keys[i-2], values[i-2], keys[i-3], values[i-3], key)

    
    #print("================Stable Tasks======================")
    #for i in range(len(values)):
        #if((values[i]-values[i-1])<10 and (values[i]-values[i-2])<10 and (values[i]-values[i-3])<10 and (values[i]-values[i-4])<10 and (values[i]-values[i-5])<10 and values[i]!=0):
            #print(keys[i], values[i], keys[i-1], values[i-1], keys[i-2], values[i-2], keys[i-3], values[i-3], key)
    


    

    

