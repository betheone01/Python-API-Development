username='mayur'
username='chai aur code'
# but string is immutable but still username we are getting chai aur code as output
print(username)

# so basically we cant change the reference of the value 
#  it wont change the actual memory reference


# What Happenend :
# username first pointing to mayur 
# then username pointed to chai aur code so it made mayur as non reference object which will further taken by garbage collection .


x=10
y=x 
print(x)
print(y)
x=15
print(x)
print(y)
