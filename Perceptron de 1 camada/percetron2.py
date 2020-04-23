# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 21:47:54 2020

@author: camil
"""


import numpy as np

# define as entradas
entradas = np.array([-1, 7, 5])

#define pesos
pesos = np.array([0.8, 0.1, 0])


# função soma
def soma(e, p):
   return e.dot(p)
    # Produto escalar


# funcao degrau
def stepFunction(soma):
    if (soma >= 1):
        return 1
    return 0
        

s = soma(entradas, pesos)


r = stepFunction(s)