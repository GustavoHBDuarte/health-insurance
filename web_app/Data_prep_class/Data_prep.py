import pickle
import pandas as pd
import numpy as np
import json




class Data_prep(object):
    
    def __init__(self):        
        self.annual_premium_scaler               =  pickle.load(open('encoders/annual_premium_scaler.pkl', 'rb')) # Opening scaler        
        self.age_scaler                          =  pickle.load(open('encoders/age_scaler.pkl', 'rb')) # Opening scaler        
        self.policy_sales_channel_scaler         =  pickle.load(open('encoders/policy_sales_channel_scaler.pkl', 'rb')) # Opening scaler        
        self.region_code_scaler                  =  pickle.load(open('encoders/region_code_scaler.pkl', 'rb')) # Opening scaler        
        self.feature_engineer_health_insurance   =  pickle.load(open('encoders/feature_engineer_health_insurance.pkl', 'rb')) # Opening feature engineer        
        self.feature_selector_health_insurance   =  pickle.load(open('encoders/feature_selector_health_insurance.pkl', 'rb')) # Opening feature selector        
        self.stage_of_life_encoder               =  pickle.load(open('encoders/stage_of_life_encoder.pkl', 'rb')) # Opening encoder        
        self.vehicle_age_encoder                 =  pickle.load(open('encoders/vehicle_age_encoder.pkl', 'rb')) # Opening encoder
        
    
    
    def feature_engineering(self, df_2):
        
        
        # Lower-casering X_test columns <- requirement for data handling

        df_2.columns = [i.lower() for i in list(df_2.columns)]
        
        
        # Reorganizing columns <- requirement from 'feature engineer' object

        df_2 = df_2[['id', 'gender', 'age', 'region_code', 'policy_sales_channel', 
                     'previously_insured', 'annual_premium', 'vintage', 
                     'driving_license', 'vehicle_age', 'vehicle_damage']]
        
        # Setting 'id' column as index

        df_2 = df_2.set_index('id')
        
        
        
        # Creating the feature 'stage of life'

        df_2['stage_of_life']= df_2['age'].apply(lambda x: 'adult' if x>=20 and x<=39 
                                                 else 'middle_age_adult' if x>=40 and x<=59
                                                 else 'senior_adult')
        
        
        
        # ========== Data filtering =======================
        
        df_3 = df_2
        
        df_3 = df_3.drop(columns=['vintage'])
        
        return df_3
    
    
    
    
    def data_preparation(self, df_3):
        
        X_test = df_3
        
        
        # Scaling age
        
        X_test['age'] = self.age_scaler.transform(X_test[['age']].values) # scaling test
        
        
        # Scaling region_code
        
        X_test['region_code'] = self.region_code_scaler.transform(X_test[['region_code']].values) # scaling test
        
        
        # Scaling policy_sales_channel
        
        X_test['policy_sales_channel'] = self.policy_sales_channel_scaler.transform(X_test[['policy_sales_channel']].values) # scaling test
        
        
        # Scaling annual_premium
        
        X_test['annual_premium'] = self.annual_premium_scaler.transform(X_test[['annual_premium']].values) # scaling test
        
        
        
        # =============== Encoding =======================
        
        # One-hot-encoding gender
        
        X_test = pd.get_dummies(data=X_test, columns=['gender']) # encoding test
        
        
        # vehicle_damage - 1 for Yes, 0 for No
        
        X_test['vehicle_damage'] = [1 if i=='Yes' else 0 for i in X_test['vehicle_damage']] # encoding test
        
        
        # vehicle_age - Ordinal encoding
        
        X_test['vehicle_age'] = self.vehicle_age_encoder.transform(X_test[['vehicle_age']].values) # encoding test
        
        
        # stage of life - Label encoding
        
        X_test['stage_of_life'] = self.stage_of_life_encoder.transform(X_test[['stage_of_life']].values) # encoding test
        
        
        
        
        # ============= Re-engineering features ==============
        
        
        # Applying feature engineer object do X_test

        new_X_test = self.feature_engineer_health_insurance.transform(X_test)
        
        
        # Getting X_test with selected features

        new_X_test = self.feature_selector_health_insurance.transform(pd.DataFrame(new_X_test))
        
        
        # Redefining new_X_test indexes

        new_X_test.index = X_test.index
        
        
        return new_X_test
    
    
    
    def get_predictions(self, model, test_raw, df_3):
        
        # prediction
        predictions = model.predict_proba(df_3)
        
        # join predictions into the original data
        test_raw.loc[test_raw.index, 'Rank'] = predictions[:,1]
        
        # return data sorted by Rank
        #test_raw = test_raw.sort_values('Rank', ascending=False)
        
        
        return test_raw.to_json(orient='records', date_format='iso')    

