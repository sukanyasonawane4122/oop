class student():
    pass
s1=student()
print(s1)
print(type(s1))
print(id(s1))



class student():
    print(id(s1))
    s1.name='Jay'
    s1.roll=1
    s1.age=20
    print(f'student name is {s1.name},Roll number is {s1.roll},Age is{s1.age}')



    s2=student()
    print(type(id))
    s2.name='Tom'
    s2.roll=2
    s2.age=22
    print(f'student name is {s2.name},Roll number is {s2.roll},Age is{s2.age}')



class student():
    def __init__(self,nm,rl,age):
        print('we are in student class')
        print(id(self))
        self.name=nm
        self.roll=rl
        self.age=age

print('we are creating object')
s1=student('jay',1,20)
print(id(s1))
print(f'student name is {s1.name},Roll number is {s1.roll},Age is {s1.age}')





