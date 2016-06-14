# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 01:10:03 2016

@author: ontibile
"""

import numpy
from matplotlib import pyplot as plt

#the correlaltion function f*g=int(f(x)*g(x+y)).it can be proved that 
################f*g=ifft(dft(f)*conj(dft(g)))######################
#write a routine to take the correlation function of two arrays
#plot the correlation function of the gaussian with itself

from numpy.fft import fft,ifft


def mycorr(x,y):
    assert(x.size==y.size)  
    ft1=fft(x)
    ft2=fft(y)
    ft2conj=numpy.conj(ft2)
    return numpy.real(ifft(ft1*ft2conj))

if __name__=='__main__':
        x=numpy.arange(-20,20,0.1)
        y=numpy.exp(-0.5*x**2/(2**2))
        
        ycorr=mycorr(y,y)
        plt.plot(x,ycorr)
        plt.savefig('correlation_fit')
        plt.show()

