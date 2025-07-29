# 
mylist=[]
mylist1=[1, 2, 3, 4, 5,6, 7, 8, 9, 10]
print(  len(mylist1))

print(mylist1[0],mylist1[len(mylist1)//2],mylist1[len(mylist1)-1])
mixed_data_types=[ "KODJO", 30 , 1.70,"celibataire"]
it_compagny=["Facebook"," Google", "Microsoft","Apple", "IBM", "Oracle"  "Amazon."]
print(it_compagny)
print(it_compagny[0],it_compagny[len(it_compagny)//2],it_compagny[len(it_compagny)-1])
it_compagny[2]="alibaba"
print(it_compagny)

it_compagny.append("IT")
it_compagny.insert( len(it_compagny)//2 , "IT")
print(it_compagny)

it_compagny[3]=it_compagny[3].lower()
print(it_compagny)

print("#".join(it_compagny))

print("banane " in it_compagny)
print("Google " in it_compagny)
print("Apple" in it_compagny)

it_compagny.sort()

it_compagny.reverse()
print(it_compagny)
print(it_compagny.remove("Facebook"))
(it_compagny.remove(it_compagny[2]))
(it_compagny.remove(it_compagny[0]))
print(it_compagny)


front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

stack=front_end.copy()
stack.extend(back_end)
print(stack)

stack.append("python")
stack.append("SQL")

## level 2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages1=ages.copy()
ages1.sort()

ages1.append( 19)
ages1.append( 26)