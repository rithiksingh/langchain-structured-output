from pydantic import BaseModel

class Person(BaseModel):
    name: str
    age: int


person={'name': 'hrithik', 'age': 23}

person1= Person(**person)

print(type(person1))
print(person1.age)