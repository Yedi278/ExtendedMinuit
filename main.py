from Minuit_newClass import ExtendedMinuit

try:
    from iminuit import Minuit
except:
    Exception("Iminuit lib not installed! \n >>>pip install iminuit")

try:
    import sympy as sp
except:
    Exception("Sympy lib not installed! \n >>>pip install sympy")


if __name__ == '__main__':
    from iminuit.cost import*
    import numpy as np
    import matplotlib.pyplot as plt

    def f(x,a,b,c):
        return a*x**2+b*x+c

    x = np.linspace(0,10)
    y = [f(i,1,2,3)+np.random.uniform(0,1) for i in x]

    plt.scatter(x,y)
    # plt.show()

    c = LeastSquares(x,y,0.01,f)
    m = ExtendedMinuit(c,a=1,b=1,c=1)
    m.migrad()
    val = m.prop_errors('a,b,c','a*x**2+b*x+c',2,True)
    print(val)
    print(m)
