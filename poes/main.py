import numpy as np
from poes.model.poes import poes
#Asignando arreglos para las variables

area = np.array([100,150,163])
h = np.array([30,40,13])
poro = np.array([0.16,0.18,0.24])
swi = np.array([0.50,0.69,0.71])
boi = np.array([1,1.01,1.2])
print(area)
#Imprimimos el area para ver el arreglo, y a continuación se imrpime el resultado de la funcion poes
print(poes(area,h,poro,swi,boi))
    #hi
