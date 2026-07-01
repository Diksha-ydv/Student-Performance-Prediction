import pandas as pd 
import numpy as np 
import sys 
import os 

from src.logger import logging
from src.exception import CustomException
from dataclasses import dataclass
from sklearn.model_selection import train_test_split
from src.components.data_transformation import DataTransformation,DataTransformationConfig
from src.components.model_trainer import ModelTrainer,ModelTrainerConfig

@dataclass
class DataIngestionConfig:
    train_data_path:str = os.path.join("artifacts","train.csv")
    test_data_path:str = os.path.join("artifacts","test.csv")
    raw_data_path:str = os.path.join("artifacts","data.csv")

class DataIngestion:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()

    def initiate_data_path(self):
        try:
            logging.info("Data ingestion process started")
            df = pd.read_csv("notebook/data/stud.csv")

            os.makedirs(os.path.dirname(self.data_ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.data_ingestion_config.raw_data_path,index=None,header=True)
            train_set,test_set = train_test_split(df,test_size=0.2,random_state=1)

            train_set.to_csv(self.data_ingestion_config.train_data_path,index=None,header=True)
            test_set.to_csv(self.data_ingestion_config.test_data_path,index=None,header=True)
            logging.info("Train test splitting done")

            return self.data_ingestion_config.train_data_path,self.data_ingestion_config.test_data_path

        except Exception as e:
            raise CustomException(e,sys)
        
if __name__=="__main__":
    data_ingestion = DataIngestion()
    train_data,test_data = data_ingestion.initiate_data_path()

    data_transform = DataTransformation()
    train_arr,test_arr,_ = data_transform.train_test_transform(train_data,test_data)


    model_trainer = ModelTrainer()
    r2_square = model_trainer.model_train(train_arr,test_arr)
    print(f"r2 score is : {r2_square}")