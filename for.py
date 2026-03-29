p=input('enter a string:')
for i in p:
    print(i)
    print('*')

for i in range(5):
    print(i)
print()
for i in range (3,7):
    print(i)
print()
for i in range(1,10,2):
    print(i)  #adds 2 to the previous number. also u can write -ve integers to subtract ex:(7,-4,-3) output: 4, 1, -2
print()
z=int(input('please enter a positive integer:'))
for i in range(-z,z+1):
    print(i)