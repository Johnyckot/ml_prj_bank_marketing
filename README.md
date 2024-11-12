


1. Problem desription

 A Portuguese banking institution applies direct marketing campaigns. The marketing campaigns were based on phone calls. Often, more than one contact to the same client was required, in order to access if the product (bank term deposit) would be (or not) subscribed.
 The project goal is to predict if the client will subscribe a term deposit based on available data about the customer.
 
 The dataset is publicly available https://www.openml.org/search?type=data&sort=runs&status=active&id=1461 

 Dataset consists of followng fiedls: 
 bank client data:
        1 - age (numeric)

        2 - job : type of job (categorical: "admin.","unknown","unemployed","management","housemaid","entrepreneur", "student","blue-collar","self-employed","retired","technician","services")

        3 - marital : marital status (categorical: "married","divorced","single"; note: "divorced" means divorced or widowed)

        4 - education (categorical: "unknown","secondary","primary","tertiary")

        5 - default: has credit in default? (binary: "yes","no")

        6 - balance: average yearly balance, in euros (numeric)

        7 - housing: has housing loan? (binary: "yes","no")

        8 - loan: has personal loan? (binary: "yes","no")

        related with the last contact of the current campaign:
        9 - contact: contact communication type (categorical: "unknown","telephone","cellular")

        10 - day: last contact day of the month (numeric)

        11 - month: last contact month of year (categorical: "jan", "feb", "mar", ..., "nov", "dec")

        12 - duration: last contact duration, in seconds (numeric)

        other attributes:
        13 - campaign: number of contacts performed during this campaign and for this client (numeric, includes last contact)

        14 - pdays: number of days that passed by after the client was last contacted from a previous campaign (numeric, -1 means client was not previously contacted)

        15 - previous: number of contacts performed before this campaign and for this client (numeric)

        16 - poutcome: outcome of the previous marketing campaign (categorical: "unknown","other","failure","success")

        output variable (desired target):
        17 - y - has the client subscribed a term deposit? (binary: "yes","no")
 
 2. Data analysis
    Data analysis and Model selsction is performed in Jupyter notebook ml_prj_bank-marketing.ipynb. 
    It consists of folowing sections:
      1. Download dataset 
      2. Prepare data
      3. EDA
      4. Training models
    All steps are designed to be fully reproducible/
 3. Exploritary Data Analisys results
    EDA is perormed in ml_prj_bank-marketing.ipynb notebook '3.EDA' section. Main results are:
    - According to the target value distribution ~11 percents of customers apply to a marketing company;
    - All categorical features have values (groups) with signifacant deviation from the gloabal mean target value, e.g. might highly invfuense the result;
    - According to Mutual Information metric, the most relevant Categorical features are: poutcome,month,contact
    - According to the Corellation analysis of Numerical features, the most important are: 'duration' , 'previous', 'pdays'

 4. Models training and evaluation
    In order to select the most fitting aproach, 4 models where trained on a dataset: Logistic Regression, Random Forest, Decision tree, XGBoost. 
    Each model was evaluated using the Area Under the Curve (AUC) metric, and then tuned to maximize the AUC value. The relevant code and results is in '4.Training models' section of ml_prj_bank-marketing.ipynb.
    Here is the outcome:
    Model  |  Max_AUC
    LogisticRegression | 0.907
    Decision Tree | 0.883
    Random Forest | 0.93
    XGBoost | 0.926

    The best result is achieved by 'Random Forest' with folowwing parameters n_estimators = 120, max_depth = 6. Therefore this model was selected for deploment.  

 5. Source code
    The project consists of 3 python scripts:     
        train.py - logic which trains selected model on the dataset from /data folder and saves it into a file model.bin;
        predict.py - launches the Flask web service  on the 9696 port and the /predict API method. It accepts JSON with customer data as an input and returns the prediction if the customer is going to subscribe or not. Prediction is based on the model from model.bin file. 
        predict-test.py - auxilary script which invokes the API call to localhost:99696/predict  passing the sample JSON, and prints-out the result of prediction. COuld be used for tests.

 6. Dependecy management
    



    












docker build -t bank-marketing-prediction .

docker run -it -p 9696:9696 bank-marketing-prediction:latest


