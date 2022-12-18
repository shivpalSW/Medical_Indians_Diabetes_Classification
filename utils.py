import config
import pickle
import pandas as pd
import sklearn
#import pymongo


model = pickle.load(open(config.MODEL_PATH, 'rb'))

# mongo_client = pymongo.MongoClient("mongodb://localhost:27017")
# db = mongo_client['diabetes']
# user_collection = db['diabetes_data']

def get_prediction(data):

    pregnant                    =  0
    plasma                      =  eval(data['plasma'])
    bp                          =  eval(data['bp'])
    bmi                         =  eval(data['bmi'])
    diabetes_pedigree_function  =  eval(data['diabetes_pedigree_function'])
    age                         =  int(eval(data['age']))

    test_df = pd.DataFrame([[pregnant,plasma,bp,bmi,diabetes_pedigree_function,age]], 
                                    columns=['pregnant','plasma','bp','bmi','diabetes_pedigree_function','age'])

    predicted_value = model.predict(test_df) 

    # record = test_df.to_dict("records")[0]
    # record.pop('pregnant')

    # user_collection.insert_one(record)

    return  predicted_value