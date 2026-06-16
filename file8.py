infile=open(r"C:\Users\Juvie Leona\Documents\infile.txt")
outfile=open(r"C:\Users\Juvie Leona\Documents\outfile.txt",'w')

for i in infile.readlines():
    w=i.split()
    w.sort(key=str.lower)
    s=' '.join(w)
    outfile.write(s+'\n')

infile.close()
outfile.close()