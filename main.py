import matplotlib.pyplot as plt
import numpy as np

#x = np.random.rand(100) * 100
#y = 3 * x + 5 + np.random.rand(100) * 40 - 20

#x = np.array([20,24,27.5,31.5,35.5,40,45,50])
#y = np.array([672,668,691,711,714,727,751,765])

x = np.array([21.2,27,30,33,36,39,42,45,48,50])
y = np.array([2316,1711,1591,1449,1280,1160,1040,942,850,790])

a = 0
b = 0

k = 1.38064852e-23
x += 273.15
#y = np.log(y)
#x = 1/x

def j():
    #print(sum((y-(a*x+b))**2))
    return sum((y-a*np.exp(b/(x)))**2)

def j1(a,b): #誤差関数
    #return sum((y-(a*x+b))**2)
    return sum((y-a*np.exp(b/(x)))**2)

def min_loss():
    global a,b
    h = 1e-3
    aa = h * sum(2*(-a*x+y-b)*(-x))
    bb = h * sum(2*(-a*x+y-b)*(-1))
    a -= aa
    b -= bb

ah = 1e0
bh = 1e0
def min_loss1(): #誤差関数を最小化する関数
    global a,b,ah,bh
    #a -= 10000 * h * sum(2*(-a*x+y-b)*(-x))
    #b -= h * sum(2*(-a*x+y-b)*(-1))
    mema, memb = float('inf'),float('inf')
    tmpa, tmpb = float('inf'),float('inf')
    cnt = 0
    while True:
        cnt += 1
        if j1(a+ah,b) < j1(a,b):
            a += ah
        elif j1(a-ah,b) < j1(a,b):
            a -= ah
        if j1(a,b+bh) < j1(a,b):
            b += bh
        elif j1(a,b-bh) < j1(a,b):
            b -= bh
        mema,memb = tmpa,tmpb
        tmpa,tmpb = a,b
        if cnt % 1000 == 0:
            print(str(a)[0:10],str(b)[0:10],cnt)
        if mema == a:
            ah /= 1.1
        if memb == b:
            bh /= 1.1
        if cnt == 50000:
            break

min_loss1()
print(j())
#print(f"R:{np.exp(b)}, Q:{a*k}")
r = 0.019012020821896788
q = 4.746401479150738e-20
#a,b = r,q/k
print(j())
plt.scatter(x,y,s=3)
m = np.arange(290,340,1)
l = a * np.exp(b/m)
#l = a * m + b
plt.plot(m,l)
plt.show()
11386.171236072674