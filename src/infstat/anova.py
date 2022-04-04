import pandas as pd
class dataErrorException(Exception):
    def __init__(self):
        super().__init__("WrongDataException: Undetected data format, give a dictionary or DataFrame.")
class dictionaryArraySizeException(Exception):
    def __init__(self):
        super().__init__("ArraySizeErrorException: values in the dictionary are not of the same size. Add commas and leave the blanks incase of no values");
class anova:
    def __init__(self, data, alpha = 0.005, kind="crd", tail = "both"):
        self.Fcal = 0;
        self.treatmentDegreeOfFreedom = len(data);
        self.lstSize = list();
        self.lstData = list();
        if type(data) == type(pd.DataFrame()):
            pass;
        elif type(data) == dict:
            keys = [i for i in data]
            data = pd.DataFrame(data)
            
        else:
            raise dataErrorException();
        if(kind=="crd"):
            for i, j in zip(data.columns,range(self.treatmentDegreeOfFreedom)):
                temp = data[i];
                self.lstData.append([k for k in temp if str(k) != 'nan'])
                self.lstSize.append(len(self.lstData[j]))        
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
if __name__ == "__main__":
    # crd testing

    # testing with DoE practical 1 problem
    dictionary = {"A": [55, 49, 42, 21, 52], "B": [61, 112, 30, 89, 63], "C": [42, 97, 81, 95, 92],  "D": [169, 137, 169, 85, 154]}

    # instanciating the object of anova class
    obj =  anova(data = dictionary);
    print(obj.Fcal)
