import pickle 
import os
import sys 

from src.exception import CustomException 
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score

def save_object(file_path,obj):
    try:
        os.makedirs(os.path.dirname(file_path),exist_ok=True)

        with open(file_path,"wb") as file:
            pickle.dump(obj,file)
    except Exception as e:
        raise CustomException(e,sys)
    
def evaluate_model(x_train_pred,y_train,x_test_pred,y_test):
    try:
        r2_train = r2_score(y_train,x_train_pred)
        mse_train = mean_squared_error(y_train,x_train_pred)
        mae_train = mean_absolute_error(y_train,x_train_pred)

        r2_test = r2_score(y_test,x_test_pred)
        mse_test = mean_squared_error(y_test,x_test_pred)
        mae_test = mean_absolute_error(y_test,x_test_pred)

        return r2_train,r2_test,mse_train,mse_test,mae_train,mae_test
    
    except Exception as e:
        raise CustomException(e,sys)

