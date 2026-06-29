import zipfile,os

def backuptozip(folder):
    folder=os.path.abspath(folder)
    n=1
    while True:
        file=os.path.basename(folder)+'_'+str(n)+'.zip'
        if not os.path.exists(file):
            break
        n+=1

    print('creating',file)
    z=zipfile.ZipFile(file,'w')
    for foldername,subfolders,filenames in os.walk(folder):
        z.write(foldername)
        for filename in filenames:
            filepath=os.path.join(foldername,filename)
            z.write(filepath)
    z.close()

    print('backup completed')

backuptozip("C:\\Users\\Juvie Leona\\Documents\\pets")