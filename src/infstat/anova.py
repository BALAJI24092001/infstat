import pandas as pd
class dataErrorException(Exception):
    def __init__(self):
        super().__init__("Undetected data format, give a dictionary or DataFrame.")
class anova:
    def __init__(self, data, alpha = 0.005, kind="crd", tail = "both"):
        self.Fcal = 0;
        self.treatmentDegreeOfFreedom = len(data);
        self.lstSize = list();
        self.lstData = list();
        if type(data) == type(pd.DataFrame()):
            if(kind=="crd"):
                for i in range(self.treatmentDegreeOfFreedom):
                    temp = data.iloc[i];
                    self.lstData.append([k for k in temp if str(k) != 'nan'])
                    self.lstSize.append(len(self.lstData[i]))        
            N = sum(self.lstSize)
            G = 0;
            for i in range(self.treatmentDegreeOfFreedom):
                for j in range(self.lstSize[i]):
                    G += self.lstData[i][j]
            CF = G**2 / N
            SS = 0;
            for i in self.lstData:
                for j in i:
                    SS += j**2;
            totalSumOfSquares = SS - CF;
            SS = 0;
            for i in range(self.treatmentDegreeOfFreedom):
                SS += sum(self.lstData[i])**2 / self.lstSize[i]
            treatmentSumOfSquares = SS - CF;
            errorSumOfSquares = totalSumOfSquares - treatmentSumOfSquares;
            meanTreatmentSumOfSquares = treatmentSumOfSquares/(self.treatmentDegreeOfFreedom-1);
            meanErrorSumOfSquares = errorSumOfSquares/(N-self.treatmentDegreeOfFreedom);
            self.Fcal = meanTreatmentSumOfSquares/meanErrorSumOfSquares;
        elif type(data) == dict:
            pass;
        else:
            raise dataErrorException();
