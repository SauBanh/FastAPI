# FastAPI

## Refresher

### Variables!

#### Number

```python
const = 10
print(const)
```

#### String

```python
username = "Tuấn Anh"
first_name = "Nguyễn"
print(username + " " + first_name)
```

#### Formating String

```python
first_name = "Nguyễn Tuấn Anh"
last_name = "Tuấn Anh"
print(f"Hi {first_name} {last_name}")
print("Hi " + first_name)
print(f"Hi {first_name}")
sentence = "Hi {} {}"
print(sentence.format(first_name, last_name))
```

### Comments!

```python
#print("Nguyễn Tuấn Anh")
"""
This is going over
multiple
lines
"""
'''
This is going over
multiple
lines
'''
```

### User Input

```python
first_name = input("Enter your first name: ")
days = input("How many days before your birth date: ")
print(f"Hi {first_name} only {days} before your birthdate!")
```

### String Assignment Solution

```python
days = int(input("How many days before your birthdate: "))
print(days/7)
print(round(days/7, 2))
```

### Lists in Python

```python
my_list = [80, 96, 72, 100, 8]
my_list.append(1000) # add last item from array
my_list.insert(2,1000) # insert 1000 in index 2 to array
my_list.remove(8) # remove value 8 from array
my_list.pop(0) # remove first item index from array
my_list.sort() # sort values from low to high
print(my_list)
print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[-1])
print(my_list[-2])
print(my_list[-3])

people_list = ["Nguyễn Tuấn Anh", "Tài Lê", "Thành Công"]
people_list[0] = "Sáu Bảnh"
print(people_list)
print(people_list[0:2])
```

### Sets and Tuples

```python
my_set = {1, 2, 3, 4, 5, 1, 2}
print(my_set)
print(len(my_set))

for x in my_set:
    print(x)

# print(my_set[0]) it not works
my_set.discard(3) # remove value 3 from my_set
my_set.add(6) # add value 6 to my_set
my_set.update([7, 8])
print(my_set)
```

```c
my_tuples = (1, 2, 3, 4, 5)
print(my_tuples)
print(my_tuples[1])
print(len(my_tuples))
```

```c
zoo = ["Monkey", "Zebra", "Gorilla", "Lion", "Tiger"]
zoo.pop(3) # remove index 3 in zoo
zoo.append("Lizard") # add last item in zoo
zoo.pop(0) # remove index 0 in zoo
for x in zoo:
    print(x)
```

### Booleans

```python
like_coffee = True
like_tea = False

favorite_food = "Pizza"
favorite_number = 32
print(type(like_coffee))
print(type(like_tea))
print(type(favorite_food))
print(type(favorite_number))

```

### Operators

```python
# Comparison Operators
print(1 == 2)
print(1 != 2)
print(1 > 2)
print(1 < 2)
print(1 >= 2)
print(1 <= 2)
# Logical Operators
print(1 > 3 and 5 < 7) # both must be right
print(1 > 3 or 5 < 7) # one of the two is correct
```

### If Else Statements

```python
x = 1
if x == 1:
    print("x is 1")
else:
    print("x is not greater 1")
print("Outside of if statement")

hour = 18
if hour < 15:
    print("Good morning!")
elif hour = 20:
    print("Good afternoon!")
else:
    print("Good Night!")
```

### If Else Assignment Solution

```python
grade = 73
if grade >= 90
    print("A")
# elif grade >= 80 and grade < 90:
elif 80 <= grade < 90:
    print("B")
elif 70 <= grade < 80:
    print("C")
elif 60 <= grade < 70:
    print("D")
else:
    print("F")
```

### Loops in Python

```python
my_list = [1, 2, 3, 4, 5]
# print(my_list[0])
# print(my_list[1])
# print(my_list[2])
# print(my_list[3])
# print(my_list[4])

for iterator in my_list:
    print(iterator)

for x in range(3,6):
    print(x)
```

```python
my_list = ["Monday", "Tuesday", "Wednesday", "Thursday"]
for x in my_list:
    print(f"Happy {x}!")
```

```python
i = 0
while i < 5:
    i+=1
    if i == 3:
        continue
    print(i)
    if i == 4:
        break
else:
    print("i is now larger equalto 5")
```

### Loops Assignment Solution

```python
my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
x = 0
while x < 5:
    x += 1
    for i in my_list:
        if i == "Monday":
            print("-------")
            continue
        print(i)
```

### Dictionaries in Python

