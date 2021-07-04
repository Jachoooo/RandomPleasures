import numpy as np
from numpy.lib.function_base import average
from numpy.random import default_rng
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.animation import PillowWriter
from math import floor
import time


NUM_OF_SIGNALS=20
DIST=4
SPEED=5
ANIMATE=True
PLOT=True

def normal_dist(x , mean , sd):
    prob_density = (np.pi*sd) * np.exp(-0.5*((x-mean)/sd)**2)
    return prob_density

def random_signal():
    mean=rng.random()*0.3-0.30
    sd=rng.random()*0.01+0.05
    scale=rng.random()*0.2+2
    x = np.linspace(-1,1,200)
    A = normal_dist(x,mean,sd)*scale

    mean=rng.random()*0.1+0.1
    sd=rng.random()*0.1+0.1
    scale=rng.random()*0.1+0.2
    x = np.linspace(-1,1,200)
    B = normal_dist(x,mean,sd)*scale

    mean=rng.random()*0.4+0.1
    sd=rng.random()*0.01+0.02
    scale=rng.random()*5
    x = np.linspace(-1,1,200)
    C = normal_dist(x,mean,sd)*scale

    rand=rng.standard_normal(200)*0.01
    
    return A+B+C+rand




rng=default_rng()

signals=np.empty([NUM_OF_SIGNALS,200])
for i in range(0,NUM_OF_SIGNALS):
    signals[i,:]=random_signal()+i*DIST/NUM_OF_SIGNALS


    
signals=signals.transpose()


for n in range(0,signals.shape[0]):
    temp=0
    for i in range(0,signals.shape[1]):
        if signals[n,i]>=temp+0.02:
            temp=signals[n,i]
        else:
            signals[n,i]=temp


fig, ax = plt.subplots(1,1, figsize=(10,10),facecolor='black')

ln1 = plt.plot([])
ax.set_facecolor("black")
plt.yticks([])
plt.xticks([])
plt.xlim((-100,300))
plt.ylim((-1,DIST+1))

def animate(i):
    global T0
    i+=1
    i*=SPEED
    S=floor(i/200)
    #if S!=0: plt.plot(signals[:,0:S],'w')
    try:
        
        plt.plot(signals[0:i%200,S],'w')
    except:
        ''
        
    if not i%(200*NUM_OF_SIGNALS/10): 
        print('\t',floor(i/(2*NUM_OF_SIGNALS)),"%\t T%=",time.thread_time()-T0,'s')
        T0=time.thread_time()

if ANIMATE:    
    global T0
    T0=time.thread_time()
    start=time.thread_time()
    ani = animation.FuncAnimation(fig, animate, frames=200*round(NUM_OF_SIGNALS/SPEED) )
    ani.save('ani.gif',writer='pillow',fps=50,dpi=100)
    print("DONE\t 100 %\tTotal render time =",time.thread_time()-start,'s')


if PLOT:
    fig, ax = plt.subplots(1,1, figsize=(10,10),facecolor='black')

    ln1 = plt.plot([])
    ax.set_facecolor("black")
    plt.yticks([])
    plt.xticks([])
    plt.xlim((-100,300))
    plt.ylim((-1,DIST+1))
    plt.plot(signals,'w')
    plt.savefig('plot.png',dpi=1200,format='png')
