# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 18:59:43 2023

@author: alanm
"""
import sys
sys.path.append('C:\\Users\\alanm\\OneDrive\\Área de Trabalho\\curso python\\Python na IDE\\Trabalho calNum AV2N2\\Metodos')

import TrapezioSimples as ts
import TrapezioRepetidos as tr
import SimpsonSimples as ss
import SimpsonRepetidos as sr
import time as tm


def opcao1():
    resultado, erro = ts.resultados()
    for i, res in enumerate(resultado):
        print("Resultado {0}: {1:.10f}".format(i + 1, res))

    for i, err in enumerate(erro):
        print("Erro {0}: {1:.10f}".format(i + 1, err))

    tm.sleep(4)  
    
def opcao2():
    resultado, erro = tr.resultados()
    for i, res in enumerate(resultado):
        print("Resultado {0}: {1:.10f}".format(i + 1, res))

    for i, err in enumerate(erro):
        print("Erro {0}: {1:.10f}".format(i + 1, err))

    tm.sleep(4) 
    
def opcao3():
    resultado, erro = ss.resultados()
    for i, res in enumerate(resultado):
        print("Resultado {0}: {1:.10f}".format(i + 1, res))

    for i, err in enumerate(erro):
        print("Erro {0}: {1:.10f}".format(i + 1, err))

    tm.sleep(4) 
    
def opcao4():
    resultado, erro = sr.resultados()
    for i, res in enumerate(resultado):
        print("Resultado {0}: {1:.10f}".format(i + 1, res))

    for i, err in enumerate(erro):
        print("Erro {0}: {1:.10f}".format(i + 1, err))

    tm.sleep(4) 
    
def opcao5():
    # Código para a opção 5 (encerrar o loop)
    print("Encerrando...")
    return True  # Encerra o loop

opcoes = {
    1: opcao1,
    2: opcao2,
    3: opcao3,
    4: opcao4,
    5: opcao5
}

encerrar = False

while not encerrar:
    print("Menu:")
    print("1 - Trapézio Simples")
    print("2 - Trapézio Repetido")
    print("3 - Simpson Simples")
    print("4 - Simpson Repetido")
    print("5. Encerrar")

    escolha = int(input("Selecione uma opção: "))

    if escolha in opcoes:
        funcao = opcoes[escolha]
        encerrar = funcao()
    else:
        print("Opção inválida. Tente novamente.")