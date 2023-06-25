# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 16:35:46 2023

@author: alanm
"""
import sys
sys.path.append('C:\\Users\\alanm\\OneDrive\\Área de Trabalho\\curso python\\Python na IDE\\Trabalho calNum AV2N2\\Integral(definição)')

import Integral as itg

def simpsonSimples(integral, a, b, n):
    h = (b - a) / n  # Tamanho do intervalo
    valorItg = integral(a) + integral(b)  # Inicialização da soma da integral

    for i in range(1, n):
        x = a + i * h

        # Se o índice 'i' é par, o coeficiente é 4
        # Se o índice 'i' é ímpar, o coeficiente é 2
        coeficiente = 4 if i % 2 == 0 else 2

        valorItg += coeficiente * integral(x)

    valorItg *= h / 3  # Multiplica pelo coeficiente final

    erro = abs(itg.r) - abs(valorItg)
    erro = abs(erro)
    
    return valorItg, erro

############################################################################################
#resultado
def resultados():
    resultado = [0] * len(itg.n)
    erro = [0] * len(itg.n)
    for i in range(len(itg.n)):
        resultado[i], erro[i] = simpsonSimples(itg.Integral, itg.a, itg.b, itg.n[i])
    
    return resultado, erro