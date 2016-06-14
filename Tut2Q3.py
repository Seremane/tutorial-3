# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 01:27:02 2016

@author: ontibile
"""
import numpy
from matplotlib import pyplot as plt

#using the results of part1 and part2, write a routine to take the correlation function
#of a guassian(shifted by an arbitrary amount) with itself.
#how does the correlation function depend on the shift?
#is it surpring??

from numpy.fft import fft,ifft

#from question 1:
def myshift(x,n=0):
    nvec=0*x #starts at zeros array
    nvec[n]=1
    nvecft=numpy.fft.fft(nvec)
    xft=numpy.fft.fft(x)
    return numpy.real(ifft(nvecft*xft))

#from question 2:   
def mycorr(x,y):
    assert(x.size==y.size) 
    #vectors made equal for simplicity
    
    ft1=fft(x)
    ft2=fft(y)
    ft2conj=numpy.conj(ft2)
    return numpy.real(ifft(ft1*ft2conj))

if __name__=='__main__':
        x=numpy.arange(-20,20,0.1)
        y=numpy.exp(-0.5*x**2/(2**2))
        
        ycorr=mycorr(y,y)
        yshift=myshift(y,y.size/4)
        yshiftcorr=mycorr(yshift,yshift)
        meanerr=numpy.mean(numpy.abs(ycorr-yshiftcorr)) #meanerr is mean error
        print 'mean difference is ' + repr(meanerr)
        plt.plot(x,ycorr)
        plt.plot(x,yshiftcorr)        
        plt.show()
        
        
        