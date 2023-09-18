"""
Fecha: 18/09/2023
Autor: Mayra Alejandra Franco Castaño
Objetivo: Ejemplo de versionamiento con git desde python
"""
import random

print("Número aleatorio entre 1 y 10")

random_number = random.randint(1, 10) #Genera núms aleatorios entre un rango
print(random_number)

print("-----------------------------------")

for i in range(0, 10) :
    random_number = random.randrange(20, 100, 5) #Genera núms aleatorios entre un rango multiplos de 5
    print(random_number)

print("-----------------------------------")

for i in range(0, 10) :
    random_number = random.random() #Genera núms aleatorios con decimales
    print(random_number)

print("-----------------------------------")

for i in range(0, 10) :
    random_number = random.uniform(10.5, 20.6) #Genera núms aleatorios partiendo de decimales
    print(random_number)

print("-----------------------------------")