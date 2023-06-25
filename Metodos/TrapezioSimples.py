# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 16:35:18 2023

@author: alanm
"""
import sys
sys.path.append('C:\\Users\\alanm\\OneDrive\\Área de Trabalho\\curso python\\Python na IDE\\Trabalho calNum AV2N2\\Integral(definição)')

import Integral as itg

def trapezioSimples(integral, a, b, n):
    h = (b - a) / n # Tamanho do intervalo
    
    valorItg = 0.5 * (integral(a) + integral(b))
    
    for i in range(1, n):
        x = a + i * h
        valorItg += integral(x)
        
    valorItg *= h
    
    return valorItg

############################################################################################
#resultado
def resultado():
    resultado = [0] * len(itg.n)
    for i in range(len(itg.n)):
        resultado[i] = trapezioSimples(itg.Integral, itg.a, itg.b, itg.n[i])
    
    return resultado



    