```python
user_dictionary = {
    "username": "Nguyễn Tuấn Anh",
    "name": "Tuấn Anh",
    "age": 32
}
user_dictionary["maried"] = True
user_dictionary.pop("age")
user_dictionary.clear()
print(user_dictionary)

for x, y in user_dictionary.items():
    print(x, y)

user_dictionary2 = user_dictionary.copy()
user_dictionary2.pop("age")
print(user_dictionary)

# Dictionaries Assignment Solution
my_vehicle = {
    "model": "Ford",
    "make": "Explorer",
    "year": 2018,
    "mileage": 40000,
}
for x, y in my_vehicle.items():
    print(x, y)
vehicle2 = my_vehicle.copy()
vehicle2["number_of_tires"] = 4
vehicle2.pop("mileage")

for i in vehicle2:
    print(i)
```

### Functions in Python

```python
def my_function():
    print("Inside my_function")
my_function()
def print_my_name(first_name, last_name):
    print(f"Hello {first_name} {last_name}!")
print_my_name("Nguyễn", "Tuấn Anh")
```

```python
def print_color_red():
    color = "Red"
    print(color)

print_color_red()
```

```python
def multiply_numbers(a, b):
    return a * b
solution = multiply_numbers(10, 6)
print(solution)

def print_list(list_of_numbers):
    for x in list_of_numbers:
        print(x)
number_list = [1, 2, 3, 4, 5]
print_list(number_list)
```

```python
def buy_item(cost_of_item):
    return cost_of_item + add_tax_to_item(cost_of_item)

def add_tax_to_item(cost_of_item):
    current_tax_rate = .03
    return cost_of_item * current_tax_rate

print(buy_item(50))
```

### Functions Assignment Solution

```python
def user_dictionary(firstname, lastname, age):
    created_user_dictionary = {
        "firstname": firstname,
        "lastname": lastname,
        "age": age
    }
    return created_user_dictionary

solution_dictionary = user_dictionary(firstname="Nguyễn",  lastname="Tuấn Anh", age=22)
print(solution_dictionary)
print(user_dictionary("Sáu", "Bảnh", 22))
```

### Imports in Python

```python
# homework_grades.py
# import (FolderName).(FileName)
# import (FolderName).grade_average_service
# import (FolderName).grade_average_service as (CreateName)
import (FolderName).grade_average_service as grade_service
homework_assignment_grades = {
    "homework_1": 85,
    "homework_2": 100,
    "homework_3": 81,
}

# Import.grade_average_service.calculate_homework(homework_assignment_grades)
calculate_homework.calculate_homework(homework_assignment_grades)
```

```python
# grade_average_service.py
def calculate_homework(homework_assignment_arg):
    sum_of_grades = 0
    for homework in homework_assignment_grades.values():
        sum_of_grades += homework
    final_grade = round(sum_of_grades / len(homework_assignment_grades), 2)
    print(final_grade)
```

import random

```python
import random
types_of_drinks = ["Soda", "Coffee", "Water", "Tea"]
print(random.choice(types_of_drinks))

print(random.randint(1, 10))
```

import math

```python
import math
square_root = math.sqrt(64)
print(square_root)
```

## OOP (Object Oriented Programming)

Create class

```python
class Student:
    pass


# create a object
student_1 = Student()
student_2 = Student()

# add properties to the object
student_1.first_name = "Tuấn Anh"
student_1.last_name = "Nguyễn"
student_1.major = "FullStack"

student_2.first_name = "Bảnh"
student_2.last_name = "Sáu"
student_2.major = "FrontEnd"

print(student_1.first_name)
print(student_2.first_name)

print(student_1.major)
print(student_2.major)
```

Create contructor

```python
class Student:

    school = "Online School"

    # Create contructor
    def __init__(self, first_name, lastname, major):
        self.first_name = first_name
        self.last_name = lastname
        self.major = major

student_1 = Student("Nguyễn", "Tuấn Anh", "Full Stack")
student_2 = Student("Sáu", "Bảnh", "FrontEnd")

print(student_1.first_name)
print(student_2.first_name)
```

create function in class

