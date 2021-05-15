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

import collections
od = collections.OrderedDict(sorted(time_dict.items()))
i=1
for key, value in od.items():
    if(i%4==0):
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


plots_tasks_year_before={}
plots_datasets_year_before={}
plots_metrics_year_before={}

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
                    if(ent['type']=='TASK' and ent['confidence']>0.7):
                        tasks.append(ent['text'])
                    if(ent['type']=='DATASET' and ent['confidence']>0.7):
                        datasets.append(ent['text'])
                    if(ent['type']=='METRIC' and ent['confidence']>0.7):
                        metrics.append(ent['text'])
        except:
            pass

        #print(tasks, datasets, metrics)
        for elem in tasks:
            time_tasks.append(elem)
        for elem in datasets:
            time_datasets.append(elem)
        for elem in metrics:
            time_metrics.append(elem)
    counter=collections.Counter(time_tasks)
    #print(counter.most_common(20))
    
    for elem in counter.items():
        plots_tasks_year_before[elem[0]]={}

f.close()


year_wise_sentences={}

import json
#print(plots_tasks_year_before.keys())
for key, value in time_dict.items():
    
    time_tasks=[]
    time_datasets=[]
    time_metrics=[]
    for files in value:
        try:
            f = open(files)
            data = json.load(f)
            #print("data", data)
            tasks=[]
            datasets=[]
            metrics=[]
            for elem in data['abstractContent']:
                for ent in elem['entities']:
                    if(ent['type']=='TASK' and ent['confidence']>0.1):
                        tasks.append(ent['text'])
                    if(ent['type']=='DATASET' and ent['confidence']>0.75):
                        datasets.append(ent['text'])
                    if(ent['type']=='METRIC' and ent['confidence']>0.75):
                        metrics.append(ent['text'])
            for elem in data['introductionContent']:
                for ent in elem['entities']:
                    if(ent['type']=='TASK' and ent['confidence']>0.1):
                        tasks.append(ent['text'])
                    if(ent['type']=='DATASET' and ent['confidence']>0.75):
                        datasets.append(ent['text'])
                    if(ent['type']=='METRIC' and ent['confidence']>0.75):
                        metrics.append(ent['text'])
            for elem in data['datasetContent']:
                for ent in elem['entities']:
                    if(ent['type']=='TASK' and ent['confidence']>0.1):
                        tasks.append(ent['text'])
                    if(ent['type']=='DATASET' and ent['confidence']>0.75):
                        datasets.append(ent['text'])
                    if(ent['type']=='METRIC' and ent['confidence']>0.75):
                        metrics.append(ent['text'])
            
            year_wise_sentences[key].append()
            #print(tasks, datasets, metrics)
            for elem in tasks:
                time_tasks.append(elem)
            for elem in datasets:
                time_datasets.append(elem)
            for elem in metrics:
                time_metrics.append(elem)
        except:
            pass
    counter=collections.Counter(time_tasks)
    #print(time_tasks)
    for elem in counter.items():
        #print(elem)
        plots_tasks_year_before[elem[0]][key]=elem[1]


f.close()

print(plots_tasks_year_before)