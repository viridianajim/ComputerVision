from PIL import Image
from pylab import *
#import os
#pil_im = Image.open('fruitas.jpg').convert('L')

'''
#converts all the picture in the file as jps
for infile in filelist:
    outfile = os.path.splitext(infile)[0]+".jpg"
    if infle != otule:
        try:
            Image.open(infile).save(outfile)
        except IOError:
            print("cannot convert", infile)
'''
#read imget to array
im = array(Image.open('fruitas.jpg'))

#plot the image
imshow(im)

#some points
x=[100, 100, 400, 400]
y=[200, 500, 200, 500]

#plot the points with red star-makers
plot(x, y, 'm+')

#line plot connecting the first two points
plot(x[:2], y[:2])

#add title and show the plot
title('Plotting: "fruitas.jpg"')
show()
