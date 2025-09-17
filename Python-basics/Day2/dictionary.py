# Dictionary

chai_types={"Masala":"Spicy" ,"Ginger":"Zesty","Green":"Mild"}

print(chai_types)

print(chai_types['Masala'])
print(chai_types.get("masala"))
print(chai_types.get("Masala"))

chai_types["Green"]="Fresh"
print(chai_types)


for chai in chai_types:
    print(chai)
    # returns key 
    
for chai in chai_types:
    print(chai, chai_types[chai])
    
for key,values in chai_types.items():
    print(key,values)


if "masala" in chai_types:
    print("We have it")
else:
    print("We dont have it ")

chai_types["Earl Grey"]="Citrus"

print(chai_types)

print(chai_types.pop("Masala"))
print(chai_types)


print(chai_types.popitem())
print(chai_types)


del chai_types["Green"]
print(chai_types)

# dict comphrensions

squared_nums={x:x*2 for  x in range(10)}
print(squared_nums)

squared_nums.clear()
print(squared_nums)


keys=["Masala","Ginger","Lemon"]
default_value="Delicious"
new_dict=dict.fromkeys(keys,default_value)
print(new_dict)
new_dict=dict.fromkeys(keys,keys)
print(new_dict)