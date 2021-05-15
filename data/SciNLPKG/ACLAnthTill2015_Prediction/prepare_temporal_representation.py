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
    if(i%4==0):
        pass
        #print("=============")
    #print(key, len(value))
    i=i+1

#print("+==================")

year_range=[]
s_yr=1979

for i in range(37):
    yr=1979+i
    year_range.append(str(yr))

#print(year_range)

dictionary_yearwise={}
total_datasets=[]
total_tasks=[]
total_metrics=[]

import json
import collections
for key, value in time_dict.items():
    dictionary_yearwise[key]=[]
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
            sentences=" "
            for elem in data['abstractContent']:
                for ent in elem['entities']:
                    if(ent['confidence']>0.85):
                        sentences=sentences+" "+"_".join(ent['text'].split())
                    if(ent['type']=='TASK' and ent['confidence']>0.75):
                        tasks.append(ent['text'].lower())
                    if(ent['type']=='DATASET' and ent['confidence']>0.75):
                        datasets.append(ent['text'].lower())
                    if(ent['type']=='METRIC' and ent['confidence']>0.75):
                        metrics.append(ent['text'].lower())
            for elem in data['introductionContent']:
                for ent in elem['entities']:
                    if(ent['confidence']>0.85):
                        sentences=sentences+" "+"_".join(ent['text'].split())
                    if(ent['type']=='TASK' and ent['confidence']>0.75):
                        tasks.append(ent['text'].lower())
                    if(ent['type']=='DATASET' and ent['confidence']>0.75):
                        datasets.append(ent['text'].lower())
                    if(ent['type']=='METRIC' and ent['confidence']>0.75):
                        metrics.append(ent['text'].lower())
            for elem in data['datasetContent']:
                for ent in elem['entities']:
                    if(ent['confidence']>0.85):
                        sentences=sentences+" "+"_".join(ent['text'].split())
                    if(ent['type']=='TASK' and ent['confidence']>0.75):
                        tasks.append(ent['text'].lower())
                    if(ent['type']=='DATASET' and ent['confidence']>0.75):
                        datasets.append(ent['text'].lower())
                    if(ent['type']=='METRIC' and ent['confidence']>0.75):
                        metrics.append(ent['text'].lower())
        except:
            pass
        #print(tasks, datasets, metrics)
        sentences2=[]
        for task in tasks:
            total_tasks.append("_".join(task.split()))
            sentences2.append("_".join(task.split()))
        for dataset in datasets:
            total_datasets.append("_".join(dataset.split()))
            sentences2.append("_".join(dataset.split()))
        for metric in metrics:
            total_metrics.append("_".join(metric.split()))
            sentences2.append("_".join(metric.split()))
        
        dictionary_yearwise[key].append(sentences.split())

f.close()
#print(dictionary_yearwise['2012'])

final_sent_dict={}
for year, sentences in dictionary_yearwise.items():
    #print(year)
    sentences1=" "
    for elem in sentences:
        sentences1=sentences1+" ".join(elem)
    final_sent_dict[year]=sentences1

#print(dictionary_yearwise['2000'])

from gensim.models import Word2Vec
for key, sentences1 in dictionary_yearwise.items():
    model = Word2Vec(sentences=sentences1, vector_size=200, window=5, min_count=1, workers=4)
    model.save("/mnt/c/Users/D.MONDAL/Downloads/tdm-kg-new/tdm-kg/ACLAnthTill2015_Prediction/w2v_models/word2vec.model"+"_"+str(key))



########################################################################################################################

import os, glob, pickle
os.chdir("/mnt/c/Users/D.MONDAL/Downloads/tdm-kg-new/tdm-kg/ACLAnth2016to2019_Prediction")

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
import collections
od = collections.OrderedDict(sorted(time_dict.items()))
i=1
for key, value in od.items():
    if(i%4==0):
        pass
        #print("=============")
    #print(key, len(value))
    i=i+1

#print("+==================")

year_range=[]
s_yr=2016

for i in range(4):
    yr=2016+i
    year_range.append(str(yr))

#print(year_range)

dictionary_yearwise={}
total_datasets=[]
total_tasks=[]
total_metrics=[]

