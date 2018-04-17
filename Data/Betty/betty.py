import numpy as np

bias = 0.5

x,y,z = 128,32,64

A = np.fromfile('betty.raw', dtype='uint8', sep="")
A = A.reshape([x,y,z,3])

A = A/255 - bias

x_vec = A[:,:,:,0]
y_vec = A[:,:,:,1]
z_vec = A[:,:,:,2]

x_vec = x_vec.flatten()
y_vec = y_vec.flatten()
z_vec = z_vec.flatten()

xv = np.linspace(0,x-1,x)
yv = np.linspace(0,y-1,y)
zv = np.linspace(0,z-1,z)

x_i, y_i, z_i = np.meshgrid(xv,yv,zv)

x = x_i.flatten()
y = y_i.flatten()
z = z_i.flatten()

data = []

data.append(x_vec)
data.append(y_vec)
data.append(z_vec)
data.append(x)
data.append(y)
data.append(z)
data = np.asarray(data).T

np.savetxt('data.csv',data, delimiter = ',',
           header = 'x_vec,y_vec,z_vec,ix,iy,iz',
           comments = '')