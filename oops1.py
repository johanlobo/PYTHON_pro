class student:
    def __init__(self,n,u):
        self.name=n
        self.usn=u
        self.marks=[]

    def entermarks(self):
        total=0
        for i in range(3):
            print('enter the marks of the subject',i+1,':')
            m=int(input())

            self.marks.append(m)
            total+=m
        self.marks.append(total)
        self.marks.append(total/3)

    def display(self):
        print('SCORE CARD OF STUDENT'+'\n')
        print('NAME:',self.name.upper())
        print('USN:',self.usn.upper())
        for i in range(3):
            print('marks of subject',i+1,':',self.marks[i])
        print('total marks:',self.marks[3])
        print('percentage:',self.marks[4])

n=input('enter the name of the student:')
u=input('enter the usn of the student:')
s1=student(n,u)
s1.entermarks()
s1.display()


        