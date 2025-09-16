username="betheone01"
print(len(username))

# username[0]="A"
# TypeError: 'str' object does not support item assignment
# Becuase string is immutable

username[-1] 

print(username[1:4])


dir(username)

myList=[123, "hello" ,3.14]
print(myList)
print(len(myList))


myDict= {"one":1 ,"two":2}
print(myDict.get("one"))
print(myDict["one"])
# myDict.add("three":3)


myTuples=(1,2,3.14)
print(myTuples[1])