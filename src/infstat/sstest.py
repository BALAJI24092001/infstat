import pandas as pd
import numpy as np
class oneMean:
    '''
    This is for one mean test
    '''
    def __init__(self, data, mean, x=None):
        dt = None;
        df = int(0);
        mean = int(0);
        std = float(0);
        p_val = float(0);
        decision = str();
        if type(data) == "<class 'pandas.core.frame.DataFrame'>":
            if type(x) == "<class 'NoneType'>":
                print(" "*10, "-"*10)
                print("The column name 'x' is necessary for datatype DataFrame.")
                print(" "*10, "-"*10)
            else:
                self.dt = np.array(data[x]);
                self.mean = self.dt.mean();
                self.std = self.dt.std();
                self.df = np.prod(self.dt.shape);