```python
class Student:
    # Create variable in class
    school = "Online School"
    # Create contructor
    def __init__(self, first_name, last_name, major):
        self.first_name = first_name
        self.last_name = last_name
        self.major = major
    def fullname_with_major(self):
        return f"{self.first_name} {self.last_name} is a {self.major} major!"
    def fullname_major_school(self):
        return f"{self.first_name} {self.last_name} is a {self.major} go to {self.school}"
    @classmethod
    def set_online_school(cls, new_shool): # for the first argument, we'll use CLS, which stands for class.
        cls.school = new_shool
    @classmethod
    def split_student(cls, student_str):
        first_name, last_name, age = student_str.split(".")
        return cls(first_name, last_name, age)

student_1 = Student("Nguyễn", "Tuấn Anh", "Full Stack")
student_2 = Student("Sáu", "Bảnh", "FrontEnd")

print(student_1.fullname_with_major())
print(Student.fullname_with_major(student_2))
print(student_1.fullname_major_school())
print(student_2.fullname_major_school())

print(f"Number of students= {Student.number_of_students}")
student_1 = Student("Nguyễn", "Tuấn Anh", "Full Stack")
student_2 = Student("Sáu", "Bảnh", "FrontEnd")
print(f"Number of students= {Student.number_of_students}")

print(student_1.school)
print(student_2.school)
Student.set_online_school("I use Google Hangouts for class!")
print(student_1.school)
print(student_2.school)

new_student = "Tài.Lê.Mobile"
student_3 = Student.split_student(new_student)
print(student_3.fullname_with_major())
```

### Class Inheritance

```python
# create class
class Student:
    def __init__(self, first_name, last_name):
        self.first_name =first_name
        self.last_name = last_name
    def greetings(self):
        return f"Hello! I am {self.first_name} {self.last_name}"

# Create class
class CollegeStudent(Student):
    def __init__(self, first_name, last_name, major):
        super().__init__(first_name, last_name)
        self.major = major
    def greetings(self):
        return f"{self.first_name} is a college student!"

class NonCollegeStudent(Student):
    def __init__(self, first_name, last_name, future_adult_job):
        super().__init__(first_name, last_name)
        self.future_adult_job = future_adult_job
    def grow_up(self):
        return f"When I grow up, I want to be a {self.future_adult_job}"

# student_1 = CollegeStudent("Nguyễn", "Tuấn Anh", "FullStack")
# student_2 = Student("Sáu", "Bảnh")

student_1 = CollegeStudent("Nguyễn", "Tuấn Anh", "FullStack")
student_2 = NonCollegeStudent("Sáu", "Bảnh", "FrontEnd")

# print(student_1.greetings())
# print(student_2.greetings())
# print(student_1.major)
print(student_2.greetings())
print(student_2.grow_up())
```

## Virtual Environments Overview

### Install Dependencies

Check version

```terminal
python -m pip --version
```

Create a virtual environment with name fastapienv

```terminal
python -m venv fastapienv
```

To enable a virtual field we use

```terminal
fastapienv\Scripts\activate.bat
```

Install FastAPI

```terminal
pip install fastapi
```

Install uvicorn[standard]

```terminal
pip install "uvicorn[standard]"
```

Uvicorn is a lightning-fast ASGI (Asynchronous Server Gateway Interface) server that allows you to run and serve Python web applications that are built on ASGI frameworks like FastAPI, Starlette, and others. ASGI is a specification that enables handling asynchronous web requests in Python, making it possible to build high-performance web applications.

The [standard] part in the command refers to an "extra" feature of the uvicorn package, which means it installs optional dependencies that are not required for basic functionality but might be useful for certain use cases. These additional dependencies could include things like support for HTTP/2, automatic reload on code changes, and more.

By running this command, you will install uvicorn along with any optional dependencies that are part of the "standard" extra feature, enhancing its capabilities and allowing you to run ASGI web applications efficiently.

To deactivate an environment

```terminal
deactivate
```

### GET Request Method

```python
from fastapi import FastAPI

app = FastAPI()

@app.get('/api-endpoint')
async def first_api():
    return {"message": "Hello Tuấn Anh đẹp trai"}
```

to run the project:
activate the environment where the libraries are installed
run

```terminal
uvicorn main:app --reload
```

with main is name file and app is variable in file main

```python
from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {"title": "Title One", "author": "Author One", "category": "science"},
    {"title": "Title Two", "author": "Author Two", "category": "science"},
    {"title": "Title Three", "author": "Author Three", "category": "history"},
    {"title": "Title Four", "author": "Author Four", "category": "math"},
    {"title": "Title Five", "author": "Author Five", "category": "math"},
    {"title": "Title Six", "author": "Author Six", "category": "math"},
]

@app.get('/books')
async def read_all_book():
    return BOOKS
```

FastAPI has Swagger integration if you want to use it add "/docs" to the root path

### Path Parameters

