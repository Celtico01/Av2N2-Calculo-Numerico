# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 16:36:00 2023

@author: alanm
"""
import sys
sys.path.append('C:\\Users\\alanm\\OneDrive\\Área de Trabalho\\curso python\\Python na IDE\\Trabalho calNum AV2N2\\Integral(definição)')

import Integral as itg

def simpsonRepetido(integral, a, b, n):
    h = (b - a) / n  # Tamanho do subintervalo

    # Calcula os termos ímpares
    soma_termos_impares = 0
    for i in range(1, n, 2):
        x_i = a + i * h
        soma_termos_impares += integral(x_i)

    # Calcula os termos pares
    soma_termos_pares = 0
    for i in range(2, n, 2):
        x_i = a + i * h
        soma_termos_pares += integral(x_i)

    # Aplica a fórmula do método de Simpson repetido
    valorItg = h / 3 * (integral(a) + integral(b) + 4 * soma_termos_impares + 2 * soma_termos_pares)
    return valorItg

############################################################################################
#resultado
def resultado():
    resultado = [0] * len(itg.n)
    for i in range(len(itg.n)):
        resultado[i] = simpsonRepetido(itg.Integral, itg.a, itg.b, itg.n[i])
    
    return resultado