import zipfile,os
def backup(folder):
    folder=os.path.abspath(folder)
    number=1
    while True:
        file=os.path.basename(folder)+'_'+str(number)+'.zip'
        
        if not os.path.exists(file):
            break
        number+=1

    print('creating:',file)
    z=zipfile.ZipFile(file,'w')
    for fn,sf,fnms in os.walk(folder):
        z.write(fn)
        for filename in fnms:
            filepath=os.path.join(fn,filename)
            z.write(filepath)
            z.close()
    print('backup completed')

backup('C:\\lobo')