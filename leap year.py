y=int(input('enter the year:'))

if y%4==0 and y%100!=0 or y%400==0:
        print('leap year')
        
else:
       while True:
            y+=1
            if y%4==0 and y%100!=0 or y%400==0:
                print('not a leap year, the next leap year is:',y)
                
                break          
        


    #u can use 2 loops also and make it nested. but will have to use 2 break stmts
    


        