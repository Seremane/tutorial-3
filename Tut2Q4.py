# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 01:30:31 2016

@author: ontibile
"""
import numpy
from matplotlib import pyplot as plt


#the circulant(wrap-around) nature of the dft can sometimes be problematic.
#write a routine to take the convolution of two arrays *without* any danger of
#wrapping around.
#may add zeros to the end of the input arrays

from numpy.fft import fft,ifft

def convwrap(x,y):
    assert(x.size==y.size)
    xx=numpy.zeros(2*x.size)
    xx[0:x.size]=x
    yy=numpy.zeros(2*x.size)
    yy[0:y.size]=y
    xxft=numpy.fft.fft(xx)
    yyft=numpy.fft.fft(yy)
    z=numpy.real(ifft(xxft*yyft))
    return z[0:x.size]

#doubled length arrays with zeros

if __name__=='__main__':
    x=numpy.arange(-20,20,0.1)
    y=numpy.exp(-0.5*x**2/(2**2))
    y=y/y.sum()
    
    yconv=convwrap(y,y)
    plt.plot(x,y)
    plt.plot(x,yconv)
    plt.savefig('wrap_around')
    plt.show()