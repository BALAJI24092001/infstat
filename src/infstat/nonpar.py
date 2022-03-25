class runTestAttributeError(Exception):
    def __init__(self, leng):
        message1 = "The data given for the test is not bivariate data. More than two attributes are given in the sequence."
        message2 = "The data given for the test is bivariate data. Only one attribute is given in the sequence."
        if leng == 'extra':
            super().__init__(message1)
        if leng == 'less':
            super().__init__(message2)

class runTest():
    '''

    '''
    def __init__(self, string, alpha= 0.005, sol = True):
        seq = list(string)
        count = len(set(string))
        if count > 2:
            raise runTestAttributeError(leng = "extra")
        elif count < 2:
            raise runTestAttributeError(leng = "less")
        runs = int(1)
        for i in range(len(seq) - 1):
            if seq[i] != seq[i+1]:
                runs = runs + 1
    def solution(self, full = True):
        hypothesis = """
        RUN TEST FOR RANDOMNESS
        ````````````````````````
        H0: The sequence of the given bivariate data is random.
        H1: The sequence of the given bivariate data is not random.
        """
