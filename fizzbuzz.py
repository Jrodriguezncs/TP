
"""Programa ...."""

#Este programa llamado fissbuzz es un clasico de una evaluacion de programacion
#El programa muestra FIZZ si es multiplo de 3
#El programa muestra BUZZ si es multiplo de 5
#El programa muestra el numero si no es multiplo de 3 o de 5
#El programa muestra FIZZ BUZZ si es multiplo de 3 y de 5 al mismo tiempo

# Pseudocodigo:

#Repito del 1 al 100, comenzando del 1. Si el nro es multiplo de 3, esto es cuando divido este nro por 3 y el resto es 0. Entonces muestro la palabra FIZZ, sino, si es multiplo de 5, o sea, al dividir ese nro por 5 el resto debe ser 0. Sino, 


a=1
while a<=100 :
    
    if a%3==0 and a%5==0 :
        print ("FIZZBUZZ")
    
    elif a%3==0 :
        print ("FIZZ")
    
    elif a%5==0 :
        print ("BUZZ")
    
    else: 
        print a
    
    a=a+1