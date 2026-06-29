import sys 
from logger import logging 

def error_detail_message(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "error occured in python script name [{0}] line no [{1}] error detail [{2}]".format(file_name,exc_tb.tb_lineno,error)
    return error_message


class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_detail_message(error=error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message
    

try:
    10/0
except Exception as e:
    logging.info("zero division error")
    raise CustomException(e,sys)