# List (Array)

my_chai=['Black',"Green","Oolong"]
print(my_chai)
print(my_chai[-1])
# slicing works same as strings

for i in my_chai:
    print("chai are",i)
    
    

for i in my_chai:
    print("chai is",i,end=" - ")
    
my_chai.append("White")
print(my_chai)

if "Oolong" in my_chai:
    print("We have Oolong tea")
    
my_chai.pop()
# returns the last item
print(my_chai)

my_chai.remove("Oolong")
# didnt return anything
print(my_chai)


my_chai=['Black',"Green","Oolong"]

my_chai.insert(1,"White")
print(my_chai)

my_chai_copy=my_chai.copy()
# different references  
print(my_chai_copy)


# List comphrensions
squqared_nums=[x**2 for x in range(10)]
print(squqared_nums)