```python
from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {"title": "Title One", "author": "Author One", "category": "science"},
    {"title": "Title Two", "author": "Author Two", "category": "science"},
    {"title": "Title Three", "author": "Author Three", "category": "history"},
    {"title": "Title Four", "author": "Author Four", "category": "math"},
    {"title": "Title Five", "author": "Author Five", "category": "math"},
    {"title": "Title Six", "author": "Author Six", "category": "math"},
]

@app.get('/books')
async def read_all_books():
    return BOOKS
@app.get('/books/{dynamic_param}')
async def read_all_books(dynamic_param: str):
    return {"dynamic_param": dynamic_param}
```

```python
from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {"title": "Title One", "author": "Author One", "category": "science"},
    {"title": "Title Two", "author": "Author Two", "category": "science"},
    {"title": "Title Three", "author": "Author Three", "category": "history"},
    {"title": "Title Four", "author": "Author Four", "category": "math"},
    {"title": "Title Five", "author": "Author Five", "category": "math"},
    {"title": "Title Six", "author": "Author Six", "category": "math"},
]

@app.get('/books')
async def read_all_book():
    return BOOKS
@app.get('/books/mybook')
async def read_all_books():
    return {"book_title": "My favorite book!"}
@app.get('/books/{book_title}')
async def read_all_books(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book
```

## Query Parameters

```python
@app.get("/books/")
async def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return
```

```python
@app.get("/books/{book_author}/")
async def read_author_category_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold()  and book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return
```

## Post Request

```python
@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)
    return new_book
```

## Put Request

```python
@app.put("/books/update_book")
async def update_book(update_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == update_book.get("title").casefold():
            BOOKS[i] = update_book
```

## Delete Request

```python
@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == book_title.casefold():
            BOOKS.pop(i)
            break
```

## Assignment Solution

```python
# @app.get("/books/byauthor/{author}")
# async def read_book_by_author_path(author: str):
#     book_return = []
#     for book in BOOKS:
#         if book.get("author").casefold() == author.casefold():
#             book_return.append(book)
#     return book_return

@app.get("/books/byauthor/")
async def read_book_by_author_path(author: str):
    book_return = []
    for book in BOOKS:
        if book.get("author").casefold() == author.casefold():
            book_return.append(book)
    return book_return
```

# Project 2

## Pydantic Book Request Validation

```python
class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating

class BookRequest(BaseModel):
    id: int
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=-1, lt=6)
```

## Fields - Data Validation

```python
# from fastapi import Body, FastAPI
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating

class BookRequest(BaseModel):
    id: int
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=-1, lt=6)

BOOKS = [
    Book(1, "Computer Science Pro", "CodingwithSauBanh", "A very nice book", 5),
    Book(2, "Be Fast with FastAPI", "CodingwithSauBanh", "A great book", 5),
    Book(3, "Master Endpoints", "CodingwithSauBanh", "A awesome book", 5),
    Book(4, "HP1", "Author 1", "Book Description", 2),
    Book(5, "HP2", "Author 2", "Book Description", 3),
    Book(6, "HP3", "Author 3", "Book Description", 1),
]

@app.get("/books")
async def read_all_books():
    return BOOKS

@app.post("/create_book")
async def create_book(book_request: BookRequest):
    # print(type(book_request))
    new_book = Book(**book_request.dict())
    # print(type(new_book))
    BOOKS.append(find_book_id(new_book))

def find_book_id(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    # if len(BOOKS) > 0:
    #     book.id = BOOKS[-1].id + 1
    # else:
    #     book.id = 1
    return book
```

```python
# from fastapi import Body, FastAPI
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating

class BookRequest(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=-1, lt=6)

BOOKS = [
    Book(1, "Computer Science Pro", "CodingwithSauBanh", "A very nice book", 5),
    Book(2, "Be Fast with FastAPI", "CodingwithSauBanh", "A great book", 5),
    Book(3, "Master Endpoints", "CodingwithSauBanh", "A awesome book", 5),
    Book(4, "HP1", "Author 1", "Book Description", 2),
    Book(5, "HP2", "Author 2", "Book Description", 3),
    Book(6, "HP3", "Author 3", "Book Description", 1),
]

@app.get("/books")
async def read_all_books():
    return BOOKS

@app.post("/create_book")
async def create_book(book_request: BookRequest):
    # print(type(book_request))
    new_book = Book(**book_request.dict())
    # print(type(new_book))
    BOOKS.append(find_book_id(new_book))

def find_book_id(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    # if len(BOOKS) > 0:
    #     book.id = BOOKS[-1].id + 1
    # else:
    #     book.id = 1
    return book
```

## Pydantic Configurations

```python

```
