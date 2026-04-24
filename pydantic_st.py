from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str = "ashish"
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(
        default=5.0,
        gt=0,
        lt=10,
        description="A decimal value representing the CGPA"
    )

# data
new_student = {
    "age": 32,
    "email": "abc@gmail.com",
    "cgpa": 5
}


student_obj = Student(**new_student)


print(student_obj)            
print(student_obj.model_dump())  
print(f"Name: {student_obj.name}, Age: {student_obj.age}, Email: {student_obj.email}, CGPA: {student_obj.cgpa}")