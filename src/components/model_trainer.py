import os 
import sys 
from src.exception import CustomException
from src.logger import logging 
import pandas as pd 

from sklearn.linear_model import LinearRegression,Lasso,Ridge
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor,AdaBoostRegressor,GradientBoostingRegressor
from xgboost import XGBRegressor
from catboost import CatBoostRegressor
from sklearn.svm import SVR
from sklearn.metrics import r2_score

from dataclasses import dataclass

from src.utils import save_object,evaluate_model

@dataclass 
class ModelTrainerConfig:
    model_path = os.path.join("artifacts","model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_path_config = ModelTrainerConfig()

    def model_train(self,train_arr,test_arr):
        try:
            models = {
                "linear regression":LinearRegression(),
                "lasso regression":Lasso(),
                "ridge regression":Ridge(),
                "k neighbors regressor":KNeighborsRegressor(),
                "decision tree regressor":DecisionTreeRegressor(),
                "random forest regressor":RandomForestRegressor(),
                "adaboost regressor":AdaBoostRegressor(),
                "gradient boost regressor":GradientBoostingRegressor(),
                "XG boost regressor":XGBRegressor(),
                "support vector regressor":SVR(),
                "Catboost regressor":CatBoostRegressor(verbose=False)
            }
            logging.info("Model training started")

            x_train,y_train,x_test,y_test = [train_arr[:,:-1],train_arr[:,-1],test_arr[:,:-1],test_arr[:,-1]]
            r2_list = []
            model_list = []
            for name,model in models.items():
                model.fit(x_train,y_train)
                y_test_pred = model.predict(x_test)
                y_train_pred = model.predict(x_train)

                r2_train,r2_test,mse_train,mse_test,mae_train,mae_test = evaluate_model(x_train_pred=y_train_pred,
                                                            x_test_pred=y_test_pred,y_train=y_train,y_test=y_test)
                
                r2_list.append(r2_test)
                model_list.append(name)

            score_df = pd.DataFrame(list(zip(model_list,r2_list)),columns=["model_name","r2_score"]).sort_values(by="r2_score",ascending=False)
            best_model_name = score_df.iloc[0,0]
            best_model = models[best_model_name]

            best_model.fit(x_train,y_train)
            best_model_pred = best_model.predict(x_test)

            r2_square = r2_score(y_test,best_model_pred)

            logging.info("best model found with r2_score = {}".format(r2_square))

            save_object(file_path=self.model_path_config.model_path,obj=best_model)
            logging.info("model saved")

            return r2_square

        except Exception as e:
            raise CustomException(e,sys)



