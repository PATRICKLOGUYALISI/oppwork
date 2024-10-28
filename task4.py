class employee:
    def work(self):
        print("Employee is working")
        
class Manager(employee):
    def work(self):
        print("Manger is managing them")

Patrick=Manager()
Patrick.work()        
        
class Developer(employee):
    def work(self):
        print("Developer is Writing code")

Amos=Developer()
Amos.work()        