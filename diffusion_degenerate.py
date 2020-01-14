import matplotlib.pyplot as plt
import numpy as np
import random

from matplotlib import animation
import matplotlib.pyplot as plt

np.random.seed(1)

fig,ax=plt.subplots()

n=50000
UPDATE_STEP = 50000
eps=0.001
dt=0.001
A=[]
B=[]
A.append(1)
B.append(1)

def update_line(n, A, line):
 for j in range(UPDATE_STEP):
  i = n * UPDATE_STEP + j
  print(i)
  A.append(A[i] + (2/A[i]-A[i])*dt+random.gauss(0,dt))
#  A.append(A[i] - (A[i]*B[i]/eps+A[i])*dt+random.gauss(0,dt))
#  B.append(B[i] + (A[i]*A[i]/eps-B[i])*dt+random.gauss(0,dt))
 line.set_data(A,0)
 return line

l, = plt.plot(A,B, color='red')

line_ani = animation.FuncAnimation(fig, 
                                   update_line, 
                                   int(n/UPDATE_STEP), 
                                   fargs=(A, B, l),
                                   interval=1, 
                                   blit=False, 
                                   repeat=False)

plt.xlim(-0.1, 2)
plt.ylim(-0.1, 2)

plt.show()

#plt.subplot(111)
#plt.plot(A[0:200],B[0:200])
#
#plt.subplot(112)
#plt.plot(A[0:500],B[0:500])
#
#plt.subplot(1,1,1)
#plt.plot(A[0:1000],B[0:1000])
#
#plt.subplot(1,1,1)
#plt.plot(A[0:5000],B[0:5000])

#Generate one data point (A[i],B[i])
#def data_gen():  
#    cnt = 0  
#    while cnt < n:  
#        cnt+=1  
#        yield A[cnt], B[cnt]  
#
#
#line,=ax.plot(A[0],B[0])
#
#def animate(i):
#    line.set_data(A[i], B[i])
#    return line,
#
#def init():
#    line.set_data(A[0], B[0])
#    return line,
#
#ani=animation.FuncAnimation(fig=fig, 
#                            func=animate, 
#                            frames=100, 
#                            init_func=init, 
#                            interval=10000, 
#                            blit=True)
#plt.show()

   
  
# 绘图  
#fig, ax = plt.subplots()  
#line, = ax.plot([], [], lw=2)  
#ax.set_ylim(-1.1, 1.1)  
#ax.set_xlim(0, 5)  
#ax.grid()  
#xdata, ydata = [], []  
#  
# 因为run的参数是调用函数data_gen,所以第一个参数可以不是framenum:设置line的数据,返回line  
#def run(data):  
    # update the data  
#    t,y = data  
#    xdata.append(t)  
#    ydata.append(y)  
#    xmin, xmax = ax.get_xlim()  
#  
#    if t >= xmax:  
#        ax.set_xlim(xmin, 2*xmax)  
#        ax.figure.canvas.draw()  
#    line.set_data(xdata, ydata)  
#  
#    return line,  
#      
# 每隔10秒调用函数run,run的参数为函数data_gen,  
# 表示图形只更新需要绘制的元素  
#ani = animation.FuncAnimation(fig, run, data_gen, blit=True, interval=10,  
#    repeat=False)  
#plt.show()  

