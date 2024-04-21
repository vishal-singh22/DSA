class Employee:
    def __init__(self,emp_id=None,name=None,sal=None):
        self.emp_id=emp_id
        self.name=name
        self.sal=sal
    def setemp_id(self,emp_id):
        self.emp_id=emp_id
    def setname(self,name):
        self.name=name
    def getemp_id(self):
        return self.emp_id
    def getname(self):
        return self.name
    def getsal(self):
        return self.sal
e1=Employee(23,'yuvi',25000)
e2=Employee(32,'sing',2000)
e3=Employee(2,'vishu',5000)
e4=Employee()
e4.setname('vinay')
e4.setemp_id(36)
print(e1.getemp_id(),e1.getsal(),e1.getname())
print(e2.getemp_id(),e2.getsal(),e2.getname())
print(e3.getemp_id(),e3.getsal(),e3.getname())
print(e4.getemp_id(),e4.getname())
