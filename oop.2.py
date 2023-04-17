class employee():
    pass
e1=employee()
print(e1)
print(type(e1))
print(id(e1))


class employee():
    print(id(e1))
    e1.name='Ankita'
    e1.adress='Pune'
    e1.gender='Female'
    print(f'employees name is {e1.name},Adress is {e1.adress},Gender is {e1.gender}')



class employee():
    def __init__(a,name,adress,gender):
        print('Im an employee')
        print(id(a))
        a.name=name
        a.adress=adress
        a.gender=gender
        print('Im an employee who is doing work in IT company')
        e1=employee('Ankita','Pune','Female')
        print(id(e1))
        print(f'employee name is {e1.name},Adress is {e1.adress},Gender is {e1.gender}')




