from statistics import mode
import pandas as pd
import numpy as np
import pickle
import pymongo
import warnings
warnings.filterwarnings("ignore")

CLIENT='mongodb://localhost:27017'
DATABASE='parkinson_models'


def load_data_from_db_as_model(client, db):
    '''
    Load the data from the database as a DataFrame,
    And return a list of models from the DataFrame.
    '''
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

def load_scaler_from_db():
    '''
    Load the scaler used to transform the data
    '''
    myclient = pymongo.MongoClient(CLIENT)
    mydb = myclient['parkinson']
    mycon=mydb['test_to_mongo']
    records=mycon.find()
    patients=list(records)[0]['data']
    p = pickle.loads(patients)
    scaler = p[2]                  
    return scaler


def predict_y(x):
    '''
    Return the predicted y value for the given x value.
    x need to be list of features in a list [[feature1,feature2,feature3,...]]
    '''
    
    scaler = load_scaler_from_db()
    new_pd_x = pd.DataFrame(x)
    new_np_x = scaler.transform(new_pd_x)
    
    models=load_data_from_db_as_model(CLIENT,DATABASE)

    # save all models predictions in a list
    print(new_np_x)
    predictions=[]
    for model in models:
        y_pred = model.predict(new_np_x)
        predictions.append(y_pred[0])
    
    # get the most common prediction (0 or 1)
    majority_vote=mode(predictions)
    
    if majority_vote==1:
        return 1
    else:
        return 0


