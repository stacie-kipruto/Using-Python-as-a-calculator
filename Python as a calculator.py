#!/usr/bin/env python
# coding: utf-8

# ### 1. (a) Calculate the area of a triangle

# In[1]:


b= 55
h= 35
area = (0.5*b*h)
print(area)


# ### (b) Calculate the value of a sphere

# In[2]:


pi=3.142
r=7
volume= (4/3*pi*(r**3))
print(volume)


# ### (c) Calculate the volume of a cylinder (r=14)(h=12)

# In[3]:


pi= 3.142
r= 14
h=12
volume= (pi*(r**2)*h)
print(volume)


# ### (d) Calculate the density of a solid cone, mass (4.77) of a solid cone (rad=14) (hgt=20)

# In[4]:


pi= 3.142
hgt= 20
r= 14
v=(1/3*hgt*pi*(r**2))
print(v)
m= 4.77
density = (m/v*(1000))
print(density)


# ### 2. For each of the question above,output their type. Use fxn type()

# In[5]:


a= 962.5
type(962.5)


# In[6]:


b=1436.9413333333332
type(1436.9413333333332)


# In[7]:


c=7389.984
type(7389.984)


# In[8]:


d= 1.1618428402551346
type(1.1618428402551346)


# ### 3. For each of the question above convert the type of the answers to be integer types.

# In[9]:


int(a)


# In[10]:


int(b)


# In[11]:


int(c)


# In[12]:


int(d)


# ### 4. (a) The employee’s total taxable income (taxable_income) in that month

# In[35]:


taxable_income= 38892 + 2108
print(taxable_income)


# ### (b) the tax payable(tax_payable) by the employee in that month

# In[44]:


upper_a= 10164
lower_b= 0
a=((upper_a - lower_b)*0.1)
print (a)


# In[39]:


upper_b =19740
lower_b = 10165
b=((upper_b - lower_b)*0.15)
print(b)


# In[40]:


upper_c = 29316
lower_c = 19741
c=((upper_c - lower_c)*0.20)
print (c)


# In[41]:


upper_d = 38892
lower_d = 29317
d=((upper_d - lower_d)*0.25)
print(d)


# In[42]:


taxable_income=41000
lower_e=38892
e=((taxable_income-lower_e)*0.30)
print(e)


# In[49]:


tax_payable = a+b+c+d+e
print (tax_payable)


# ### (c)Calculate the employees net pay(net_pay) for that month

# In[47]:


basic_sal=41000
house= 15000
total_sal = (basic_sal + house)
print (total_sal)


# In[50]:


upper_limit= 56000
lower_limit = 38892
net_sal= ((upper_limit - lower_limit)*0.30)
print(net_sal)


# In[ ]:





# ### 5. Using an if -else control structure, create a program that asks a user for inputs

# In[14]:


age=int(input("How old are you : "))
name = input("what is your name: ")
req_age = 18
if age >= req_age: 
    print("Congratulations",name,"of age",age," you are legible for voting!")
else:
        print("you cannot vote",name)


# ### 6. A shop will give discount of 10% if the cost of purchased quantity is more than 1000. Ask user for quantity

# In[15]:


cost = 100
quantity = int(input("how many pieces are you buying "))
total_cost = quantity * cost
print(total_cost)
if total_cost > 1000: 
    total_cost = total_cost * 0.9
    print("your total cost is : ", total_cost)


# ### 7. Ask user for their salary and year of service and print the net bonus amount

# In[32]:


bonus = 5/100
salary = int(input("How much do you earn: "))
years_worked = int(input("how many years have you worked here: "))
years_to_qualify = 5
if years_worked >= years_to_qualify:
    bonus_amt = (bonus * salary)
    print("this is your new salary: " + bonus_amt)
else:
    if years_worked <= years_to_qualify:
        bonus_amt= salary
        print("you do not qualify for a bonus")


# ### 8. Ask user to enter marks and print the corresponding grade. 

# In[18]:


points = int(input("enter your marks: "))
if points <=100 and points >=80:
    print("A")
elif points <80 and points >=60:
    print ("B")
elif points <60 and points >= 50:
    print ("C")
elif points <50 and points >=45:
    print ("D")
elif points <45 and points >= 25:
    print ("E")
elif points <25 and points >= 0:
    print ("F")
else:
    print ("Invalid Option")


# ### 9. A student will not be allowed to sit in exam if his/her attendance is less than 75%

# In[19]:


class_held = int(input("Number of classes held: "))
class_attended = int(input("Number of classes attended: "))
percentage = class_attended/class_held*100
if percentage >=75:
    print ("the student is allowed to sit for the exams")
else:
    print ("the student is not allowed to sit for the exam")


# In[33]:


import math #to import mathematical values if you are not sure of the values

print(math.pi)

