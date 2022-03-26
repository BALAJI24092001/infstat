from criValues import *
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
    def __init__(self, string, alpha=0.005):
        self.seq = list(string)
        self.count = len(set(string))
        self.uniqVals = list(set(self.seq))
        self.count1 = 0
        self.count2 = 0
        self.runs = 1

        if self.count > 2:
            raise runTestAttributeError(leng = "extra")
        elif self.count < 2:
            raise runTestAttributeError(leng = "less")
        for i in range(len(self.seq) - 1):
            if self.seq[i] != self.seq[i+1]:
                self.runs = self.runs + 1
            if self.seq[i] == self.uniqVals[0]:
                self.count1 = self.count1 + 1
            elif self.seq[i] == self.uniqVals[1]:
                self.count2 = self.count2 + 1
    def solution(self, full = True):
        hypothesis = """
        RUN TEST FOR RANDOMNESS
        ````````````````````````
        H0: The sequence of the given bivariate data is random.
        H1: The sequence of the given bivariate data is not random.

        Here we are intending to check the randomness, so we are using run test.

        """
        step1 = "Step 1: Determine the run length 'R'."
        step2 = "we got the total number of runs = " + str(self.runs) + "."
        step3 = "we got the count of first attritbute " + str(self.uniqVals[0]) + "(m) = " + str(self.count1)
        step4 = "we got the count of first attritbute " + str(self.uniqVals[1]) + "(n) = " + str(self.count2)
        step5 = "Considering the alpha level of 5%(0.005), the critical region for the run test is given below: "
        step6 = "Check if the numbers of runs in the sequence, with m and n attributes of same time lies in the interval form the run test table."
        step7 = "The lower limit is " + str( runTestCriValues[self.count1-2][self.count2][0] ) + " and upper limit is " + str(runTestCriValues[self.count1-2][self.count2][1])
        step8 = "Comparing the run length with the critical values, we get"
        if(runTestCriValues[self.count1-2][self.count2][0] <= self.runs):
            if(self.runs == None or runTestCriValues[self.count1-2][self.count2][1] >= self.runs):
                step9 = "Since the run length lies in the interval, we fail to reject the null hypothesis."
            else:
                step9 = "Since the run length does not lie in the interval, we reject the null hypothesis."
        else:
            step9 = "Since the run length does not lie in the interval, we reject the null hypothesis."

        steps = [step1, step2, step3, step4, step5, step6, step7, step8, step9]
        for i in steps:
            print(i)
