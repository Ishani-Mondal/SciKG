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
                    if(ent['confidence']>0.8):
                        sentences=sentences+" "+"_".join(ent['text'].split())
                    if(ent['type']=='TASK' and ent['confidence']>0.75):
                        tasks.append(ent['text'].lower())
                        total_tasks.append("_".join(ent['text'].split()))
                    if(ent['type']=='DATASET' and ent['confidence']>0.75):
                        datasets.append(ent['text'].lower())
                        total_datasets.append("_".join(ent['text'].split()))
                    if(ent['type']=='METRIC' and ent['confidence']>0.75):
                        metrics.append(ent['text'].lower())
                        total_metrics.append("_".join(ent['text'].split()))
            for elem in data['introductionContent']:
                for ent in elem['entities']:
                    if(ent['confidence']>0.8):
                        sentences=sentences+" "+"_".join(ent['text'].split())
                    if(ent['type']=='TASK' and ent['confidence']>0.75):
                        tasks.append(ent['text'].lower())
                        total_tasks.append("_".join(ent['text'].split()))
                    if(ent['type']=='DATASET' and ent['confidence']>0.75):
                        datasets.append(ent['text'].lower())
                        total_datasets.append("_".join(ent['text'].split()))
                    if(ent['type']=='METRIC' and ent['confidence']>0.75):
                        metrics.append(ent['text'].lower())
                        total_metrics.append("_".join(ent['text'].split()))
            for elem in data['datasetContent']:
                for ent in elem['entities']:
                    if(ent['confidence']>0.8):
                        sentences=sentences+" "+"_".join(ent['text'].split())
                    if(ent['type']=='TASK' and ent['confidence']>0.75):
                        tasks.append(ent['text'].lower())
                        total_tasks.append("_".join(ent['text'].split()))
                    if(ent['type']=='DATASET' and ent['confidence']>0.75):
                        datasets.append(ent['text'].lower())
                        total_datasets.append("_".join(ent['text'].split()))
                    if(ent['type']=='METRIC' and ent['confidence']>0.75):
                        metrics.append(ent['text'].lower())
                        total_metrics.append("_".join(ent['text'].split()))
        except:
            pass 
        dictionary_yearwise[key].append(sentences.split())

import collections
od = collections.OrderedDict(sorted(dictionary_yearwise.items()))
sentences={}
i=1
for k, v in sorted(dictionary_yearwise.items()):
    sentences[str(k)]=[]

i=1979
for k, v in sorted(dictionary_yearwise.items()):
    for elem in v:
        sentences[k].append(elem)

t1_sents={}
t2_sents={}
t3_sents={}
t4_sents={}

for year, sents in sentences.items():
    if(int(year)<=1989):
        for elem in sents:
            t1_sents[1]=[]
    if(int(year)<=1999 and int(year)>1989):
        for elem in sents:
            t2_sents[2]=[]
    if(int(year)<=2009 and int(year)>1999):
        for elem in sents:
            t3_sents[3]=[]
    if(int(year)<=2019 and int(year)>2009):
        for elem in sents:
            t4_sents[4]=[]

for year, sents in sentences.items():
    if(int(year)<=1989):
        for elem in sents:
            t1_sents[1].append(elem)
    if(int(year)<=1999 and int(year)>1989):
        for elem in sents:
            t2_sents[2].append(elem)
    if(int(year)<=2009 and int(year)>1999):
        for elem in sents:
            t3_sents[3].append(elem)
    if(int(year)<=2019 and int(year)>2009):
        for elem in sents:
            t4_sents[4].append(elem)

for elem in t4_sents.values():
    print(len(elem))



from gensim.models import Word2Vec
for key, sentences1 in t4_sents.items():
    model = Word2Vec(sentences=sentences1, vector_size=200, window=5, min_count=1, workers=4)
    model.save("/mnt/c/Users/D.MONDAL/Downloads/tdm-kg-new/tdm-kg/ACLAnthTill2015_Prediction/w2v_models/word2vec.model")


for key, sentences1 in t1_sents.items():
    model = Word2Vec(sentences=sentences1, vector_size=200, window=5, min_count=1, workers=4)
    model.save("/mnt/c/Users/D.MONDAL/Downloads/tdm-kg-new/tdm-kg/ACLAnthTill2015_Prediction/w2v_models/word2vec1.model")


for key, sentences1 in t2_sents.items():
    model = Word2Vec(sentences=sentences1, vector_size=200, window=5, min_count=1, workers=4)
    model.save("/mnt/c/Users/D.MONDAL/Downloads/tdm-kg-new/tdm-kg/ACLAnthTill2015_Prediction/w2v_models/word2vec2.model")


for key, sentences1 in t3_sents.items():
    model = Word2Vec(sentences=sentences1, vector_size=200, window=5, min_count=1, workers=4)
    model.save("/mnt/c/Users/D.MONDAL/Downloads/tdm-kg-new/tdm-kg/ACLAnthTill2015_Prediction/w2v_models/word2vec3.model")



os.chdir("/mnt/c/Users/D.MONDAL/Downloads/tdm-kg-new/tdm-kg/ACLAnthTill2015_Prediction/w2v_models/")

print("========================1979=======================")
model = Word2Vec.load("word2vec1.model")
word_vectors = model.wv
#result1 = word_vectors.most_similar("textual_entailment", topn=20)
#v1=word_vectors['textual_entailment']
#print(result1)

#print("========================1989=======================")
model = Word2Vec.load("word2vec2.model")
word_vectors = model.wv
#v2=word_vectors['textual_entailment']
#result2 = word_vectors.most_similar("textual_entailment", topn=20)
#print(result2)

print("========================1999=======================")
model = Word2Vec.load("word2vec3.model")
word_vectors = model.wv
v3=word_vectors['textual_entailment']
result3 = word_vectors.most_similar("textual_entailment", topn=20)
print(result3)


print("========================2009=======================")
model = Word2Vec.load("word2vec.model")
word_vectors = model.wv
v4=word_vectors['natural_language_inference_(NLI)']
result4 = word_vectors.most_similar("natural_language_inference_(NLI)", topn=20)
print(result4)

print("Top 10 Tasks for textual_entailment for 1999-2009")
for res in result3:
    if(res[0] in list(set(total_tasks))):
        print(res[0])

print("================================================")

print("Top 10 Datasets for textual_entailment for 1999-2009")
for res in result3:
    if(res[0] in list(set(total_datasets))):
        print(res[0])

print("================================================")

print("Top 10 Metrics for textual_entailment for 1999-2009")
for res in result3:
    if(res[0] in list(set(total_metrics))):
        print(res[0])

print("================================================")

print("Top 10 Tasks for NLI for 2009-2019")
for res in result4:
    if(res[0] in list(set(total_tasks))):
        print(res[0])

print("================================================")

print("Top 10 Datasets for NLI for 2009-2019")
for res in result4:
    if(res[0] in list(set(total_datasets))):
        print(res[0])

print("================================================")

print("Top 10 Metrics for NLI for 2009-2019")
for res in result4:
    if(res[0] in list(set(total_metrics))):
        print(res[0])