a = 99
while a>=1:
    print(a)
    a-=2
    
# While Bertingkat 
a = 1
while a <=10:
    b = 1
    while b<=10:
        print(a*b, end=" ")
        b+=1
    print()
    a+=1

# Range
for i in range(50):
    print(i)
    
for i in range(0,31,3):
    print (i, end=" ")

for i in range(5,55,5):
    print(i)
    
for i in range(50,0,-5):
    print(i, end=" ")
    
for TI03 in range(3):
    print("TI03")
    
# For bertingkat
for i in range(1,11):
    for j in range(1,11):
        k = i*j
    print (k, end=' ')
print()
 
# break statement  
a = 1
while a<6:
    print(a)
    if a==3:
        break
    a+=1
    
# continue statement
i = 0
while i <6:
    i +=1
    if i==3:
        continue
    print(i)