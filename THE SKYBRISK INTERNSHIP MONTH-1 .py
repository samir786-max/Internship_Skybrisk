==================== WEEK: 1 ====================

### Introduction to Python

Python is a high-level programming language known for its simplicity and readability. It was created by Guido van Rossum in 1989 at CWI (Centrum Wiskunde & Informatica) in the Netherlands and officially released in 1991.

Python is widely preferred because it allows developers to write clean and understandable code with fewer lines compared to many other programming languages.

Why Python is Popular:

Easy to understand and beginner-friendly

Dynamically typed (no need to declare data types explicitly)

Large community and strong library support

Used in multiple domains like:

Web development

Data analysis

Automation

Artificial Intelligence

GUI applications

Game development

### Input and Output in Python


Taking Input from the User

In Python, we use the input() function to receive data from the user. By default, the value entered through input() is treated as a string.

If we want to use numbers, we must convert the string into int or float.

name = input("Enter your name: ")
print(name)

age = int(input("Enter your age: "))
price = float(input("Enter price: "))
print(age)
print(price)
Displaying Output

To show results on the screen, Python provides the print() function.

print("Hello")

### Variables in Python

A variable is simply a name used to store data. Python automatically decides the data type based on the assigned value, so we don’t need to declare it manually.

a = 10
b = 20
print(a, b)

x = 10
print(x)

name = "Alice"
print(name)

a, b, c = 1, 2, 3
print(a, b, c)

Variables help us store, reuse, and modify data easily throughout the program.

Data Types in Python

Python supports different types of data:

x = 10          # Integer
y = 3.14        # Float
z = 2 + 3j      # Complex number
print(x, y, z)
String (Text)
name = "Python"
print(name)

## Boolean

is_active = True
print(type(is_active))

### Collection Data Types

List (Ordered & Changeable)
fruits = ["apple", "banana"]
print(fruits)

Tuple (Ordered but Immutable)
colors = ("orange", "blue")
print(colors)


Set (Unordered & Unique Values)
numbers = {1, 2, 3}
print(numbers)


Dictionary (Key–Value Pair)
person = {
    "name": "anu",
    "age": 23
}
print(person)

### Conditional Statements

Conditional statements allow a program to make decisions based on certain conditions.

if Statement
x = 10
if x > 5:
    print("x is greater than 5")

if–else Statement
x = 10
if x > 20:
    print("Greater than 20")
else:
    print("Less than or equal to 20")

if-elif-else Statement
    
marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

Nested Condition
num = 10
if num > 0:
    if num % 2 == 0:
        print("Positive even number")
Logical Operator Example
age = 25
if age > 18 and age < 60:
    print("Working age")

Loops in Python

Loops help us repeat a block of code multiple times.

For Loop
n = 5
for i in range(n):
    print(i)
Looping Through a List
fruits = ["apple", "mango"]
for fruit in fruits:
    print(fruit)
While Loop
i = 1
while i <= 5:
    print(i)
    i += 1
Break Statement

Stops the loop immediately.

for i in range(10):
    if i == 5:
        break
    print(i)
Continue Statement

Skips the current iteration.

for i in range(5):
    if i == 2:
        continue
    print(i)
Nested Loop
for i in range(3):
    for j in range(2):
        print(i, j)

 Basic Programs

Temperature Converter

This program converts temperature between Celsius and Fahrenheit.

print("Temperature Converter")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = int(input("Enter your choice (1 or 2): "))

if choice == 1:
    c = float(input("Enter temperature in Celsius: "))
    f = (c * 9/5) + 32
    print("Temperature in Fahrenheit:", f)

elif choice == 2:
    f = float(input("Enter temperature in Fahrenheit: "))
    c = (f - 32) * 5/9
    print("Temperature in Celsius:", c)

else:
    print("Invalid choice")

Simple Calculator
print("Select Operation")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Floor Division")

choice = int(input("Enter your choice (1/2/3/4/5): "))

n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))

if choice == 1:
    print("Result =", n1 + n2)
elif choice == 2:
    print("Result =", n1 - n2)
elif choice == 3:
    print("Result =", n1 * n2)
elif choice == 4:
    print("Result =", n1 / n2)
