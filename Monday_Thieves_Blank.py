#!/usr/bin/env python
# coding: utf-8

# # Week 2 - Monday Lesson (variable assignment, loops, lists)

# ## Tasks Today:
# 
# 1) Int & Float assignments <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Assigning int <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) Assigning float <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) Performing Calculations on ints and floats <br>
#  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Addition <br>
#  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Subtraction <br>
#  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Multiplication <br>
#  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Division <br>
#  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Floor Division <br>
#  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Modulo <br>
#  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Exponential <br>
# 2) String Input-Output <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) String Assignment <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) print() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) String Concatenation <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; d) Type Conversion <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; e) input() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; f) format() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; g) Old Way (python 2) <br>
# 3) <b>In-Class Exercise #1</b> <br>
# 4) If Statements <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) 'is' keyword <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) 'in' keyword <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) 'not in' keyword <br>
# 5) <b>In-Class Exercise #2</b> <br>
# 6) Elif Statements <br>
# 7) Else Statements <br>
# 8) <b>In-Class Exercise #3</b> <br>
# 9) For Loops <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Using 'in' keyword <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) Continue Statement <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) Break Statement <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; d) Pass Statement <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; e) Double For Loops <br>
# 10) While Loops <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Looping 'While True' <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) While and For Loops Used Together <br>
# 11) Built-In Functions <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) range() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) len() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) help() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; d) isinstance() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; e) abs() <br>
# 12) Try and Except <br>
# 13) Lists <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Declaring Lists <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) Indexing a List <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) .append() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; d) .insert() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; e) .pop() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; f) .remove() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; g) del() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; h) Concatenating Two Lists <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; i) Lists Within Lists <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; j) Looping Through Lists <br>

# ### Int & Float Assignments

# ##### Assigning int - Integer types are whole numbers

# In[2]:


int1 = 1

print(int1)


# ##### Assinging float - Float types are decimals
# 

# In[ ]:


fl


# #### Performing Calculations on ints and floats

# ##### Addition (+)

# In[3]:


print(1+1)


# ##### Subtraction (-)

# In[ ]:


print(5-2)


# ##### Multiplication (*)

# In[ ]:





# ##### Division (/)

# In[ ]:





# ##### Floor Division (//) - Normal division but returns the largest possible integer
# 

# In[ ]:





# ##### Modulo (%) - Returns the remainder of division
# 

# In[ ]:





# ##### Exponential (**)

# In[15]:


int1 = 5
print(int1**2)


# ### String Input-Output

# ##### String Assignment

# In[ ]:





# ##### print() <br>
# <p>Don't forget about end=' '</p>

# In[ ]:





# ##### String Concatenation

# In[ ]:





# ##### Type Conversion

# In[ ]:





# ##### input()

# In[ ]:





# ##### format()

# In[ ]:





# # In-Class Exercise 1 <br>
# <p>Create a format statement that asks for color, year, make, model and prints out the results</p>

# In[3]:


color = input("What is the color?: ")
year = input("What is the year: ")
make = input("What is the make: ")
model = input("What is your model: ")
answer = f'Hello I own a {year} {make} {model} in the color of {color}'
print(answer)


# ### If Statements

# In[5]:


# Available operators: Greater(>), Less(<),Equal(==)
# Greater or Equal(>=), Less or Equal (<=)

# Truth Tree:
# T and F = F
# T and T = T
# T or F = T
# F or T = T
# F or F = F

print(1 == 1 and 1==2)
print('john' == 'johhn' or 'h' == 'h')


# ##### 'is' keyword - Checks if the value refers to the same object in memory, not if they equal each other

# In[7]:


list1 = ['yo','yoyo']
list2 = list1[::]
print(list1 is list2)


# ##### 'in' keyword = used to check if a value is present in a sequence

# In[9]:


list1 = ['yo','yoyo']
print('yo' in list1)


# ##### 'not in' keyword'

# In[ ]:


print('kfof' not in list1)


# # In-Class Exercise 2 <br>
# <p>Ask user for input, check to see if the letter 'p' is in the input</p>

# In[1]:


Name = input("What is your name? : ").lower()
print("p" in Name)


# ## Using 'and'/'or' with If Statements

# In[7]:


if 100 == 100 or 34 == 304:
    print(True)
else:
    print(False)


# ### Elif Statements

# In[14]:


winning_number = 3
choice = int(input("Choose a winning number between 1 and 10: "))
if choice > winning_number:
    print("Go lower")
elif choice < winning_number:
    print("Go higher")
