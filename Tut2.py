# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 21:56:36 2016

@author: ontibile
"""

import numpy
from matplotlib import pyplot as plt

#Question 1:
#write a function that will shift an array by an arbitrary amount using a convolution
#this funtion should take 2 arguments ie an array, and an amount by which to shift the array
#plot a guassian that started in the centre of the array shifted by half the array length
from numpy.fft import ifft

def myshift(x,n=0):
    nvec=0*x #starts at zeros array
    nvec[n]=1
    nvecft=numpy.fft.fft(nvec)
    xft=numpy.fft.fft(x)
    return numpy.real(ifft(nvecft*xft))
    
if __name__=='__main__':
    x=numpy.arange(-20,20,0.1)
    y=numpy.exp(-0.5*x**2/(2**2))
    yshift=myshift(y,y.size/2)

    plt.plot(x,y)
    plt.plot(x,yshift)
    plt.savefig('shift_array')
    plt.show()





