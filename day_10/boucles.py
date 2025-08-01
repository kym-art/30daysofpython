# les boucles
for i in range (10):
    print(i)
while i<11:
    print(i)
    i=i+1

n="#"
for i in range(0,8):
    print(f"{i*n}")



for i in range(0,11):
    print(f"{i}*{i}={i*i}")

mylist=['Python', 'Numpy','Pandas','Django', 'Flask']    
for i in mylist:
    print(i)


for i in range(0,101):
    if i %2==0:
        print(i)

somme=0
#### level 2 
for i in range (0,101):
          somme+=i 
print(somme)      

somme2=0
for i in range (0,101):
          if i%2==0:
            somme2+=i 
print(somme)          


###level 3
liste=['banana', 'orange', 'mango', 'lemon'] 
liste1=[]
for i in range(0,len(liste),-1):
     liste1.append(i)
