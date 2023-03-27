class Person():
    def __init__(self, name, age, height, email):
        self.name = name
        self.age = age
        self.height = height
        self.email = email



from dataclasses import dataclass

@dataclass
class Person():
    name: str
    age: int
    height: float
    email: str


# default attributes
@dataclass
class Person():
    name: str = 'Joe'
    age: int = 30
    height: float = 1.85
    email: str = 'joe@test.com'

print(Person())


# error
@dataclass
class Person():
    name: str = 'Joe'
    age: int = 30
    height: float = 1.85
    email: str



person = Person('Joe', 25, 1.85, 'joe@test.com')
print(person.name)



from typing import Tuple

@dataclass
class Person():
    name: str
    age: int
    height: float
    email: str
    house_coordinates: Tuple

print(Person('Joe', 25, 1.85, 'joe@test.com', (40.748441, -73.985664)))



from dataclasses import dataclass
from typing import List

@dataclass
class Person():
    name: str
    age: int
    height: float
    email: str

@dataclass
class People():
    people: List[Person]

joe = Person('Joe', 25, 1.85, 'joe@test.com')
mary = Person('Mary', 43, 1.67, 'mary@test.com')

print(People([joe, mary]))



# comparison 
# no data class
from dataclasses import dataclass

class Person():
    def __init__(self, name, age, height, email):
        self.name = name
        self.age = age
        self.height = height
        self.email = email

    def __repr__(self):
        return (f'{self.__class__.__name__}(name={self.name}, age={self.age}, height={self.height}, email={self.email})')

person = Person('Joe', 25, 1.85, 'joe@test.com')
print(person)


# data classes
from dataclasses import dataclass

@dataclass
class Person():
    name: str
    age: int
    height: float
    email: str

person = Person('Joe', 25, 1.85, 'joe@test.com')
print(person)


# to overwite 
@dataclass
class Person():
    name: str
    age: int
    height: float
    email: str

    def __repr__(self):
        return (f'''This is a {self.__class__.__name__} called {self.name}.''')

person = Person('Joe', 25, 1.85, 'joe@dataquest.io')
print(person)


# comparing insances
# data class
@dataclass
class Person():
    name: str = 'Joe'
    age: int = 30
    height: float = 1.85
    email: str = 'joe@dataquest.io'

print(Person() == Person()) # returns True because of __eq__


# no data class
class Person():
    def __init__(self, name='Joe', age=30, height=1.85, email='joe@dataquest.io'):
        self.name = name
        self.age = age
        self.height = height
        self.email = email

print(Person() == Person()) # returns False



class Person():
    def __init__(self, name='Joe', age=30, height=1.85, email='joe@dataquest.io'):
        self.name = name
        self.age = age
        self.height = height
        self.email = email

    def __eq__(self, other):
        if isinstance(other, Person):
            return (self.name, self.age,
                    self.height, self.email) == (other.name, other.age,
                                                 other.height, other.email)
        return NotImplemented

print(Person() == Person())



# sorting
from dataclasses import dataclass

@dataclass(order=True)
class Person():
    name: str
    age: int
    height: float
    email: str
joe = Person('Joe', 25, 1.85, 'joe@test.com')
mary = Person('Mary', 43, 1.67, 'mary@test.com')

print(joe < mary) # because J comes before M, if equal it would go to the next element



# no frozen keyword
@dataclass()
class Person():
    name: str
    age: int
    height: float
    email: str

joe = Person('Joe', 25, 1.85, 'joe@test.com')

joe.age = 35
print(joe)

# frozen keyword
@dataclass(frozen=True)
class Person():
    name: str
    age: int
    height: float
    email: str

joe = Person('Joe', 25, 1.85, 'joe@test.com')

joe.age = 35
print(joe)



# inheritance
from dataclasses import dataclass, field

@dataclass(order=True)
class Person():
    name: str
    age: int
    height: float
    email: str

@dataclass(order=True)
class Employee(Person):
    salary: int
    departament: str    
    
print(Employee('Joe', 25, 1.85, 'joe@test.com', 100000, 'Marketing'))
