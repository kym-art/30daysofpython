empty_tuple=()
mytuple1=("adjo","afi","carmelle","emmanuella")
mytuple2=("kodjo","gerard","benjamin")

sublings=mytuple1+mytuple2
len(sublings)

family_menbers=sublings+("papa", "maman")

### 2 level

fruits=("banane","orange","citron")
vegetale=("jfchfj","jedgdgdj","hdghdhdj")
animal=("chien","canard","leopard")

food_stupp=fruits+animal+vegetale
food_list=list(food_stupp)

food_stupp[0:2]
food_stupp[len(food_stupp)-3:len(food_stupp)-1]

del(food_stupp)
print(food_stupp)
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway','Sweden')


print("Estonia" in nordic_countries )
print("iceland" in nordic_countries )