else:
    print("Correct")


# ### Else Statements

# # see above

# ### For Loops

# In[22]:


people = ['christian' , 'shoha', 'dylan']
for index in range(len(people)):
    print(index)
for index, name in enumerate(people):
    print(index,name)


# ##### Continue Statement

# In[23]:


# will continue to next iteration
for num in range(10):
    if num == 3:
        continue
    else:
        print(num)


# ##### Break Statement

# In[24]:


# will break out of current loop
for num in range(10):
    if num == 3:
        break
    else:
        print(num)


# ##### Pass Statement

# In[25]:


# mostly used as a placeholder, and will continue on same iteration
def using_pass_keyword():
    pass


# ##### Double For Loops

# In[26]:


colors = ['red','purple','blue']
items = ['car','phone','desk']

for color in colors:
    for item in items:
        print(color,item)


# ### While Loops

# In[28]:


num = 4
while num < 10:
    print(num)
    num = num + 1


# ##### Looping 'While True'

# In[ ]:


while True:
    winning_number = 3
    choice = int(input("Guess a number between 1 and 10:"))
    if winning_number == choice:
        print("Correct")
        break

correct_guess = False
while not correct_guess:
    winning_number = 3
    choice = int(input("Guess a number between 1 and 10:"))
    if winning_number == choice:
        print("Correct")
        correct_guess = True


# ##### While & For Loops Used Together

# In[1]:


counter = 0
while counter < 5:
    for num in range(2):
        print(counter)
        print('This is the for loop iterating inside of the while loop', num)
        counter += 1


# ### Built-In Functions

# ##### range()

# In[ ]:





# ##### len()

# In[ ]:





# ##### help() -  used to display the documentation of modules, functions, classes, keywords, etc. 

# In[2]:


print(help(str))


# ##### isinstance() - checks if the object is the type

# In[6]:


print(isinstance('Yo',str))


# ##### abs() - returns the absolute value

# In[7]:


print(abs(-5))


# ### Try and Except Blocks
# #### try - lets you test a block of code for errors
# #### except - lets you handle the error

# In[2]:


try:
    user_age = int(input("What is your age:"))
    print(user_age)
except ValueError:
    print("Please input a valid number")


# ### Lists

# ##### Declaring Lists

# In[2]:


print(list1
list1 = []


# ##### Indexing a List

# In[6]:


students = ['sj', 'shannon', 'emma','devin']
print(students[0:2])


# ##### .append()

# In[7]:


students = ['sj', 'shannon', 'emma','devin']
students.append("luke")
print(students)


# ##### .insert()

# In[11]:


students = ['sj', 'shannon', 'emma','devin']
students.insert(2,'luke')
print(students)


# ##### .pop()

# In[13]:


students.pop(1)
print(students)


# 
# ##### .remove() - removes element in a list, does not remove duplicates

# In[15]:


students.append('sj')
students.remove('sj')
print(students)


# ##### del()

# In[21]:


def delete_me():
    print("I am about to be deleted")
delete_me()
del delete_me
delete_me()


# ##### Concatenating Two Lists

# In[23]:


nfl = ['sea', 'yoyo']
nba = ['lakers', 'momo']
all = nfl + nba
print(all)


# ##### Lists Within Lists

# In[27]:


grades = [[2,3,4,2],[5,6,5,5],[1,1,1,1]]
print(grades[1][1])


# ##### Looping Through Lists

# In[31]:


nested_list = ['christian','dylan',['shoha','brandt','sam']]
print(nested_list[2][::])


# ## Exercise #1 <br>
# <p>Cube Number Test... Print out all cubed numbers up to the total value 1000. Meaning that if the cubed number is over 1000 break the loop.</p>

# In[2]:


num = 1
while (num**3)<1000:
    print(num**3)
    num += 1


# ## Exercise #2 <br>
# <p>Get first prime numbers up to 100</p>

# In[1]:


# HINT::
# An else after an if runs if the if didn’t
# An else after a for runs if the for didn’t break

num = 1
while num < 100:
    if num % 2 or if num % 3 or if num % 4 or if num % 5:
        print("Not Prime")
    else:
        print("Prime")


# # Exercise 3 <br>
# <p>Take in a users input for their age, if they are younger than 18 print kids, if they're 18 to 65 print adults, else print seniors</p>

# In[4]:


Age = int(input("What is your age?"))
if Age < 18:
    print("Kids")
elif Age < 65:
    print("Adults")
else:
    print("Seniors")


# In[ ]:





# In[ ]:




