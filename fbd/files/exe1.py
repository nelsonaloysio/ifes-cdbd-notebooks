#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Arquivo exe1.py
Autor: Nelson A. Reis
Descrição: Resolução do Exercício 1 da Unidade 3.
"""

def soma_dois_numeros():
	num1 = float(input('Entre o primeiro numero para soma:\n> '))
	num2 = float(input('Entre o segundo numero para soma:\n> '))
	soma = num1 + num2
	print('num1:',num1,
	      '\nnum2:',num2,
	      '\nsoma:',soma)

if __name__ == '__main__':
    soma_dois_numeros()