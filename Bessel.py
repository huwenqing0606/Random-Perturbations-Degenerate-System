import matplotlib.pyplot as plt
import numpy as np
import random

from matplotlib import animation
import matplotlib.pyplot as plt

np.random.seed(1)

n=15000
dt=0.0001
eps=0.01

R=[]
R.append(2)

#for i in range(n):
#      R.append(R[i] + (0.5/R[i]-R[i])*dt+random.gauss(0,dt**0.5))
#      R.append(R[i] - R[i]*dt + random.gauss(0,dt**0.5))
#      R.append(R[i] + random.gauss(0,dt**0.5))
#      plt.plot(i/n,R[i],'r.')

A=[]
B=[]
A.append(0)
B.append(2)

for i in range(n):
       W=random.gauss(0,dt**0.5)
       R.append(R[i] + (0.5/R[i]-R[i])*dt+W)
       A.append(A[i] - (A[i]*B[i]/eps+A[i])*dt+random.gauss(0,dt**0.5))
       B.append(B[i] + (A[i]*A[i]/eps-B[i])*dt+W)
#      A.append(A[i] - (A[i]*B[i]/eps)*dt+random.gauss(0,dt**0.5))
#      B.append(B[i] + (A[i]*A[i]/eps)*dt+random.gauss(0,dt**0.5))
       plt.plot(i/n,B[i],'b.')
       plt.plot(i/n,R[i],'r.')
#      plt.plot(i/n,A[i],'k.')
#      plt.plot(i/n,(A[i]*A[i]+B[i]*B[i])**0.5,'g.')
#      plt.plot(i/n,A[i]*A[i]/eps,'b.')
#      plt.plot(i/n,A[i]*A[i]/eps,'r.')
#      plt.plot(i/n,A[i],'g.')

