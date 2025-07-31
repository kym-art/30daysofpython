age=int(input("entrer votre age"))
if age>18:
    print("vous etes assez vieux pour conduire!")
else:
    print(f"attends encore {18-age} ans ")


myage=19
if age>myage:
    print(f" vous avez {myage-age} de plus que moi !")
elif age==myage:
    print("nous avons les memes ages !")
else:
    print("je suis plus age que toi!")

a=int(input("entrer un nombres"))            
b=int(input("entrer un nombres"))      
if a>b:
    print(b)
else:
    print(a)          


note=int(input("entrer votre note de classe"))
if 80<note<100:
    print("vous avez un A")   
elif 70<note<79 :   
    print("vous avez un B")    
elif 60<note<69 :   
    print("vous avez un C")    
elif 50<note<59:     
    print("vous avez un D")    
else:     
    print("vous avez un E ")    



fruits = ['banana', 'orange', 'mango', 'lemon']
fruit=input("entrer un fruit")
if fruit in fruits:
    print("ce fruit existe deja dans le liste")
    print(fruits)
else:
    fruits.append(fruit)   
    print(fruits)


personne = {'premier_name': 'asabeneh', 'last_name': 'yetayeh', 'age': 250, 'country': 'Finland', 'is_marred': True, 'competences': 'javascript', 'Zipcode': '02210'}

a=personne['competences']
print(a)