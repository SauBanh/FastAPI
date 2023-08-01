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
# from fastapi import Body, FastAPI
from typing import Optional
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel, Field

app = FastAPI()

class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    published_date: int
    def __init__(self, id, title, author, description, rating, published_date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date

class BookRequest(BaseModel):
    id: Optional[int] = 0
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=-1, lt=6)
    published_date: int = Field(gt=1999, lt=2031)

    class Config:
        json_schema_extra = {
            "example": {
                "title": "A new book",
                "author": "codingwithSauBanh",
                "description": "A new description of a book",
                "rating": 5,
                "published_date": 2000
            }
        }

BOOKS = [
    Book(1, "Computer Science Pro", "CodingwithSauBanh", "A very nice book", 5, 2008),
    Book(2, "Be Fast with FastAPI", "CodingwithSauBanh", "A great book", 5, 2005),
    Book(3, "Master Endpoints", "CodingwithSauBanh", "A awesome book", 5, 2010),
    Book(4, "HP1", "Author 1", "Book Description", 2, 2021),
    Book(5, "HP2", "Author 2", "Book Description", 3, 2023),
    Book(6, "HP3", "Author 3", "Book Description", 1, 2007),
]

@app.get("/books")
async def read_all_books():
    return BOOKS

@app.get("/books/{book_id}")
async def read_book(book_id: int = Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book

@app.get("/books/")
async def read_book_by_rating(book_rating: int = Query(gt=-1, lt=6)):
    book_to_return = []
    for book in BOOKS:
        if book.rating == book_rating:
            book_to_return.append(book)
    return book_to_return

@app.get("/books/publish/")
async def read_book_published_date(published_date: int = Query(gt=1999, lt=2031)):
    books_to_return = []
    for book in BOOKS:
        if book.published_date == published_date:
            books_to_return.append(book)
    return books_to_return

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

@app.put("/books/update_book")
async def update_book(book: BookRequest):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book

@app.delete("/books/{book_id}")
async def delete_book(book_id: int = Path(gt=0)):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            break


```

## Data Validation Query Parameters

```python
# from fastapi import Body, FastAPI
from typing import Optional
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel, Field

app = FastAPI()

class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    published_date: int
    def __init__(self, id, title, author, description, rating, published_date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date

class BookRequest(BaseModel):
    id: Optional[int] = 0
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=-1, lt=6)
    published_date: int = Field(gt=1999, lt=2031)

    class Config:
        json_schema_extra = {
            "example": {
                "title": "A new book",
                "author": "codingwithSauBanh",
                "description": "A new description of a book",
                "rating": 5,
                "published_date": 2000
            }
        }

BOOKS = [
    Book(1, "Computer Science Pro", "CodingwithSauBanh", "A very nice book", 5, 2008),
    Book(2, "Be Fast with FastAPI", "CodingwithSauBanh", "A great book", 5, 2005),
    Book(3, "Master Endpoints", "CodingwithSauBanh", "A awesome book", 5, 2010),
    Book(4, "HP1", "Author 1", "Book Description", 2, 2021),
    Book(5, "HP2", "Author 2", "Book Description", 3, 2023),
    Book(6, "HP3", "Author 3", "Book Description", 1, 2007),
]

@app.get("/books")
async def read_all_books():
    return BOOKS

@app.get("/books/{book_id}")
async def read_book(book_id: int = Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book

@app.get("/books/")
async def read_book_by_rating(book_rating: int = Query(gt=-1, lt=6)):
    book_to_return = []
    for book in BOOKS:
        if book.rating == book_rating:
            book_to_return.append(book)
    return book_to_return

@app.get("/books/publish/")
async def read_book_published_date(published_date: int = Query(gt=1999, lt=2031)):
    books_to_return = []
    for book in BOOKS:
        if book.published_date == published_date:
            books_to_return.append(book)
    return books_to_return

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

@app.put("/books/update_book")
async def update_book(book: BookRequest):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book

@app.delete("/books/{book_id}")
async def delete_book(book_id: int = Path(gt=0)):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            break
```

## Status Codes

status list:

**1xx (Information)**: Request received, continue processing.

| Status Code | Describe                                                     |
| ----------- | ------------------------------------------------------------ |
| 1xx         | Information: Request has been received, continue processing. |
| 100         | Continue                                                     |
| 101         | Switching Protocols                                          |
| 102         | Processing (WebDAV)                                          |
| 103         | Early Hints                                                  |

**2xx (Success)**: Request has been received, understood and accepted.

| Status Code | Describe                                                    |
| ----------- | ----------------------------------------------------------- |
| 2xx         | Success: The request was received, understood and accepted. |
| 200         | OK                                                          |
| 201         | Created                                                     |
| 202         | Accepted                                                    |
| 203         | Non-Authoritative Information                               |
| 204         | No Content                                                  |
| 205         | Reset Content                                               |
| 206         | Partial Content                                             |
| 207         | Multi-Status (WebDAV)                                       |
| 208         | Already Reported (WebDAV)                                   |
| 226         | IM Used                                                     |

**3xx (Navigation)**: Requires to continue or take an additional action to complete.

| Status Code | Describe                                                                 |
| ----------- | ------------------------------------------------------------------------ |
| 3xx         | Redirect: Requires to continue or take an additional action to complete. |
| 300         | Multiple Choices                                                         |
| 301         | Moved Permanently                                                        |
| 302         | Found (Moved Temporarily)                                                |
| 303         | See Other                                                                |
| 304         | Not Modified                                                             |
| 305         | Use Proxy (deprecated)                                                   |
| 307         | Temporary Redirect                                                       |
| 308         | Permanent Redirect (experimental)                                        |

**4xx (Client error)**: The request contains incorrect syntax or cannot be completed.

| Status Code | Describe                                                                    |
| ----------- | --------------------------------------------------------------------------- |
| 4xx         | Client error: The request contains incorrect syntax or cannot be completed. |
| 400         | Bad Request                                                                 |
| 401         | Unauthorized                                                                |
| 402         | Payment Required                                                            |
| 403         | Forbidden                                                                   |
| 404         | Not Found                                                                   |
| 405         | Method Not Allowed                                                          |
| 406         | Not Acceptable                                                              |
| 407         | Proxy Authentication Required                                               |
| 408         | Request Timeout                                                             |
| 409         | Conflict                                                                    |
| 410         | Gone                                                                        |
| 411         | Length Required                                                             |
| 412         | Precondition Failed                                                         |
| 413         | Payload Too Large                                                           |
| 414         | URI Too Long                                                                |
| 415         | Unsupported Media Type                                                      |
| 416         | Range Not Satisfiable                                                       |
| 417         | Expectation Failed                                                          |
| 418         | I'm a teapot (RFC 2324)                                                     |
| 421         | Misdirected Request                                                         |
| 422         | Unprocessable Entity (WebDAV)                                               |
| 423         | Locked (WebDAV)                                                             |
| 424         | Failed Dependency (WebDAV)                                                  |
| 426         | Upgrade Required                                                            |
| 428         | Precondition Required                                                       |
| 429         | Too Many Requests                                                           |
| 431         | Request Header Fields Too Large                                             |
| 451         | Unavailable For Legal Reasons                                               |

**5xx (Server error)**: The server could not complete a valid request.

| Status Code | Describe                                                     |
| ----------- | ------------------------------------------------------------ |
| 5xx         | Server Error: The server could not complete a valid request. |
| 500         | Internal Server Error                                        |
| 501         | Not Implemented                                              |
| 502         | Bad Gateway                                                  |
| 503         | Service Unavailable                                          |
| 504         | Gateway Timeout                                              |
| 505         | HTTP Version Not Supported                                   |
| 506         | Variant Also Negotiates (Experimental)                       |
| 507         | Insufficient Storage (WebDAV)                                |
| 508         | Loop Detected (WebDAV)                                       |
| 510         | Not Extended                                                 |
| 511         | Network Authentication Required                              |

```c
1xx (Informational responses):

100 Continue: Máy chủ hiểu yêu cầu từ máy khách và yêu cầu máy khách tiếp tục gửi phần còn lại của yêu cầu.
101 Switching Protocols: Máy chủ đồng ý chuyển đổi giao thức được yêu cầu trong yêu cầu nào đó.

2xx (Successful responses):

200 OK: Yêu cầu đã thành công và có dữ liệu phản hồi được trả về.
201 Created: Yêu cầu đã thành công và tài nguyên mới đã được tạo thành công.
202 Accepted: Yêu cầu đã được chấp nhận để xử lý, nhưng việc xử lý có thể chưa hoàn thành.
203 Non-Authoritative Information: Dữ liệu được trả về không phải là nguồn gốc từ máy chủ xuất phát, mà là từ một máy chủ trung gian.
204 No Content: Yêu cầu đã thành công, nhưng không có nội dung phản hồi để trả về.
205 Reset Content: Yêu cầu đã thành công, và client phải đặt lại tài liệu mà nó đang hiển thị.
206 Partial Content: Máy chủ đã trả về chỉ một phần của tài nguyên yêu cầu, thường được sử dụng cho phân mảnh (range) yêu cầu.

3xx (Redirection messages):

300 Multiple Choices: Có nhiều tài nguyên khả dụng cho yêu cầu được cho, máy khách nên chọn một trong số chúng.
301 Moved Permanently: Tài nguyên được yêu cầu đã được chuyển vĩnh viễn đến một địa chỉ mới.
302 Found (or Moved Temporarily): Tài nguyên được yêu cầu tạm thời chuyển đến một địa chỉ mới.
303 See Other (or Redirect): Yêu cầu đã được xử lý xong và client nên chuyển sang địa chỉ mới cung cấp trong trường header "Location".
304 Not Modified: Client sử dụng bộ nhớ cache và phiên bản đã cache của tài nguyên vẫn hiện có, không cần phải tải lại.
307 Temporary Redirect: Tài nguyên được yêu cầu tạm thời chuyển đến một địa chỉ mới, client không nên thay đổi phương thức HTTP khi gửi lại yêu cầu.
308 Permanent Redirect: Tài nguyên được yêu cầu đã được chuyển vĩnh viễn đến một địa chỉ mới, client không nên thay đổi phương thức HTTP khi gửi lại yêu cầu.

4xx (Client error responses):

400 Bad Request: Yêu cầu không hợp lệ do lỗi cú pháp hoặc yêu cầu không thể hiểu được.
401 Unauthorized: Yêu cầu cần xác thực và người dùng chưa được xác thực hoặc thông tin xác thực không hợp lệ.
402 Payment Required: Đã không sử dụng (từ phiên bản HTTP/1.1).
403 Forbidden: Máy chủ hiểu yêu cầu, nhưng từ chối cung cấp nội dung cho người dùng cụ thể.
404 Not Found: Tài nguyên được yêu cầu không tồn tại trên máy chủ.
405 Method Not Allowed: Phương thức yêu cầu không được hỗ trợ cho tài nguyên được yêu cầu.
406 Not Acceptable: Máy chủ không hỗ trợ định dạng yêu cầu mà người dùng yêu cầu.
407 Proxy Authentication Required: Yêu cầu cần xác thực proxy.
408 Request Timeout: Máy chủ đã hết thời gian chờ đợi cho yêu cầu.
409 Conflict: Yêu cầu xung đột với trạng thái hiện tại của tài nguyên.
410 Gone: Tài nguyên đã bị xóa và không còn tồn tại trên máy chủ.
411 Length Required: Yêu cầu thiếu trường "Content-Length".
412 Precondition Failed: Điều kiện tiên quyết của yêu cầu không được thỏa mãn.
413 Payload Too Large: Yêu cầu quá lớn, máy chủ từ chối xử lý do kích thước quá lớn.
414 URI Too Long: URL yêu cầu quá dài, máy chủ không thể xử lý.
415 Unsupported Media Type: Định dạng dữ liệu yêu cầu không được hỗ trợ.
416 Range Not Satisfiable: Yêu cầu có trường "Range" không hợp lệ hoặc không thể thỏa mãn.
417 Expectation Failed: Máy chủ không thể đáp ứng các yêu cầu trong header "Expect".
418 I am a teapot: Mã trạng thái phụ thuộc vào chế độ chế biến trà của máy chủ (thông qua RFC 2324).
421 Misdirected Request: Yêu cầu không thể được gửi tới máy chủ hiện tại (RFC 7540).
422 Unprocessable Entity: Yêu cầu hợp lệ nhưng máy chủ không thể xử lý (WebDAV; RFC 4918).
423 Locked: Tài nguyên được yêu cầu đang bị khóa (WebDAV; RFC 4918).
424 Failed Dependency: Yêu cầu yêu cầu không thành công do yêu cầu trước đó thất bại (WebDAV; RFC 4918).
426 Upgrade Required: Máy chủ yêu cầu phiên bản protocol cao hơn (RFC 2817).
428 Precondition Required: Yêu cầu yêu cầu phải có header điều kiện tiên quyết (RFC 6585).
429 Too Many Requests: Người dùng đã gửi quá nhiều yêu cầu trong một khoảng thời gian cụ thể (RFC 6585).
431 Request Header Fields Too Large: Header yêu cầu quá lớn, máy chủ từ chối xử lý (RFC 6585).
451 Unavailable For Legal Reasons: Truy cập tài nguyên bị từ chối vì lý do pháp lý (RFC 7725).

5xx (Server error responses):

500 Internal Server Error: Máy chủ gặp lỗi nội bộ không xác định khi xử lý yêu cầu.
501 Not Implemented: Máy chủ không hỗ trợ tính năng yêu cầu trong yêu cầu.
502 Bad Gateway: Máy chủ proxy hoặc cổng không hợp lệ nhận được phản hồi không hợp lệ từ máy chủ lưu trữ.
503 Service Unavailable: Máy chủ không thể xử lý yêu cầu do quá tải hoặc bảo trì.
504 Gateway Timeout: Máy chủ proxy không nhận được phản hồi từ máy chủ lưu trữ trong khoảng thời gian cho phép.
505 HTTP Version Not Supported: Phiên bản HTTP không được hỗ trợ bởi máy chủ.
506 Variant Also Negotiates: Máy chủ có nhiều biến thể lựa chọn trong cơ sở dữ liệu, nhưng mục tiêu chỉ định đã không được tìm thấy (RFC 2295).
507 Insufficient Storage: Máy chủ không có không gian đủ để hoàn thành yêu cầu (WebDAV; RFC 4918).
508 Loop Detected: Máy chủ đã phát hiện một vòng lặp vô hạn trong yêu cầu (WebDAV; RFC 5842).
510 Not Extended: Máy chủ yêu cầu giá trị mở rộng bổ sung không được hỗ trợ bởi máy khách.
511 Network Authentication Required: Yêu cầu yêu cầu xác thực mạng (RFC 6585).
```

## HTTP Exceptions

```python
# from fastapi import Body, FastAPI
from typing import Optional
from fastapi import FastAPI, Path, Query, HTTPException
from pydantic import BaseModel, Field

@app.get("/books/{book_id}")
async def read_book(book_id: int = Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Item not found")
```

```python
# from fastapi import Body, FastAPI
from typing import Optional
from fastapi import FastAPI, Path, Query, HTTPException
from pydantic import BaseModel, Field
from starlette import status

@app.get("/books", status_code=status.HTTP_200_OK)
async def read_all_books():
    return BOOKS

@app.get("/books/{book_id}")
async def read_book(book_id: int = Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Item not found")

@app.post("/create_book", status_code=status.HTTP_201_CREATED)
async def create_book(book_request: BookRequest):
    # print(type(book_request))
    new_book = Book(**book_request.dict())
    # print(type(new_book))
    BOOKS.append(find_book_id(new_book))
```

## Config SQLite 3

1. Download Sqlite: https://www.sqlite.org/download.html
2. Move file in C and set variables
3. Control Panel => System and Security => System => Advanced => Environment Variables
4. Inside System variables double click
5. Add new variables: C:\sqlite3
6. Ok all

## SQL Queries

### Inserting database table(todos)

```SQL
insert into todos(title, description, priority, complete)
values("Haircut", "Need to get length 1mm'3", False)
```

### Select Queries

```SQL
SELECT * FROM todos; --Select all columns and rows
SELECT title FROM todos; --Select just title from columns
SELECT description FROM todos; --Select just description from columns
SELECT description, title FROM todos; --Select title, description from columns
SELECT description, title, priority FROM todos; --Select title, description, priority from columns
```

### wwhere SQL queries

```SQL
SELECT * FROM todos WHERE priority=5 -- select all rows & columns where priority=5
SELECT * FROM todos WHERE title='Feed dog' -- select all rows & columns where title='Feed dog'
SELECT * FROM todos WHERE id=2 -- select all rows & columns where id=2
```

### Update SQL queries

```SQL
UPDATE todos SET complete=True WHERE id=5 -- Update All rows & columns to now have complete = True Where id=5

UPDATE todos SET complete=True WHERE title='Learn something new' -- Update All rows & columns to now have complete = True Where title='Learn something new'
```

### Delete SQL queries

```SQL

```
