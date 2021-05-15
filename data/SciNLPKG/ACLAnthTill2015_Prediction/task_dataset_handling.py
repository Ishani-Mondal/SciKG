import os, glob, pickle
os.chdir("/mnt/c/Users/D.MONDAL/Downloads/tdm-kg-new/tdm-kg/ACLAnthTill2015_Prediction")

with open('important_tasks.pickle', 'rb') as handle:
    important_tasks = pickle.load(handle)

'''
for key, values in important_tasks.items():
    #print(key)
    keys=list(values.keys())
    for i in range(len(keys)):
        if(values[keys[i]]-values[keys[i-1]]>20 and values[keys[i]]-values[keys[i-2]]>20 and values[keys[i]]-values[keys[i-3]]>20 and values[keys[i-1]]==0):
            print(key, keys[i], values[keys[i]], keys[i-1], values[keys[i-1]])

####################################################################################################

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
            


year_range=[]
s_yr=1979

for i in range(37):
    yr=1979+i
    year_range.append(str(yr))

total_datasets=[]

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
            #print(data)
            tasks=[]
            datasets=[]
            metrics=[]
            for elem in data['abstractContent']:
                for ent in elem['entities']:
                    if(ent['type']=='DATASET' and ent['confidence']>0.5):
                        total_datasets.append(ent['text'])
                    if(ent['type']=='TASK' and ent['confidence']>0.6):
                        tasks.append(ent['text'].lower())
                    if(ent['type']=='DATASET' and ent['confidence']>0.6):
                        datasets.append(ent['text'].lower())
                        total_datasets.append()
                    if(ent['type']=='METRIC' and ent['confidence']>0.6):
                        metrics.append(ent['text'].lower())
            
            for elem in data['introductionContent']:
                
                for ent in elem['entities']:
                    if(ent['type']=='DATASET' and ent['confidence']>0.5):
                        total_datasets.append(ent['text'])
                    if(ent['type']=='TASK' and ent['confidence']>0.6):
                        tasks.append(ent['text'].lower())
                    if(ent['type']=='DATASET' and ent['confidence']>0.6):
                        datasets.append(ent['text'].lower())
                    if(ent['type']=='METRIC' and ent['confidence']>0.6):
                        metrics.append(ent['text'].lower())
            
            for elem in data['datasetContent']:
                
                for ent in elem['entities']:
                    if(ent['type']=='DATASET' and ent['confidence']>0.5):
                        total_datasets.append(ent['text'])
                    if(ent['type']=='TASK' and ent['confidence']>0.1):
                        tasks.append(ent['text'])
                    if(ent['type']=='DATASET' and ent['confidence']>0.75):
                        datasets.append(ent['text'])
                    if(ent['type']=='METRIC' and ent['confidence']>0.75):
                        metrics.append(ent['text'])
            
        except:
            pass

f.close()


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
            #print(data)
            tasks=[]
            datasets=[]
            metrics=[]
            for elem in data['abstractContent']:
                for ent in elem['entities']:
                    if(ent['type']=='DATASET' and ent['confidence']>0.5):
                        total_datasets.append(ent['text'])
                    if(ent['type']=='TASK' and ent['confidence']>0.6):
                        tasks.append(ent['text'].lower())
                    if(ent['type']=='DATASET' and ent['confidence']>0.6):
                        datasets.append(ent['text'].lower())
                        total_datasets.append()
                    if(ent['type']=='METRIC' and ent['confidence']>0.6):
                        metrics.append(ent['text'].lower())
            
            for elem in data['introductionContent']:
                
                for ent in elem['entities']:
                    if(ent['type']=='DATASET' and ent['confidence']>0.5):
                        total_datasets.append(ent['text'])
                    if(ent['type']=='TASK' and ent['confidence']>0.6):
                        tasks.append(ent['text'].lower())
                    if(ent['type']=='DATASET' and ent['confidence']>0.6):
                        datasets.append(ent['text'].lower())
                    if(ent['type']=='METRIC' and ent['confidence']>0.6):
                        metrics.append(ent['text'].lower())
            
            for elem in data['datasetContent']:
                
                for ent in elem['entities']:
                    if(ent['type']=='DATASET' and ent['confidence']>0.5):
                        total_datasets.append(ent['text'])
                    if(ent['type']=='TASK' and ent['confidence']>0.1):
                        tasks.append(ent['text'])
                    if(ent['type']=='DATASET' and ent['confidence']>0.75):
                        datasets.append(ent['text'])
                    if(ent['type']=='METRIC' and ent['confidence']>0.75):
                        metrics.append(ent['text'])
            
        except:
            pass

f.close()

final_imp_datasets=[]
for item in list(set(total_datasets)):
    if(total_datasets.count(item)>20):
        final_imp_datasets.append(item)
        #print(item,total_datasets.count(item))

os.chdir("/mnt/c/Users/D.MONDAL/Downloads/tdm-kg-new/tdm-kg/ACLAnthTill2015_Prediction")
f1=open('paperwithcode.tsv')
content1=f1.read()

for line in content1.split("\n"):
    try:
        final_imp_datasets.append(line.split("\t")[1])
    except:
        pass   #total_datasets.append()

import pickle
with open('/mnt/c/Users/D.MONDAL/Downloads/tdm-kg-new/tdm-kg/ACLAnthTill2015_Prediction/final_imp_datasets.pickle', 'wb') as handle:
    pickle.dump(list(set(final_imp_datasets)), handle, protocol=pickle.HIGHEST_PROTOCOL)

'''