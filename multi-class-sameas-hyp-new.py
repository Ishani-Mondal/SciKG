from simpletransformers.classification import ClassificationModel
import pandas as pd
import logging
import numpy as np
import sklearn
import torch
#torch.manual_seed(0)
np.random.seed(0)

logging.basicConfig(level=logging.INFO)
transformers_logger = logging.getLogger("transformers")
transformers_logger.setLevel(logging.WARNING)

# Train and Evaluation data needs to be in a Pandas Dataframe of two columns. The first column is the text with type str, and the second column is the label with type int.
train_df = pd.read_csv('multi_class_same_hyp_wns_26.txt', delimiter="\t", error_bad_lines=False)
train_data=[]
for ind in train_df.index:
     sentences=[]
     sentences.append(train_df['sentences1'][ind]+"::"+train_df['type1'][ind])
     #sentences.append(train_df['sentences1'][ind]+" "+train_df['sentences2'][ind])
     sentences.append(train_df['sentences2'][ind]+"::"+train_df['type2'][ind])
     sentences.append(np.int64(train_df['is_similar'][ind]))
     train_data.append(sentences)
#train_data = [['Example sentence belonging to class 1', 1], ['Example sentence belonging to class 0', 0]]
train_df = pd.DataFrame(train_data, columns=['text_a', 'text_b', 'labels'])


eval_data=[]
eval_df = pd.read_csv('Sameas_Hyp_Entire_Test.txt', delimiter="\t", error_bad_lines=False)
for ind in eval_df.index:
     print('Creating Eval Data')
     sentences=[]
     sentences.append(eval_df['sentences1'][ind]+"::"+eval_df['type1'][ind])
     #sentences.append(train_df['sentences1'][ind]+" "+train_df['sentences2'][ind])
     sentences.append(eval_df['sentences2'][ind]+"::"+eval_df['type2'][ind])
     sentences.append(np.int64(eval_df['is_similar'][ind]))
     eval_data.append(sentences)

eval_df = pd.DataFrame(eval_data, columns=['text_a', 'text_b', 'labels'])



train_args={
    'reprocess_input_data': True,
    'overwrite_output_dir': True,
    'num_train_epochs': 2,
}


# Create a ClassificationModel
model = ClassificationModel('bert','bert-base-cased', num_labels=3, use_cuda=False, cuda_device=0, args=train_args)

# Train the model
model.train_model(train_df)

print("Start Evaluating")

# Evaluate the model
result, model_outputs, wrong_predictions = model.eval_model(eval_df, acc=sklearn.metrics.accuracy_score)

print("Evaluation done, writing ")
file1=open('output_entire.txt','w')
i=0
true=[]
preds=[]
for elem in model_outputs:
  true.append(eval_df['labels'][i])
  preds.append(np.argmax(elem, axis=-1))
  print('Writing')
  if(str(np.argmax(elem, axis=-1))!='0'):
    file1.write(str(np.argmax(elem, axis=-1))+"\n")
  i=i+1
