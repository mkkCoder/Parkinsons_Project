from statistics import mode
import pandas as pd
import numpy as np
import pickle
import pymongo
from sklearn.metrics import accuracy_score
import warnings
warnings.filterwarnings("ignore")


# print the predictions for the X_test, y_test data


CLIENT='mongodb://localhost:27017'
DATABASE='parkinson_models'


def load_data_from_db_as_model(client, db):
    myclient = pymongo.MongoClient(client)
    mydb = myclient[db]
    mycollections = mydb.list_collection_names()
    
    classifiers=[]
    for i in mycollections:        
        records=mydb[i].find()
        list_cr=list(records)
        for i in list_cr:
            for j in i['parameters']:
                i[j]=i['parameters'][j]
            del i['parameters']
            
        df=pd.DataFrame(list_cr)
        df['model']=df['model'].apply(lambda x: pickle.loads(x))
        classifier=df['model'][0]
        classifiers.append(classifier)
        
    return classifiers


def predict_y(x):       # x need to be list of features in a list [[feature1,feature2,feature3,...]]
    models=load_data_from_db_as_model(CLIENT,DATABASE)

    # make the predictions
    predictions=[]
    for model in models:
        y_pred = model.predict(x)
        predictions.append(y_pred[0])
    print(predictions, end='')

    # get the most common prediction (0 or 1)
    majority_vote=mode(predictions)
    
    if majority_vote==1:
        return 1
    else:
        return 0


# make the data sutable for the prediction function
myclient = pymongo.MongoClient(CLIENT)
mydb = myclient['parkinson']
mycon=mydb['test_to_mongo']
records=mycon.find()
patients=list(records)[0]['data']
p = pickle.loads(patients)

X_test = p[0]
Y_test = p[1]


voted_pred = []
for i in X_test:
    n = predict_y([i])
    voted_pred.append(n)   # call the function to predict the y for each x in Xes
    print(f' = {n}')


# convert to numpy list
voted_pred_np = np.array(voted_pred)    # convert to numpy array


# show the accuracy of the models (the accuracy of the majority vote)
print(f'accuracy: {accuracy_score(Y_test,voted_pred_np)}')

