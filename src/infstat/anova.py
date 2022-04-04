import pandas as pd
class dataErrorException(Exception):
    def __init__(self):
        super().__init__("Undetected data format, give a dictionary or DataFrame.")
class anova:
    def __init__(self, data, alpha = 0.005, kind="crd", tail = "both"):
        self.Fcal = 0;
        df = len(data);
        lstSize = list();
        lstData = list();
        if type(data) == type(pd.DataFrame()):
            if(kind=="crd"):
                for i in range(df):
                    temp = data.iloc[i];
                    lstData.append([k for k in temp if str(k) != 'nan'])
                    lstSize.append(len(lstData[i]))        
            N = sum(lstSize)
            G = 0;
            for i in range(df):
                for j in range(lstSize[i]):
                    G += lstData[i][j]
            CF = G**2 / N
            SS = 0;
            for i in lstData:
                for j in i:
                    SS += j**2;
            TSS = SS - CF;
            SS = 0;
            for i in range(df):
                SS += sum(lstData[i])**2 / lstSize[i]
            SSB = SS - CF;
            SSE = TSS - SSB;
            MSSB = SSB/(df-1);
            MSSE = SSE/(N-df);
            self.Fcal = MSSB/MSSE;
            print("df", df);
            print("lstSize ", lstSize)
            print("lstData ", lstData)
            print("TSS ", TSS)
            print("SSB ", SSB)
            print("SSE ", SSE)
        elif type(data) == dict:
            pass;
        else:
            raise dataErrorException();
    def crd(lstData, df, lstSize):
        pass;

