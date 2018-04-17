import numpy as np

###############################################################################
'''Functions'''
###############################################################################

def gen_Sally(xs,ys,zs,time=1.0):

    r2 = 8
    SMALL = 0.00000000001
    xdelta = 1.0 / (xs-1.0)
    ydelta = 1.0 / (ys-1.0)
    zdelta = 1.0 / (zs-1.0)
    
    ix_values = []
    iy_values = []
    iz_values = []

    x_vec = []
    y_vec = []
    z_vec = []
    
    data = []

    for iz in range(0,int(zs)):
        # map z to 0->1
        z = iz * zdelta
        # For each z-slice, determine the spiral circle
        xc = 0.5 + 0.1*np.sin(0.04*time+10.0*z)
        #(xc,yc) determine the center of the circle.
        yc = 0.5 + 0.1*np.cos(0.03*time+3.0*z)
        #The radius also changes at each z-slice.
        r = 0.1 + 0.4 * z*z + 0.1 * z * np.sin(8.0*z)
        r2 = 0.2 + 0.1*z

        for iy in range(0,int(ys)):
            y = iy * ydelta
            
            for ix in range(0,int(xs)):
                x = ix * xdelta
                temp = np.sqrt( (y-yc)*(y-yc) + (x-xc)*(x-xc) )
                scale = np.fabs( r - temp )
                if ( scale > r2 ):
                    scale = 0.8 - scale
                else:
                    scale = 1.0
                z0 = 0.1 * (0.1 - temp*z )
                if ( z0 < 0.0 ):
                    z0 = 0.0
                temp = np.sqrt( temp*temp + z0*z0 )
                scale = (r + r2 - temp) * scale / (temp + SMALL)
                scale = scale / (1+z)
                xi = scale * (y-yc) + 0.1*(x-xc)
                yi = scale * -(x-xc) + 0.1*(y-yc)
                zi = scale * z0
                x_vec.append(xi)
                y_vec.append(yi)
                z_vec.append(zi)
                ix_values.append(ix)
                iy_values.append(iy)
                iz_values.append(iz)
                
    data.append(x_vec)
    data.append(y_vec)
    data.append(z_vec)
    data.append(ix_values)
    data.append(iy_values)
    data.append(iz_values)
    data = np.asarray(data)

    return data.T

###############################################################################
    
def animate_Sally(xs,ys,zs,time,steps):
    
    c = 0
    
    for t in np.linspace(0,time,steps):
        data = gen_Sally(xs,ys,zs, t)
        np.savetxt('Time/data.csv.'+str(c),data, delimiter = ',',
           header = 'x_vec,y_vec,z_vec,ix,iy,iz',
           comments = '')
        c+=1
        print('%.2f' %((c/steps)*100) + '%')
        
###############################################################################
'''Implementation'''
###############################################################################

xs,ys,zs = 20,20,20

time = 1000
steps = 1000

animate_Sally(xs,ys,zs,time,steps)
