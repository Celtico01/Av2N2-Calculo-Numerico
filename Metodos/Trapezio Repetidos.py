# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 16:35:30 2023

@author: alanm
"""
import sys
sys.path.append('C:\\Users\\alanm\\OneDrive\\Área de Trabalho\\curso python\\Python na IDE\\Trabalho calNum AV2N2\\Integral(definição)')

import Integral as itg

def trapezioRepetido(integral, a, b, n):
    h = (b - a) / n
    valorItg = 0

    for i in range(n):
        x1 = a + i * h
        x2 = a + (i + 1) * h
        valorItg += (integral(x1) + 4 * integral((x1 + x2) / 2) + integral(x2)) * h / 6

    return valorItg

resultado = [0] * len(itg.n)
for i in range(len(itg.n)):
    resultado[i] = trapezioRepetido(itg.Integral, itg.a, itg.b, itg.n[i])

#exibindo
for i, res in enumerate(resultado):
    print(f"Resultado {i + 1}: {res}")