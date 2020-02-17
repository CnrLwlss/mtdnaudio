import numpy as np

def update_w(w0, Fext, cFriction, M, dt):
    return(w0 + (float(Fext - w0*cFriction)/float(M))*dt)

def update_theta(theta0, w0, Fext, cFriction, M, dt):
    return(theta0 + w0*dt - float(Fext - w0*cFriction)/float(M)*(dt**2))

def update(theta0, w0, Fext, cFriction, M, dt):
    w = update_w(w0, Fext, cFriction, M, dt)
    theta = update_theta(theta0, w0, Fext, cFriction, M, dt)
    return((w,theta))

def update_setw(theta0, w, Fext, cFriction, M, dt):
    theta = update_theta(theta0, w, Fext, cFriction, M, dt)
    return(theta)


Fext = 1
cFriction = 1
M = 1
t = 0

Nsamps = 1000
dt = 0.1
res = np.zeros(Nsamps)

w = 0.0
theta = 0.0

for i in range(0,Nsamps):
 x = np.sin(theta)
 res[i] = x
 #print(i,t,w,theta,x)
 t = t+dt
 w,theta = update(theta,w,Fext,cFriction,M,dt)

print(res)



