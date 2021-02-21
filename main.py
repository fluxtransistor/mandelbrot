ITERATIONS = 100

class Complex:
    def __init__(self,re,im):
        self.re= re
        self.im= im
        self.mod=re*re + im*im

    def __add__(self, other):
        if type(other) == int or type(other) == float:
            return Complex(self.re+other,self.im)
        else:
            re=self.re+other.re
            im=self.im+other.im
            return Complex(re,im)

    def __radd__(self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other)

    def __mul__(self, other):
        re = self.re * other.re
        re -= self.im * other.im
        im = self.im * other.re + self.re * other.im
        return Complex(re,im)

    def __str__(self):
        return str(self.re)+" + "+str(self.im)+"i"


def iterate(c, iterations=100):
    val = Complex(0,0)
    decreases = 0
    for i in range(100):
        new_val = val*val + c
        if new_val.mod < val.mod:
            decreases += 1
        val = new_val
    return val, decreases


if __name__ == "__main__":
    re = float(input("The real part of c: "))
    im = float(input("The imaginary part of c: "))
    c = Complex(re, im)
    z, decreases = iterate(c)
    print(z, decreases, sep=", ")