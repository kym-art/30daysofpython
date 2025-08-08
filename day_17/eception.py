names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
nordic_countrie,store,russie,estonie,*RU= names
print(RU)

mylist=[2,5,8,47,7]
print(*mylist)


a=int(input("entrer un nombres :"))
b=int(input("entrer un nombres :"))

try:
    exposant=a**b
except:
    multiplie=a*b    
else:
    soostration=a-b    