import json
import collections
for key, value in time_dict.items():
    dictionary_yearwise[key]=[]
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
            sentences=" "
            for elem in data['abstractContent']:
                for ent in elem['entities']:
                    if(ent['confidence']>0.75):
                        sentences=sentences+" "+"_".join(ent['text'].split())

                    if(ent['type']=='TASK' and ent['confidence']>0.75):
                        tasks.append(ent['text'].lower())
                        
                    if(ent['type']=='DATASET' and ent['confidence']>0.75):
                        datasets.append(ent['text'].lower())
                        #sentences=sentences+" "+"_".join(ent['text'].lower().split())
                    if(ent['type']=='METRIC' and ent['confidence']>0.75):
                        metrics.append(ent['text'].lower())
                        #sentences=sentences+" "+"_".join(ent['text'].lower().split())
            for elem in data['introductionContent']:
                for ent in elem['entities']:
                    if(ent['confidence']>0.75):
                        sentences=sentences+" "+"_".join(ent['text'].split())
                    if(ent['type']=='TASK' and ent['confidence']>0.75):
                        tasks.append(ent['text'].lower())
                        #sentences=sentences+" "+"_".join(ent['text'].lower().split())
                    if(ent['type']=='DATASET' and ent['confidence']>0.75):
                        datasets.append(ent['text'].lower())
                        #sentences=sentences+" "+"_".join(ent['text'].lower().split())
                    if(ent['type']=='METRIC' and ent['confidence']>0.75):
                        metrics.append(ent['text'].lower())
                        #sentences=sentences+" "+"_".join(ent['text'].lower().split())
            for elem in data['datasetContent']:
                for ent in elem['entities']:
                    if(ent['confidence']>0.75):
                        sentences=sentences+" "+"_".join(ent['text'].split())
                    if(ent['type']=='TASK' and ent['confidence']>0.75):
                        tasks.append(ent['text'].lower())
                        #sentences=sentences+" "+"_".join(ent['text'].lower().split())
                    if(ent['type']=='DATASET' and ent['confidence']>0.75):
                        datasets.append(ent['text'].lower())
                        #sentences=sentences+" "+"_".join(ent['text'].lower().split())
                    if(ent['type']=='METRIC' and ent['confidence']>0.75):
                        metrics.append(ent['text'].lower())
                        #sentences=sentences+" "+"_".join(ent['text'].lower().split())
        except:
            pass
        #print(sentences.split())
        sentences2=[]
        for task in tasks:
            total_tasks.append("_".join(task.split()))
            sentences2.append("_".join(task.split()))
        for dataset in datasets:
            total_datasets.append("_".join(dataset.split()))
            sentences2.append("_".join(dataset.split()))
        for metric in metrics:
            total_metrics.append("_".join(metric.split()))
            sentences2.append("_".join(metric.split()))
        
        #print(key, files.split("/")[-1], sentences.split())

        dictionary_yearwise[key].append(sentences.split())

f.close()
#print(dictionary_yearwise['2018'])



final_sent_dict={}
for year, sentences in dictionary_yearwise.items():
    #print(year)
    sentences1=""
    for elem in sentences:
        sentences1=sentences1+" ".join(elem)
    final_sent_dict[year]=sentences1


from gensim.models import Word2Vec
for key, sentences1 in dictionary_yearwise.items():
    model = Word2Vec(sentences=sentences1, vector_size=200, window=5, min_count=1, workers=4)
    model.save("/mnt/c/Users/D.MONDAL/Downloads/tdm-kg-new/tdm-kg/ACLAnthTill2015_Prediction/w2v_models/word2vec.model"+"_"+str(key))

os.chdir("/mnt/c/Users/D.MONDAL/Downloads/tdm-kg-new/tdm-kg/ACLAnthTill2015_Prediction/w2v_models/")
model = Word2Vec.load("word2vec.model_2016")
word_vectors = model.wv
result = word_vectors.most_similar("natural_language_inference_(NLI)", topn=20)
print(result)

model = Word2Vec.load("word2vec.model_2017")
word_vectors = model.wv
result = word_vectors.most_similar("natural_language_inference_(NLI)", topn=20)
print(result)

model = Word2Vec.load("word2vec.model_2018")
word_vectors = model.wv
result = word_vectors.most_similar("natural_language_inference_(NLI)", topn=20)
print(result)

model = Word2Vec.load("word2vec.model_2019")
word_vectors = model.wv
result = word_vectors.most_similar("natural_language_inference_(NLI)", topn=20)
print(result)


