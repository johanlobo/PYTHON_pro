def smallest(person1:dict,person2:dict,person3:dict):
    l=[person1,person2,person3]

    name=''
    smallestavg=-4

    for i in l:
       
        for k,v in i.items():
            total=0
            count=0
            if k=='name':
                continue
            else:
                total+=v
                count+=1
            avg=total/count

            if avg>smallestavg:
                smallestavg=avg
                name=i['name']

            return 'smallest average is of '+name+' with average marks:'+str(smallestavg)
        
person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}       
        
z=smallest(person1,person2,person3)
print(z)


            
