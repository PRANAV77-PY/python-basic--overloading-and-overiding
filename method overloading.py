class Calculater:
    def add(self,a=None,b=None,c=None):
        if a is not None and b is not None and c is not None:
            return a + b + c
        elif a is not None and b is not None:
            return a + b
        else:
            return a


calc = Calculater()
print(calc.add(2,3))
print(calc.add(2,3,4))
        