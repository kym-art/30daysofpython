it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
# ## level 1
len(it_companies)
it_companies.add("twitter")
it_companies.update(["alibaba", "meta","leakdin","spacex" ])
it_companies.remove("Facebook")

### la difference entre remove et discard consiste dans le fait que remove()
#  genere une erreur si l'elment a supprimer n'existe pas alors que pour discard 
# l'instruction est tout simplement ignoré


### level 2
new_set= A.union(B)
new_set2=A.intersection(B)
print(A.issubset(B))
print(A.isdisjoint(B))

new_set3=A.symmetric_difference(B)
print(new_set3)

del new_set3
del new_set2
del new_set



### level 3
set_list=set(age)

print(len(set_list)== len(age))
print(len(set_list)< len(age))
print(set_list)



string="i am teacher and i love to inspire and teach people. "
unique_word=set(string.split())
print(unique_word)