import os  
for folderName, subfolders, filenames in os.walk("C:\\Users\\Juvie Leona\\Documents\\delicious"):  
    print('The current folder is ' + folderName)  
    for subfolder in subfolders:  
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)  
    for filename in filenames:  
        print('FILE INSIDE ' + folderName + ': '+ filename)  
print(' ') 


#here lists are automatically made for folder,subfolders,filenames