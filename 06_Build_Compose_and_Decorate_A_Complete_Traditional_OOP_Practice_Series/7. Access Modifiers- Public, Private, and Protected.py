# 7. Access Modifiers: Public, Private, and Protected
# Assignment:
# Create a class Employee with:
# a public variable name,
# a protected variable _salary, and
# a private variable __ssn.
# Try accessing all three variables from an object of the class and document what happens.

class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name            
        self._salary = salary       
        self.__ssn = ssn            

e = Employee("Ahmed", 50000, "123-45-6789")

print(e.name)        
print(e._salary)     
# print(e.__ssn)     # Error
print(e._Employee__ssn)  