elif choice == 5:
    print("Result =", n1 // n2)
else:
    print("Invalid choice")


Basic Data Processing Script

Calculating Average Temperature

This small script demonstrates how data can be collected, processed, and analyzed.

n = int(input("Enter the number of days: "))

temperatures = []

for i in range(n):
    temp = float(input(f"Enter temperature for day {i+1}: "))
    temperatures.append(temp)

total = sum(temperatures)
average = total / n

print("Temperatures:", temperatures)
print("Average temperature:", average)


==================== WEEK – 2 ====================

Working with Data Structures & Functions

During Week-2, I focused on understanding Python data structures and writing reusable functions for data transformation and cleaning.

 Python Data Structures

1️. List (Mutable Collection)

A list in Python is an ordered collection that allows storing multiple values inside a single variable. Lists are changeable (mutable) and can contain duplicate elements.

Example:

fruits = ["apple", "banana", "mango"]
print(fruits)

Key Features:

Ordered

Allows duplicates

Can be modified

2️. Tuple (Immutable Collection)

A tuple is similar to a list but cannot be modified once created.

Example:

colors = ("red", "green", "blue")
print(colors)

Key Features:

Ordered

Immutable

Allows duplicates

3️. Set (Unique Collection)

A set stores only unique values and does not maintain order.

Example:

numbers = {1, 2, 3, 3}
print(numbers)

Key Features:

Unordered

No duplicates

Mutable

4️. Dictionary (Key–Value Pair)

A dictionary stores data in key-value format.

Example:

student = {
    "name": "Ravi",
    "age": 21
}
print(student)
 Functions in Python

A function is a reusable block of code designed to perform a specific task. Functions improve code reusability, readability, and maintainability.

Why Functions Are Important:

Reduce repetition

Improve modularity

Make code easier to manage

 Defining a Function

def function_name(parameters):
    # code block
    return value


Types of Arguments

1. Default Arguments

Provide a default value if no argument is passed.

2. Keyword Arguments

Arguments passed with parameter names.

3. Positional Arguments

Arguments passed based on order.

4. Arbitrary Arguments

*args → Multiple positional arguments

**kwargs → Multiple keyword arguments

Example: Data Transformation Functions

Sum of Squares
def sum_of_squares(numbers):
    total = 0
    for n in numbers:
        total += n * n
    return total

nums = [2, 4, 6, 8, 10]
print(sum_of_squares(nums))
Filtering Even Numbers
def filter_even(numbers):
    result = []
    for n in numbers:
        if n % 2 == 0:
            result.append(n)
    return result

nums = [21, 22, 23, 42, 98, 77]
print(filter_even(nums))

Data Cleaning Script

This script removes duplicates, filters invalid values, and keeps values greater than 10.

def clean_and_filter(data):
    data = list(set(data))  # Remove duplicates
    
    cleaned = []
    for item in data:
        if isinstance(item, (int, float)) and item >= 0:
            cleaned.append(item)

    filtered = []
    for item in cleaned:
        if item > 10:
            filtered.append(item)

    return filtered

numbers = [5, 15, 20, 25, 20, -3, "a", 30, 12, 23, 37]
result = clean_and_filter(numbers)
print("Cleaned & Filtered Data:", result)

Explanation:

set() removes duplicates

isinstance() keeps only numeric values

Negative values are removed

Values greater than 10 are retained

==================== WEEK – 3 ====================

NumPy and Pandas for Data Analysis

During Week-3, I worked with NumPy and Pandas, which are essential libraries for data analysis.

NumPy

NumPy is a powerful Python library used for numerical computations. It is optimized for handling arrays and performing mathematical operations efficiently.

Key Features:

Fast n-dimensional arrays

Vectorized operations

Broadcasting

Linear algebra functions

Statistical tools

Creating Arrays
import numpy as np

a1 = np.array([1, 2, 3])         # 1D array
a2 = np.array([[1, 2], [3, 4]])  # 2D array

print(a1)
print(a2)
Basic Operations
a = np.array([10, 20, 30, 40])
b = np.array([1, 2, 3, 4])

print(a + b)
print(a - b)
print(a * b)
print(a / b)
Aggregation Functions
arr = np.array([4, 8, 11, 20, 18])

print(np.sum(arr))
print(np.mean(arr))
print(np.max(arr))
print(np.min(arr))
Broadcasting Example
a = np.array([1, 2, 3, 4, 5])
print(a + 5)

NumPy automatically expands the scalar value across all elements.

Pandas

Pandas is a data manipulation and analysis library built on top of NumPy.

It provides two main data structures:

Series (1D)

DataFrame (2D)

Creating a DataFrame
import pandas as pd

data = {
    "Student": ["Asha", "Ravi", "Meena"],
    "Marks": [85, 95, 90]
}

df = pd.DataFrame(data)
print(df)
Basic Operations in Pandas
Viewing Data
print(df.head())
print(df.info())
print(df.describe())
Filtering Data
df[df["Marks"] > 85]
Handling Missing Values
df = df.fillna(0)
Removing Duplicates
df = df.drop_duplicates()


==================== WEEK – 4 ====================


Data Visualization with Matplotlib & Seaborn

In Week-4, I learned how to visualize data using Matplotlib and Seaborn.

Matplotlib

Matplotlib is a visualization library used for creating static and interactive graphs.

Line Plot
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [2, 4, 6, 8]

plt.plot(x, y)
plt.title("Line Chart")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
Bar Chart
fruits = ["Apple", "Banana", "Mango"]
sales = [100, 150, 120]

plt.bar(fruits, sales)
plt.show()
Scatter Plot
plt.scatter(x, y)
plt.show()


Seaborn

Seaborn is built on top of Matplotlib and provides better styling and advanced statistical plots.

Scatter Plot using Dataset
import seaborn as sns
import matplotlib.pyplot as plt

sns.scatterplot(x="Marks", y="Marks", data=df)
plt.show()
Bar Plot
sns.barplot(x="Student", y="Marks", data=df)
plt.show()
Heatmap
import numpy as np

data = np.random.randint(1, 100, (5, 5))
sns.heatmap(data, annot=True)

plt.show()
