class Employee:
    def __init__(self,eid,ename,edesig,email,esal,):
        self.eid=eid
        self.ename=ename
        self.edesig=edesig
        self.email=email
        self.esal=esal
    def print(self):
        print(self.eid,",",self.ename,",",self.edesig,",",self.email)
f=open("employee")
employee=[]
for data in f:
    print(data)
    employees=data.rstrip("/n").split(",")
    eid=employees[0]
    ename=employees[1]
    edesig=employees[2]
    esal=employees[3]
    email=employees[4]
    ob=Employee(eid,ename,edesig,email,esal)
    employee.append(ob)
for employee in employee:
    esal=employee.esal
    print(maxesal.esal)

