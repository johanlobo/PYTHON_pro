infile=open('c:\\loy.txt')
outfile=open('c:\\lobo.txt','w')

for i in infile.readlines():
    w=i.split()
    w.sort(key=str.lower)
    s=' '.join(w)
    outfile.write(s+'\n')

infile.close()
outfile.close()