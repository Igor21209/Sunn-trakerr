import sys
sys.path.append(r'C:\Users\ASUS\AppData\Local\Programs\Python\Python36-32\Lib\site-packages\Pillow-8.0.0-py3.6-win32.egg')
sys.path.append(r'C:\users\asus\appdata\local\programs\python\python36-32\lib\site-packages\numpy-1.19.2-py3.6-win32.egg')
from PIL import Image
import numpy as np

def test():
    f = Image.open('IMG_9417.jpg')
    Al = np.asarray(f, dtype='uint8')
    
    '''for i in range(n):
       Al = f.readline()
        for j in range(m):
       A[i][j] = Al[j].split()'''
    f.close 
    return Al

def contr(A,n,m):
    col = 0
    xs = 0
    ys = 0
    a = 50
    for i in range(n):
        for j in range(m):
            for m in range(3):
                if A[i][j][m] != a:
                    xs += i
                    ys += j
                    col += 1
    xm = xs/col
    ym = ys/col
    return round(xm),round(ym)

def prover(C):
    xc = float(input())
    yc = float(input())
    if xc == C[0] and yc == C[1]:
        return True
    else:
        return False

A = test()
n = len(A)
m = len(A[n-1])

print(A)
print('размер картинки: ', n, '*', m)

Cent = []*2
Cent = contr(A,n,m)
print('центр масс', Cent)
print(prover(Cent))


