#!/usr/bin/env python
# coding: utf-8

# # Assignment 01

# # Question 1

# In[1]:


name=input('enter the name=')


# In[2]:


rollnumber =input('enter the roll number=')


# In[3]:


mark=input('enter the mark=')


# In[7]:


print('name:',name)
print ('roll number:',rollnumber)
print('mark:',mark)


# ## Question 2

# In[219]:


c=5
f=-32/9


# In[220]:


c=(f-32)*5/9


# In[221]:


print(input('c'))


# In[222]:


c=5
f=32/9


# In[223]:


f=(c*9/5)+32


# In[224]:


print (input(f))


# # Question 3 

# In[41]:


a=input('first number=')
b=input('second number=')
product=int(a)*int(b)
print('product=', product)


# # Question 4

# In[148]:


string=input('enter the sentence')
string1=string.replace('python','**python**')
string2=string1.replace('website','**website**')
print(string + string2)


# # Question 5

# In[82]:


r=float(input('enter the radius'))
area=3.14*r*r
print(area)


# # Question 6

# In[83]:


list=[1,2,3,4,5]
num=int(input('enter a number to insert in list :'))
index=int(input('enter a intex to insert value:'))
list.insert(index,num)
print('array after inserting',num,'=', list)


# # Question 7

# In[91]:


sample_dict= {'name':'john','age':5,'salary':8000,'city':'new york'}
print('initial dictionary',sample_dict)
sample_dict['location']=sample_dict['city']
del sample_dict['city']
print('final dictionary',sample_dict)


# # Question 8

# In[194]:


sample_dict={'emp1':{'name':'john','salary':7500},
             'emp2':{'name':'emma','salary':8000},
             'emp3':{ 'name':'brad','salary':500}}
sample_dict['emp3']['salary']=8500
sample_dict


# # Question 9

# In[92]:


tuple1=(10,20,43,54,56,68)
tuple2=tuple1[2:4]
print(tuple2)


# # question 10

# In[93]:


tuple=( 50,10,60,70,50,83,567,50,81)
print(tuple.count(50))


# In[ ]:




