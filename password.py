z=input('enter the password:')
a=0
while True:
    c=input('repeat password:')
    a+=1
    if a==3:
        print('too many attempts, account locked')
        break
    if c==z:
        print('user account created')
        break
    else:
        print('passwords do not match, try again')
    #here if u enter loy as password and for RP if u give space and write loy it wont match cuz it will take space as a string character too