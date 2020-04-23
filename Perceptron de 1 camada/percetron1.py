# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 21:35:43 2020

@author: camil
"""

# define as entradas
entradas = [-1, 7, 5]

# define os pesos
pesos = [0.8, 0.1, 0]


# função soma
def soma(e, p):
    s = 0
    for i in range(3):
        s = s + e[i]*p[i]
    return s


# funcao degrau
def stepFunction(soma):
    if (soma >= 1):
        return 1
    return 0
        
      
s = soma(entradas, pesos)


r = stepFunction(s)