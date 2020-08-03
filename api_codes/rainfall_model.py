from predictor import Predictor
import os

path = 'models'


class Rainfall_Model:
    def __init__(self):
        self.dam1 = os.path.join(path, 'dam1Model.model')
        self.dam2 = os.path.join(path, 'dam2Model.model')
        self.dam3 = os.path.join(path, 'dam3Model.model')

        self.dam2RT = os.path.join(path, 'dam2Receive-Time.model')
        self.dam3RT = os.path.join(path, 'dam3Receive-Time.model')

        self.dam3RL = os.path.join(path, 'dam3Receive-LevelRise.model')

    def dam1_rainfall_rise(self, listValues):
        modelPath = self.dam1
        predictor = Predictor(modelPath)
        out = []
        for i in predictor.predict(listValues).tolist():
            out.append(i[0])
        return out

    def dam2_rainfall_rise(self, listValues):
        modelPath = self.dam2
        predictor = Predictor(modelPath)
        out = []
        for i in predictor.predict(listValues).tolist():
            out.append(i[0])
        return out

    def dam3_rainfall_rise(self, listValues):
        modelPath = self.dam3
        predictor = Predictor(modelPath)
        out = []
        for i in predictor.predict(listValues).tolist():
            out.append(i[0])
        return out

    def dam2_Receive_Time(self, listValues):
        modelPath = self.dam2RT
        predictor = Predictor(modelPath)
        out = []
        for i in predictor.predict(listValues).tolist():
            out.append(i[0])
        return out

    def dam3_Receive_Time(self, listValues):
        modelPath = self.dam3RT
        predictor = Predictor(modelPath)
        out = []
        for i in predictor.predict(listValues).tolist():
            out.append(i[0])
        return out

    def dam3_Receive_Level(self, listValues):
        modelPath = self.dam3RL
        predictor = Predictor(modelPath)
        out = []
        for i in predictor.predict(listValues).tolist():
            out.append(i[0])
        return out
