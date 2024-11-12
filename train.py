import pickle

import pandas as pd
import numpy as np
from scipy.io import arff
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.ensemble import RandomForestClassifier

data_file_path = 'data/phpkIxskf'
output_file_path = 'model.bin'

model_params = {
    'n_estimators':120,
    'max_depth':20
}

numerical_columns = ['age', 'day', 'campaign' , 'pdays' , 'previous', 'balance', 'duration']

categorical_columns = ['job','marital','default','housing','loan','contact','month','poutcome']

def load_df(data_file_path):
    columns = [
        'age',
    'job',
    'marital',
    'education',
    'default',
    'balance',
    'housing',
    'loan',
    'contact',
    'day',
    'month',
    'duration',
    'campaign',
    'pdays',
    'previous',
    'poutcome',
    'target'
    ]


    int_columns = [
        'age', 'day', 'campaign' , 'pdays' , 'previous', 'target'
    ]

    float_columns = [
        'balance', 'duration'
    ]

    # Load your ARFF file
    data, meta = arff.loadarff(data_file_path)

    # Convert to a pandas DataFrame
    df = pd.DataFrame(data)

    # To decode byte strings into ordinary strings 
    df = df.applymap(lambda x: x.decode() if isinstance(x, bytes) else x)

    df.columns = columns

    # cast coluimns to correct datatypes
    for c in int_columns:
        df[c] = df[c].astype(int)
    for c in float_columns:
        df[c] = df[c].astype(float)
    # change the target caolumn values 1-->0 , 2-->1
    df['target'] = df['target'].replace(1,0).replace(2,1)
    
    return df

def train(df, model_params):
    # split dataset into Train(60%), Validation(20%) and Test(20%)   
    df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=1)
    df_train, df_val = train_test_split(df_full_train, test_size=0.25, random_state=1)

    y_train = df_train.target.values

    df_train = df_train.reset_index(drop=True)

    del df_train['target']

    # Vectorize dataset
    dv = DictVectorizer(sparse=False)
    train_dict = df_train[categorical_columns + numerical_columns].to_dict(orient='records')
    X_train = dv.fit_transform(train_dict)

    model = RandomForestClassifier(n_estimators=model_params['n_estimators'] , max_depth=model_params['max_depth'] ,random_state=1)
    model.fit(X_train, y_train)

    return dv, model

    





df = load_df(data_file_path)
dv, model = train(df,model_params)

with open(output_file_path, 'wb') as f_out:
        pickle.dump((dv, model), f_out)
    
print(f'the model is saved to {output_file_path}')

