from typing import TypedDict
 
class Person (TypedDict):
    name: str
    age: int


person: Person={
    'name': 'Hrithik',
    'age': 23
}

print(type(person))
print(person)