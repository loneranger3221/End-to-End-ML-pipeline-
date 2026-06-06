import pickle 
import sys
import os
from src.exception import CustomException

import dill
'''Dill is a python package which is used to serialize and deserialize python objects. It is an extension of the pickle module and it can serialize a wider range of python objects than pickle.'''

'''Main packages'''
import numpy as np
import pandas as pd

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        
        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)
    except Exception as e:
        raise CustomException(e, sys)