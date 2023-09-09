class Person:
    

    name="Abdullah"
    age = 17
    
    def __init__(self, name, age):

         self.name = name 
         self.age = age

         

    def __str__(self):
        return f"My name is {self.name} and I'am {self.age} years old" 

    def is_adult(self):
        if self.age > 18 :
            print("You have too much responsibilities")
        else:
            print("Lucky")            
   



first_student = Person("Abdullah", 17)
print(first_student.name)
print(first_student.age)
first_student.is_adult()
print(first_student)







