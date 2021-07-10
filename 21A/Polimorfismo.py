
class Test:

    def __init__(self):
        pass

    def operaciones(self, a,b):
        if a==int(a) and b==int(b):
            return a+b
        if float(a) and float(b):
            return a*b


class Test2(Test):
    def operaciones(self, a,b):
        pass


test=Test()
print(test.operaciones(2.3,3.0))