import pandas as pd
class dataErrorException(Exception):
    def __init__(self):
        super().__init__("WrongDataException: Undetected data format, give a dictionary or DataFrame.")
class dictionaryArraySizeException(Exception):
    def __init__(self):
        super().__init__("ArraySizeErrorException: values in the dictionary are not of the same size. Add commas and leave the blanks incase of no values");

class anova:
    """
    Perform one-way and two-way anova on multiple samples of based on 
    CRD(Completely randomized design) or RBD(Randomized block design).

    Hypothesis: 
        H0: Mu1 = Mu2 = ... = Mun = Mu (CRD) or (RBD 1)
        H1: Mui != Muj ; i!= j ; i,j = 1, 2, 3, ... n

        H0: Mu1 = Mu2 = ... = Mun = Mu (RBD 2)
        H1: Mui != Muj ; i != j ; i,j = 1, 2, 3, ... n

    Aim: (CRD) To check whether if there is a significant difference 
         in the mean between the rows(some given treatment).

         (RBD) To check whether if there is a significant difference 
         in the mean samples of blocks and treatments.

    Parameters
    ``````````
    data : array-like
           Pandas DataFrame or dictionary data. Note: Each sample 
           in the dataFrame must be in a single column, row wise 
           sample data is not encouraged, not to be included soon 
           with specifying parameter.
    alpha: {0.1, 0.05, 0.025, 0.01}The significance level, is the probability 
           of rejecting the null hypothesis when it is true. default = 0.05 
           indicating 5% significance level. alpha in percentage = alpha*100
    kind : {"crd", "rbd"} CRD(Completely randomized design) is a design of
           experimental model design for one-way analysis of vairance, requires 
           a one-way data in the form of dataDframe or a dictionary as like 
           given in the example.
           RBD(Randomized block design) is a design of experiment model design
           for two-way analysis of variance, requires two-way classified data
           all the values must be filled, one missing value type to be
           added soon.
    tail : {"right", "left", "both"} This indicates the tail of the test, either
           right, left or both tails. Giving right tial indicates, neglecting the
           chance that it can be in the left tail. Only to use when only one tail 
           is of the only interest of test.

    returns
    ```````
    Fcal : retunrs the F caluculated value based on the sum of squares of the
           treatments(and blocks if for RBD) by considering the error sum of 
           squares making the value given, aware of the error produced by the 
           treatments(and blocks incase of RBD).
    treatmentDegreeOfFreedom : The degree of freedom for treatments(CRD, RBD)
           used for calculating the mean sum of squares, value taken from the
           number of samples given in one-way or two-way data minus 1,
           indicating the lose of chance for the last element to participate
           in calculating the last value.
    lstSize : list of sizes of each sample in the one way classified data.
           the length of the DataFrame or the number of coumns indicates the 
           size of each row sample and column sample in randomized block
           design respectively.

    References:
    ```````````
    [1]. Statistics How to: Anova 
         https://www.statisticshowto.com/probability-and-statistics/hypothesis-testing/anova/
    [2]. Analysis of variance 
         https://en.wikipedia.org/wiki/Analysis_of_variance
    [3]. Analysis of variance (Explained) : Towards Data Science
         https://towardsdatascience.com/anova-analysis-of-variance-explained-b48fee6380af

    Example:
    >> import pandas as pd
    >> import anova as av
    >> data = pd.read_csv("input/test.csv")
    >> data
          A     B     C     D
    0   5.7  18.9  29.4  29.1
    1  10.2  19.1  16.4  21.2
    2   5.4  24.0  37.0  38.8
    3   9.5  24.9  41.7  28.9
    >> mod = av.anova(data)
    >> mod.Fcal
    9.612824127996081
    """
    def __init__(self, data, alpha = 0.05, kind="crd", tail = "both"):
        self.data = data;
        if type(data) == type(pd.DataFrame()):
            pass;
        elif type(data) == dict:
            keys = [i for i in data]
            data = pd.DataFrame(data)
        else:
            raise dataErrorException();
        if kind == "crd":
            self.crd();
        elif kind == "rbd":
            rbd();
    def crd(self):
        self.Fcal = 0;
        self.treatmentDegreeOfFreedom = len(self.data.columns);
        self.lstSize = list();
        self.lstData = list();
        for i, j in zip(self.data.columns,range(self.treatmentDegreeOfFreedom)):
            temp = self.data[i];
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
    def rbd(self):
        """
        Given a two-way classified data caluculates whether there is any significant difference in the blocks or columns.
        """
        self.treatmentDegreeOfFreedom = len(self.data.columns)
        self.blockDegreeOfFreedom = len(self.data)
        self.treatments = [list(self.data[i]) for i in self.data.columns]
        self.blocks = [list(self.data.iloc[i]) for i in range(len(data))]
        self.treatmentSums = [sum(i) for i in self.treatments]
        self.blockSums = [sum(i) for i in self.blocks]
        self.treatmentSumOfSquares = [i**2 for i in self.treatmentSums]
        self.blockSumOfSquares = [i**2 for i in self.blockSums]
    def summary(self):
        pass;
if __name__ == "__main__":
    # crd testing

    # testing with DoE practical 1 problem
    dictionary = {"A": [55, 49, 42, 21, 52], 
                  "B": [61, 112, 30, 89, 63], 
                  "C": [42, 97, 81, 95, 92],  
                  "D": [169, 137, 169, 85, 154]}

    # instanciating the object of anova class
    data = pd.read_csv("input/test.csv")
    obj0 =  anova(data = dictionary);
    obj1 = anova(data = data)
    print("F cal value from dictionary data is : ", obj0.Fcal);
    print("F cal value from CSV file data is : ", obj1.Fcal);
