class test:
    def __init__(self, a, b):
        self.a = a;
        self.b = b;
    def add(self):
        print("Addition of the supplied numbers is: ", self.a+self.b);
    def sub(self):
        print("Subtraction of the supplied two numbers is :", self.a-self.b);
    def mul(self):
        print("Multiplication of the supplied two numbers is :", self.a*self.b);
    def div(self):
        print("Division of the supplied two numbers is :", self.a/self.b);
temp = test(1, 2);
temp.add();
