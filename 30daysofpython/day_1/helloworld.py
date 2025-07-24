
#exercice niveau 3
from math import sqrt
# 1- les different types de donnees 
myentier=5 
myfloat=1.2
mystring="bonjour"
myboolean=True
mylist=[1,5,1,7,71,81,4,7,55,14,45,4,1,4,44,4]
mytuple=(1,5,1,7,28,8)
myset={"crayon","bic","regle"}
mydictionnary={"Q":"Qui etait le leader de la revolution algerienne?","a":"a:Ahmed Ben Bella","b":"b:Houari Boumediene","c":"c:Ferhat Abbas","rep":"a"}

# 2-distance euclidienne entre ( 2,3) et (10,8)
"""
il  s'agira essentiellement de calculer la distance entre 
les deux points en utilisant la fonction sqrt de math
"""
distance =sqrt((10-2)**2 + (8-3)**2 )
print(f"{ distance:.2f}")