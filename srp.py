class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def get_detail(self):
        return f"name:{self.name} salary:{self.salary}"
class files:
    @staticmethod
    def save_file(data,filename):
        with open(filename,"w") as file:
            file.write(data)

emp=employee("john",50000)
details=emp.get_detail()

files.save_file(details,"emp.txt")