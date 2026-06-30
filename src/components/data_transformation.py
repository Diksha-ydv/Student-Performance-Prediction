import pandas as pd 
import numpy as np 
import os 
import sys 
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from dataclasses import dataclass

from src.logger import logging 
from src.exception import CustomException
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from src.utils import save_object


@dataclass
class DataTransformationConfig:
    preprocessor_path:str = os.path.join("artifacts","preprocessor.pkl")


class DataTransformation:
    def __init__(self):
        self.tranformation_config = DataTransformationConfig()

    def initiate_transformation(self):
        try:
            num_feature = ["reading_score","writing_score"]
            cat_feature = ["gender","lunch","race_ethnicity","parental_level_of_education","test_preparation_course"]

            num_pipeline = Pipeline(steps=
                                    [("imputer",SimpleImputer(strategy="median")),
                                    ("standard scaler",StandardScaler())
            ]
            )
            
            cat_pipeline = Pipeline(steps=[
                ("imputer",SimpleImputer(strategy="most_frequent")),
                ("onehot encoding",OneHotEncoder()),
                ("standard scaler",StandardScaler(with_mean=False))
            ]
            )

            ct = ColumnTransformer(
                transformers=[("num_pipeline",num_pipeline,num_feature),
                            ("cat_pipeline",cat_pipeline,cat_feature)]
            )

            logging.info("Data transformation started")
            logging.info(f"numerical features = {num_feature}")
            logging.info(f"categorical features = {cat_feature}")

            return ct 
        
        except Exception as e:
            raise CustomException(e,sys)
        
    def train_test_transform(self,train_path,test_path):
        try:
            train_data = pd.read_csv(train_path)
            test_data = pd.read_csv(test_path)

            x_train_data_df = train_data.drop("math_score",axis=1)
            target_train_data_df = train_data["math_score"]

            x_test_data_df = test_data.drop("math_score",axis=1)
            target_test_data_df = test_data["math_score"]
            
            preprocessor_obj = self.initiate_transformation()

            x_train_transformed = preprocessor_obj.fit_transform(x_train_data_df)
            x_test_transformed = preprocessor_obj.transform(x_test_data_df)

            x_train_arr = np.c_[x_train_transformed,np.array(target_train_data_df)]
            x_test_arr = np.c_[x_test_transformed,np.array(target_test_data_df)]

            save_object(file_path=self.tranformation_config.preprocessor_path,obj=preprocessor_obj)
            logging.info("Saved preprocessing object")


            return x_train_arr,x_test_arr,self.tranformation_config.preprocessor_path
        except Exception as e:
            raise CustomException(e,sys)


        
