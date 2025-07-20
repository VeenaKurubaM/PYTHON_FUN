""" for loop"""
for x in range(1,11):
    
    print(x)
    
print("For loop 1 to 10")

""" for loop reverse"""
for x in reversed(range(1,11)):
    print(x)
print("Reverse from 10 to 1")

"""for loop using step"""
for x in range(1,11,2):
    print(x)
print("1 to 10 pinting every alternate number")

"""for loop sting"""
say_hello=input("enter firstname: ")
for x in say_hello:
    print(x)
    
"""reverse string"""
say_hello=input("enter firstname: ")
for x in say_hello[::-1]:
    print(x)
    
"""for loop in skipping one number"""
for x in range(1,21):
    if x==13:
        continue
    else:
        print(x)
"""for loop to break at 13"""
for x in range(1,21):
    if x==13:
        break
    else:
        print(x)
    