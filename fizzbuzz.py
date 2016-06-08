#! /usr/bin/env python
# coding: utf-8
"Programa FIZZBUZZ - Version 1"
author = "Javier A. Rodriguez (jrodriguezncs@gmail.com)"
copyright = "Copyright (C) 2016 Javier A. Rodriguez"
license = "GLP 3.0"
version = "1.0.0"

#Este programa es parte de una evaluacion de programacion
#El programa muestra FIZZ si es multiplo de 3
#Muestra BUZZ si es multiplo de 5
#Muestra el numero si no es multiplo de 3 o de 5
#Muestra FIZZ BUZZ si es multiplo de 3 y de 5 al mismo tiempo

# Pseudocodigo:
#Repito del 1 al 100, comenzando del 1/s
#Si el nro es multiplo de 3, esto es cuando divido por 3 y el resto 0#
#Entonces muestro la palabra FIZZ#
#Sino, si es multiplo de 5, o sea, al dividir ese nro por 5 el resto 0.
#Muestro la palabra BUZZ/s
#Si es multiplo de 3 y de 5 al mismo tiempo, muestro FIZZBUZZ.
#Sino muestro el numero


a = 1
while a <= 100:
    if a % 3 == 0 and a % 5 == 0:
        print ("FIZZBUZZ")
    elif a % 3 == 0:
        print ("FIZZ")
    elif a % 5 == 0:
        print ("BUZZ")
    else:
        print a
    a = a+1
