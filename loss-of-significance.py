# -*- coding: utf-8 -*-
"""
Created on Sun Aug 04 19:18:02 2019

@author: Andrés Vera
"""

import scipy as sp
from matplotlib import pyplot
import matplotlib.pylab as plt
from numpy import *
#numeros a usar
nros = [2 , 5 , 10]

#raices de los numeros usados
raicesreales = [ 1.414213562 , 2.236067978 , 3.16227766]

#raices con float32
float32 = []
for i in nros:
    m = sp.float32(sqrt(i))
    float32.append(m)
    
#raices con float64
float64 = []
for i in nros:
    n = sp.float64(sqrt(i))
    float64.append(n)
    
#calculo de errores    
error32 = []
i= 0 
T = 3
while i < T:
        error = abs((float32[i] - raicesreales[i])/raicesreales[i])
        error32.append(error)      
        i += 1 
i = 0         
error64 = []
while i < T:
        error = abs((float64[i] - raicesreales[i])/raicesreales[i])
        error64.append(error)
        i += 1 
        
print "valores exactos:", raicesreales
print "valores float32" , float32
print "error de float32", error32
print "valors float64", float64
print "error de float64", error64

#grafico de comparacion
plt.figure(1)
plt.plot(raicesreales, error32, label="Error float 32" )
plt.plot(raicesreales, error64, label="Error float 64" )


plt.xlabel("valores")
plt.ylabel("Error Relativo")
plt.grid(True)

plt.title("Perdida de significancia en raiz cuadratica")
plt.legend(["error float32", "error float64"])
plt.savefig("loss-of-significance.png")

plt.show()


