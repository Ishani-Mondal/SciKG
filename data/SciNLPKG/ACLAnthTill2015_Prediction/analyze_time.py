import os, glob, pickle
os.chdir("/mnt/c/Users/D.MONDAL/Downloads/tdm-kg-new/tdm-kg/ACLAnthTill2015_Prediction")

names=[]
time_dict={}
total_datasets=[]

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
                    if(ent['type']=='TASK' and ent['confidence']>0.6):
                        tasks.append(ent['text'].lower())
                    if(ent['type']=='DATASET' and ent['confidence']>0.6):
                        datasets.append(ent['text'].lower())
                        total_datasets.append()
                    if(ent['type']=='METRIC' and ent['confidence']>0.6):
                        metrics.append(ent['text'].lower())
            
            for elem in data['introductionContent']:
                for ent in elem['entities']:
                    if(ent['type']=='TASK' and ent['confidence']>0.6):
                        tasks.append(ent['text'].lower())
                    if(ent['type']=='DATASET' and ent['confidence']>0.6):
                        datasets.append(ent['text'].lower())
                    if(ent['type']=='METRIC' and ent['confidence']>0.6):
                        metrics.append(ent['text'].lower())
            '''
            for elem in data['datasetContent']:
                for ent in elem['entities']:
                    if(ent['type']=='TASK' and ent['confidence']>0.1):
                        tasks.append(ent['text'])
                    if(ent['type']=='DATASET' and ent['confidence']>0.75):
                        datasets.append(ent['text'])
                    if(ent['type']=='METRIC' and ent['confidence']>0.75):
                        metrics.append(ent['text'])
            '''
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
                    if(ent['type']=='TASK' and ent['confidence']>0.6):
                        tasks.append(ent['text'].lower())
                    if(ent['type']=='DATASET' and ent['confidence']>0.6):
                        datasets.append(ent['text'].lower())
                    if(ent['type']=='METRIC' and ent['confidence']>0.6):
                        metrics.append(ent['text'].lower())
            for elem in data['introductionContent']:
                for ent in elem['entities']:
                    if(ent['type']=='TASK' and ent['confidence']>0.6):
                        tasks.append(ent['text'].lower())
                    if(ent['type']=='DATASET' and ent['confidence']>0.6):
                        datasets.append(ent['text'].lower())
                    if(ent['type']=='METRIC' and ent['confidence']>0.6):
                        metrics.append(ent['text'].lower())
            #year_wise_sentences[key].append()
            #print("Tasks", tasks, "Datasets" , datasets, metrics)
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

print("##########################################################################################################")
print(plots_tasks_year_before['machine translation'])
f.close()

print("##########################################################################################################")
print(plots_tasks_year_before['word sense disambiguation'])
print("##########################################################################################################")
print(plots_tasks_year_before['sequence tagging'])
print("##########################################################################################################")
print(plots_tasks_year_before['entity linking'])

def Diff(li1, li2):
    return (list(list(set(li1)-set(li2)) + list(set(li2)-set(li1))))


keys=list(plots_tasks_year_before.keys())
print("=======================")
for task in keys:
    #if(task=='machine translation'):
    years=plots_tasks_year_before[task]
    #print(years)
    years_not_in_range=Diff(year_range, years)
    #print(years_not_in_range)
    for year in years_not_in_range:
        plots_tasks_year_before[task][year]=0
    #print("Updated")
    #print(plots_tasks_year_before['machine translation'])
    #if(elem not in year_range):
    #print(task, elem)

print("##########################################################################################################")
print(plots_tasks_year_before['machine translation'])
print("##########################################################################################################")

with open('/mnt/c/Users/D.MONDAL/Downloads/tdm-kg-new/tdm-kg/ACLAnthTill2015_Prediction/plots_tasks_year_before.pickle', 'wb') as handle:
    pickle.dump(plots_tasks_year_before, handle, protocol=pickle.HIGHEST_PROTOCOL)



##########################################################################################################

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
            
names.sort(reverse = True)
import json
import collections

#print(time_dict.keys())


