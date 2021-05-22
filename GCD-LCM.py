# Generowanie liczb pierwszych w zakresie do podanej liczby
def GenFirsts(x):
    IsFirst = True
    FirstsList = []
    
    for dividend in range(2, x+1):
        for divisor in range(2, dividend):
            if (dividend % divisor) != 0:
                IsFirst = True
            elif (dividend % divisor) == 0:
                IsFirst = False
                break
        if (IsFirst == True):
            FirstsList.append(dividend)
    return(FirstsList)

# Generowanie czynnikow pierwszych podanej liczby
def GenDivisors(x, list):
    DivisorsList = []
    
    while x != 1:
        for i in list:
            if (x % i) == 0:
                while (x % i) == 0:
                    DivisorsList.append(i)
                    x = x / i
    return(DivisorsList)

# Generowanie listy wspolnych czynnikow
def GenCommonDivisors(x, y):
    CommonDivisorsList = []
    
    for i in range(0, len(x)):
        for j in range(0, len(y)):
            if x[i] == y[j]:
                CommonDivisorsList.append(y[j])
                x[i] = "$"
                y[j] = "&"     
    return(CommonDivisorsList)

# Obliczanie NWD
def CountNWD(list):
    NWD = 1
    for i in list:
        NWD = NWD * i
    return(NWD)
    
# Obliczanie NWW
def CountNWW(x, y, NWD):
    NWW = (x * y) / NWD
    NWW = int(NWW)
    return(NWW)

a = int(input("Podaj 1. liczbe: "))
b = int(input("Podaj 2. liczbe: "))

y = GenDivisors(a, GenFirsts(a))
print(y)
z = GenDivisors(b, GenFirsts(b))
print(z)
w = GenCommonDivisors(y, z)
print(w)
u = CountNWD(w)
print("NWD: " + str(u))
t = CountNWW(a, b, u)
print("NWW: " + str(t))