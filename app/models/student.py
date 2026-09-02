from datetime import datetime

from app.core.abc_interfaces import Person
from app.core.descriptors import NameDescriptor
from app.core.descriptors import EmailDescriptor
from app.core.descriptors import AgeDescriptor
from app.core.metaclasses import ModelMeta


class Student(Person, metaclass=ModelMeta):

    name = NameDescriptor()
    email = EmailDescriptor()
    age = AgeDescriptor()

    def __init__(self, student_id, name, age, email, department):

        self.student_id = student_id
        self.name = name
        self.age = age
        self.email = email
        self.department = department

        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def display_details(self):
        print("Student ID:", self.student_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Email:", self.email)
        print("Department:", self.department)

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "email": self.email,
            "department": self.department
        }