for key, value in time_dict.items():
    print(key) 
    time_tasks=[]
    time_datasets=[]
    time_metrics=[]
    for files in value:
        f=open(files)
        #with open(files, 'r') as myfile:
        data=json.load(f)
        #obj = json.load(data)
        #print(data)
        try:
            tasks=[]
            datasets=[]
            metrics=[]
            for elem in data['abstractContent']:
                for ent in elem['entities']:
                    if(ent['type']=='TASK' and ent['confidence']>0.6):
                        tasks.append(ent['text'].lower())
                    if(ent['type']=='DATASET' and ent['confidence']>0.6):
                        datasets.append(ent['text'].lower())
                    if(ent['type']=='METRIC' and ent['confidence']>0.6):
                        metrics.append(ent['text'].lower())
            
            for elem in data['introductionContent']:
                for ent in elem['entities']:
                    if(ent['type']=='TASK' and ent['confidence']>0.6):
                        tasks.append(ent['text'].lower())
                    if(ent['type']=='DATASET' and ent['confidence']>0.6):
                        datasets.append(ent['text'].lower())
                    if(ent['type']=='METRIC' and ent['confidence']>0.6):
                        metrics.append(ent['text'].lower())
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
        for elem in counter.items():
            plots_tasks_year_after[elem[0]]={}



for key, value in time_dict.items():
    print(key) 
    time_tasks=[]
    time_datasets=[]
    time_metrics=[]
    for files in value:
        f = open(files)
        data = json.load(f)
        tasks=[]
        datasets=[]
        metrics=[]
        for elem in data['abstractContent']:
            for ent in elem['entities']:
                if(ent['type']=='TASK' and ent['confidence']>0.6):
                    tasks.append(ent['text'].lower())
                if(ent['type']=='DATASET' and ent['confidence']>0.6):
                    datasets.append(ent['text'].lower())
                if(ent['type']=='METRIC' and ent['confidence']>0.6):
                    metrics.append(ent['text'].lower())
        
        for elem in data['introductionContent']:
            for ent in elem['entities']:
                if(ent['type']=='TASK' and ent['confidence']>0.6):
                    tasks.append(ent['text'].lower())
                if(ent['type']=='DATASET' and ent['confidence']>0.6):
                    datasets.append(ent['text'].lower())
                if(ent['type']=='METRIC' and ent['confidence']>0.6):
                    metrics.append(ent['text'].lower())
        #print(tasks, datasets, metrics)
        for elem in tasks:
            time_tasks.append(elem)
        for elem in datasets:
            time_datasets.append(elem)
        for elem in metrics:
            time_metrics.append(elem)
    counter=collections.Counter(time_tasks)
    #for elem in counter.items():
        #for yr in year_range:
            #plots_tasks_year_after[elem[0]][yr]=0
    for elem in counter.items():
        plots_tasks_year_after[elem[0]][key]=elem[1]


keys=list(plots_tasks_year_after.keys())
print("=======================")
for task in keys:
    #if(task=='machine translation'):
    years=plots_tasks_year_after[task]
    #print(years)
    years_not_in_range=Diff(year_range, years)
    #print(years_not_in_range)
    for year in years_not_in_range:
        plots_tasks_year_after[task][year]=0

print(plots_tasks_year_after['machine translation'])
with open('/mnt/c/Users/D.MONDAL/Downloads/tdm-kg-new/tdm-kg/ACLAnthTill2015_Prediction/plots_tasks_year_after.pickle', 'wb') as handle:
    pickle.dump(plots_tasks_year_after, handle, protocol=pickle.HIGHEST_PROTOCOL)



def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

intersecting_tasks=intersection(list(plots_tasks_year_after.keys()), list(plots_tasks_year_before.keys()))

import editdistance, pickle

similar_tasks={}
for elem1 in intersecting_tasks:
    elems=[]
    for elem2 in intersecting_tasks:
        if(editdistance.eval(elem1, elem2)/max(len(elem1), len(elem2))<0.3):
            if(elem1!=elem2):
                elems.append(elem2)
    if(len(elems)>0):
        similar_tasks[elem1]=elems


with open('/mnt/c/Users/D.MONDAL/Downloads/tdm-kg-new/tdm-kg/ACLAnthTill2015_Prediction/similar_tasks.pickle', 'wb') as handle:
    pickle.dump(similar_tasks, handle, protocol=pickle.HIGHEST_PROTOCOL)
