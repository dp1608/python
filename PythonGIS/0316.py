import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LightSource
from sng_image import IMAGE
import matplotlib.mlab as mlab
import matplotlib as mpl
#DEM data
test = IMAGE()
data = test.read('fdem.tif')
Z = data[0]
Z[Z<0] = Z[Z>0].min()
#Shade from the northwest, with the sun 45 degrees from horizontal
ls = LightSource(azdeg=315, altdeg=45)
cmap = plt.cm.gist_earth
rgb = ls.shade(Z, cmap)
plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
plt.title('dem')
#method 1 - default
# plt.imshow(Z, cmap=plt.cm.terrain )
#method 2
r,c = Z.shape
x,y,dx,dy = data[1][0],data[1][3],data[1][1],data[1][5]
xmin,xmax,ymin,ymax = x,x+c*dx,y+r*dy,y
extent=[xmin, xmax,ymin, ymax]
levels = np.arange(0, int(Z.max()), 200) # Boost the upper limit to avoid truncation errors.
cmap = plt.cm.get_cmap(name='jet') #terrain,gist_earth,ocean,brg,hsv,Dark2,hot,gray
plt.imshow(Z, cmap = cmap, interpolation='none', aspect='equal', \
origin='upper', extent=extent, vmax=Z.max(), vmin=Z.min())
x=np.arange(xmin,xmax,(xmax-xmin)/c)
y=np.arange(ymax, ymin, (ymin- ymax)/r)
X, Y = np.meshgrid(x, y)
# CS = plt.contour(X, Y, Z)
CS = plt.contour(Z, levels, hold='on', colors='k', origin='upper', extent=extent,aspect='equal')
# CS = plt.contour(Z, levels, hold='on', colors='k', origin='image', extent=extent)
plt.clabel(CS, inline=1, fmt='%d', fontsize=10)
plt.plot([xmin,xmax],[ymin,ymax], 'r--',lw=2)
plt.gca().set_aspect(1.0)
#plt.axes().set_aspect(1.0)
plt.xlim(xmin,xmax)
#method 3
# mpl.rcParams['image.cmap'] = 'gist_rainbow'
# plt.set_cmap('gist_rainbow')
# im=plt.imshow(Z)
# plt.colorbar(im, orientation='horizontal')
#
plt.subplot(1,2,2)
ax1 = plt.gca()
ax1.set_title('hillshade')
ax1.imshow(rgb)
#
fig = plt.gcf()
fig.savefig('contour.png',format='png')
plt.savefig('contour_01.png',format='png')
plt.show()