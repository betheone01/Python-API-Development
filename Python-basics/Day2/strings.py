'''
'''

chai ="lemon chai"
print(chai)
print(chai[0])

slice_chai=chai[0:5]
print(slice_chai)

num_list="0123456789"
print(num_list[:])
print(num_list[:7])
print(" ",num_list[0:7:2])
print(num_list[0:7:-2])


print(chai.lower())
print(chai.upper())
print(chai.strip())  
# Removes extra space 

print(chai.replace("lemon","ginger"))
print(chai)

chai="Lemon, Ginger, Masala, Mint"
print(chai.split(", "))

chai="Masala Chai"
print(chai.find("Chai"))
print(chai.find("chai")) 
# -1

chai="Masala chai chai chai"
print(chai.count("chai"))

# order formatting 

order ="I ordered {} cups of {} chai"
print(order.format(2,"Masala"))

# list to string 
myList=["Lemon","Masala","Ginger"]
print("".join(myList))
print(" ".join(myList))


#len 
print(len(chai))

# 
for letter in chai:
    print(letter)


# chai="Hello , "what are you doing"
chai="Hello , \"what are you doing\""
print(chai)

