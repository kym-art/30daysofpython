age=30
taille=1.77
complexe=2+5j

# 4 scripts de calcul zone de triangle 
base=int(input("entrer la valeur de la base:"))
hauteur=int(input("entrer la valeur de la hauteur:"))
print(f" la zone du triangle est { base*hauteur*0.5  }")

# 5 scripts de calcul perimetre

base=int(input("entrer la valeur de la base :"))
hauteur=int(input("entrer la valeur de la hauteur:"))
print(f" la zone du triangle est { base*hauteur*0.5  }")
# 4 scripts de calcul zone de triangle 
c_a=int(input("entrer la valeur de la c_a :"))
c_b=int(input("entrer la valeur de la c_b :"))
c_c=int(input("entrer la valeur de la c_c:"))
print(f" le perimetre du triangle est { c_a+c_b+c_c }")

# 6 scripts de surface et perimetre d'un rectangle
longeur=int(input("entrer la valeur de la longeur :"))
largeur=int(input("entrer la valeur de la largeur:"))
print(f" la surface rectangle est { longeur*largeur  } \n son perimetre est { 2*(longeur+largeur)}")

# 7 scripts de calcul zone et de la circonference d'un cercle 
pi=3.14
rayon=int(input("entrer la valeur du rayon :"))
print(f" la zone du cercle est { pi*rayon*rayon } \n sa circonference est {2*pi*rayon}")



# 12  
len_python=len("python")
len_dragon=len("dragon")

print(len_python < len_dragon)
# 13
print( "on" in "python" and "on" in "dragon")
#14
print( "jargon" in " i hope this course is not full of jargon")
#15

# 16 j'ai deja une variable qui stock la longeur de python donc je l'utilise pour cette question
# il s'agit de la variables len_python
float_python=float(len_python)
chaines_python=str(len_python)

# 17 cette verification peut se faire tres rapidement en utilisant  la division % 
nonbre=int(input("entrer le nonbre 1 : "))

# l'instruction suivante renvoie True si le nombre est divisible par 2 et False au cas echeant
print( nonbre%2==0 )

# 18 
print( 7//3 == int(2.7))

# 19 
print( type('10')==type(10))

# 20 
print( int(90.8) == 10)


# 21 scripts de cacul de rrenumeration
nombre_heures=int(input("entrer votre nombre d'heure par semaine : "))
tarif=int(input("entrer votre renumeration par heure  "))

print(f" votre gain hebdomendaire est { nombre_heures*tarif}")

# 22 scripts de vie en seconde 
annee=int(input("entrer le nombres d'annee que vous avez vecu "))
print ( f"vous vivez pendant { annee*365*24*60*60}")

# 23 
print( "1 1 1 1 1 \n2 1 2 4 8\n3 1 3 9 27\n4 1 4 16 64\n5 1 5 25 125")