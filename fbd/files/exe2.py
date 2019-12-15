#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Arquivo exe2.py
Autor: Nelson A. Reis
Descrição: Resolução do Exercício 2 da Unidade 3.
"""

from math import pi

def circulo_perimetro_area():
	raio = float(input('Entre o raio de um circulo:\n> '))
	perimetro = float(2 * pi * raio)
	area = float(pi * (raio ** 2))
	print('raio:',raio,
	      '\nperimetro:',perimetro,
	      '\narea:',area)

if __name__ == '__main__':
    circulo_perimetro_area()