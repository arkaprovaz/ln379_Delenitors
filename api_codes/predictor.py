from pickle5 import pickle 
from sklearn.linear_model import LinearRegression
import numpy as np 

class Predictor:

    def __init__(self,modelPath):
        self.model = pickle.load(open(modelPath,'rb'))

    def predict(self,listValues):
        value = listValues
        data = np.array(value).reshape(-1,1)
        result = (self.model).predict(data)
        return result

