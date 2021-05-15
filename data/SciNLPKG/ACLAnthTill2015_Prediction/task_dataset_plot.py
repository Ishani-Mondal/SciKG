import os, glob, pickle
os.chdir("/mnt/c/Users/D.MONDAL/Downloads/tdm-kg-new/tdm-kg/ACLAnthTill2015_Prediction")

with open('important_tasks.pickle', 'rb') as handle:
    important_tasks = pickle.load(handle)


with open('final_imp_datasets.pickle', 'rb') as handle:
    final_imp_datasets = pickle.load(handle)


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

print(content_file.keys())


tasks_dataset_frequency={}

for task in important_tasks.keys():
    for dataset in final_imp_datasets:
        tasks_dataset_frequency[task+"\t"+dataset]={}

for key, value in content_file.items():
    for task in important_tasks.keys():
        for dataset in final_imp_datasets:
            if(" "+task.lower()+" " in value and " "+dataset.lower()+" " in value):
                print(task, dataset, key)
                tasks_dataset_frequency[task+"\t"+dataset][str(key.split("\t")[0])]=[]

for key, value in content_file.items():
    for task in important_tasks.keys():
        for dataset in final_imp_datasets:
            if(" "+task.lower()+" " in value and " "+dataset.lower()+" " in value):
                print(task, dataset, key)
                tasks_dataset_frequency[task+"\t"+dataset][str(key.split("\t")[0])].append('hello')



for key, value in tasks_dataset_frequency.items():
    print("=============")
    final_v={}
    totalv=[]
    for k, v in value.items():
        final_v[k]=len(v)
        totalv.append(len(v))
        #print(k, v)
    if(sum(totalv)>10):
        #final_tasks_before_2015.append(key)
        print(key, final_v)