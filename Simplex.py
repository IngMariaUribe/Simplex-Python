# -*- coding: utf-8 -*-
"""
Created on Tue May 26 10:28:09 2020

@author: jdros
"""

#Metodo simplex
import numpy as np

def gaus(arreglo,variables,auxiliares, parametros):
    while((arreglo[-1][0:parametros]!=np.zeros(parametros)).all()):
        #Hacer el procedimiento de gauz
        
        
parametros = input("Ingrese la cantidad de variables que tiene la función a maximizar")
print("Tenga en cuenta que por defecto solo se toman valores positivos, por lo que no debe tenerlos en cuenta en el siguiente paso")
restricciones = input("Ingrese la cantidad de restricciones")
matriz = np.zeros((restricciones+1),parametros)
matriz.concatenate(np.identity(restricciones),axis=1)
variables=[]
auxiliares=[]
#Se llena un alista con el nombre de las variables
for i in range(parametros):
    variables.append("X"+str(i+1))
#Se llenan los coeficientes de la función objetivo
for i in range(parametros):
    matriz[-1][i]= print("Ingrese el coeficiente del parametro "+str(i+1)+" de la función objetivo")
#Variables auxiliares
for i in range(restricciones):
    auxiliares.append("S"+str(i+1))
#Se llenan la matriz de restricciones
for i in range(restricciones):
    for j in range(parametros):
        matriz[i][j]= input("Ingrese el coeficiente "+str(j+1)+" de la restricción "+ str(i+1))
#Se hace gauss en la matriz
gaus(matriz, variables, auxiliares, parametros)