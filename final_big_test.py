from flair.data import Sentence
from flair.embeddings import WordEmbeddings, FlairEmbeddings, TransformerWordEmbeddings
embedding = TransformerWordEmbeddings('allenai/scibert_scivocab_uncased')

f=open('./data/Sameas_Hyp_Entire_Test.txt')
content=f.read()

f1=open('./data/Final_big_test.txt','w')
f1.write('sentences1'+"\t"+'type1'+'\tsentences2\t'+'type2'+"\tis_similar"+"\n")
for line in content.split("\n"):
    if(line!=""):
        if(line.split("\t")[0]!='sentences1'):
            sentence1=Sentence(line.split("\t")[0])
            embedding.embed(sentence1)
            avg1=[]
            for token in sentence1:
                #print(token.embedding)
                avg1.append(token.embedding)

            avg1=sum(avg1)
            
            sentence2=Sentence(line.split("\t")[2])
            embedding.embed(sentence2)
            avg2=[]
            for token in sentence2:
                avg2.append(token.embedding)

            avg2=sum(avg2)
            if(float(np.dot(np.array(avg1), np.array(avg2))/(norm(np.array(avg1))*norm(np.array(avg2))))>0.85):
                f1.write(line.split("\t")[0]+"\t"+line.split("\t")[1]+"\t"+line.split("\t")[2]+"\t"+line.split("\t")[3]+"\t"+line.split("\t")[4]+"\n")