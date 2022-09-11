#!/usr/bin/env python
# coding: utf-8

# In[1]:


print ("hello world")


# In[4]:


k=2+3J


# In[5]:


7//2


# In[6]:


"s"*2


# In[7]:


var@check1=10


# In[8]:


x=3
y=6


# In[9]:


x,y=y,x


# In[10]:


x


# In[11]:


y=1**2**3**2


# In[12]:


y


# In[10]:


b=5|2


# In[11]:


b


# In[12]:


type(b)


# In[13]:


c=5/2


# In[14]:


c


# In[15]:


type(c)


# In[3]:


1|2


# In[ ]:





# In[7]:


k=5%2


# In[8]:


k


# In[9]:


type(k)


# In[19]:


6/3.3


# In[22]:


x=6//3.5


# In[23]:


x


# In[24]:


type(x)


# In[25]:


answer1= True
answer2 = False
print(answer1*answer2)


# # Numpy 
*Numpy is a python package and it stands for Numerical python
*Fundamental package for numerical computations in python
*Support N- dimensional array objects that can be used for processing multidimensional data
*Support different Data Types
# ## Numpy Array
*A Numpy Array is a grid of values,all of the same type, and is indexed by tuples of non negative integers
*The number of dimensions is the rank of array
*The Shape of Array is tuple of integers giving the size of the array along each dimension
# ## Creation of Array

# In[1]:


my_list=[1,2,3,4,5,6]
print(my_list)


# In[2]:


import numpy as np


# In[9]:


array=np.array(my_list, dtype=int )


# In[10]:


array


# In[12]:


print(type(array))
print(len(array))
print(array.ndim)
print(array.shape)


# In[26]:


array2=array.reshape(3,2)
print(array2)
print(array2.shape)
array3.ndim


# In[40]:


array3=array.reshape(3,-1)
print(array3)
print(array3.ndim)


# In[42]:


#Initialising numpy arrays from nested python list
my_list2=[1,2,3,4,5,6]
my_list3=[2,3,4,5,6,7]
my_list4=[3,4,5,6,7,8]
mul_array=np.array([my_list2,my_list3,my_list4])
print(mul_array)
print(mul_array.shape)


# In[47]:


mul_array.reshape(1,18)


# 
# # Numpy- Attributes

# In[50]:


a=np.array([[1,2,3],[2,3,4]])
print(a.shape)


# In[53]:


#reshaping the array
a.shape=(3,2)
print(a)


# In[55]:


#reshape function for resizing the array
b=a.reshape(2,3)
print(b)


# In[57]:


r=range(24)
print(r)


# In[58]:


#an array of evenly spaced number
a=np.arange(24)
print(a)
print(a.ndim)


# In[61]:


#Reshaping the array 'a'
b=a.reshape(6,4)
print(b)


# In[62]:


b=a.reshape(6,4,1)
print(b)


# In[66]:


x=np.array([[1,2],[3,4]],dtype=float)
y=np.array([[5,6],[7,8]],dtype=float)
print(x)
print(y)


# # numpy.add() perform elementwise addition between two arrays

# In[67]:


print(x+y)
np.add(x,y)


# # numpy.subtract () perform elementwise subtraction between two arrays

# In[69]:


print(x-y)
np.subtract(x,y)


# # numpy.multiply () perform elementwise multiplication between two arrays

# In[70]:


print(x*y)
np.multiply(x,y)


# In[71]:


print(x.dot(y))
np.dot(x,y)


# In[72]:


print(x/y)
np.divide(x,y)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# # numpy.sum () returns sum of all array element along axis

# In[73]:


print(np.sum(x))
print(x)


# In[74]:


print(np.sum(x, axis=0))
print(x)


# In[75]:


print(np.sum(x, axis=1))
print(x)


# # Reading Data
*File format :- 
   *Standard way in which Dta is collected and stored
   *Most Commonly used format for stroing data is the       spreadsheet format where data is stored in rows &       columns.
        *Each row is called a record
        *each column in spreadsheet holds data belonging 
         to same data type
    *commonly used spreadsheet formats are comma
    separated values and excel sheets
    *other formats include plain text,json,html,mp3,mp4 
    etc.
     
# ## Comma Separated value
 *spreadsheet format
 *Format '.csv'
 *Each record is separeted by comma
 *Files where records are separeted using a tab are
  are called Tab separated values
 *'.csv' files can be open by Notepad or MS Excel
# ## Excel spreadsheet
 *spreadsheet format
 *Part of Microsoft Office
 *Format '.xlsx'
# ## Text format
 *Consist of Plain text or records
 *Format '.text'
# In[9]:


#Importing Data
import os


# In[10]:


import pandas as pd #pandas Library is to work with dataframes


# In[11]:


data_csv=pd.read_csv('iris.xlsx')


# In[16]:


os.chdir("C:\\Users\\Dll\\anaconda3\\Lib\\site-packages\\astropy\\io\\misc\\pandas")


# In[29]:


data_csv=pd.read_csv("C:\\Users\\Dll\\anaconda3\\Lib\\site-packages\\bokeh\\sampledata\\_data\\iris.csv")


# In[30]:


data_csv


# In[28]:


#Blank cells read as "nan"


# In[34]:


data_csv=pd.read_csv("C:\\Users\\Dll\\anaconda3\\Lib\\site-packages\\bokeh\\sampledata\\_data\\iris.csv")


# In[35]:


data_csv


# In[36]:


#removing column 0
data_csv=pd.read_csv("C:\\Users\\Dll\\anaconda3\\Lib\\site-packages\\bokeh\\sampledata\\_data\\iris.csv" ,index_col=0) #removing column


# In[38]:


data_csv


# In[39]:


#junk values can be converted to missing values with 'na_values'
data_csv=pd.read_csv("C:\\Users\\Dll\\anaconda3\\Lib\\site-packages\\bokeh\\sampledata\\_data\\iris.csv" ,index_col=0, na_values=["??","##"])


# In[40]:


data_csv


# In[50]:


data_xlsx=pd.read_excel("C:\\Users\\Dll\\anaconda3\\Lib\\site-packages\\bokeh\\sampledata\\_data\\iris.xlsx" )


# In[51]:


data_xlsx


# In[52]:


#sheet_name='iris_data'
#remove index column and replace'?? as missing values


# In[53]:


#Text format
data_txt=pd.read_table("C:\\Users\Dll\\Downloads\\PyDev 9.2.0\\plugins\\org.python.pydev.shared_core_9.2.0.202110311311\\libs\\README.txt")


# In[54]:


data_txt


# # PANDAS 
 *Provide high performance ,easy to use Data structures
  and   analysis tools for the python programming lang.
 *Open source Pyhton library providing high performance 
  data manipulation and analysis tool using its powerful
  Data structures
 *Name Pandas is derived from the word Panel Data - an 
  econometrics term for multidimensional data *Pandas deals with dataframes :-
  
  DataFrames    2      *two-dimensional size mutable
                       *potentially heterogeneous tabular
                        data structure with labeled axes 
                        (rows and column)
# In[1]:


#imort data 
#import data to jupyter


# ## Creating copy of original data

# In[ ]:


#Shallow copy
Functiom: samp=cars_data.copy(deep=false)
          samp= cars_data
Description: *It only creates new variable that shares the
              reference of original object
             *Any changes made to a copy of object will be
              reflected in original object as well

#Deep copy
Function: samp=cars_dat.copy(deep=True)
Description: *In case of Deep copy, a copy of object is
              is copied in other object with no reference
              to the original
             *Any changes made to a copy of object will not
              be reflected in the original object.
                


# ## Atttributes of Data 

# In[13]:


data_xlsx=pd.read_excel("C:\\Users\\Dll\\anaconda3\\Lib\\site-packages\\bokeh\\sampledata\\_data\\iris.xlsx" )


# In[14]:


data_xlsx


# In[31]:


data_xlsx.index


# In[16]:


data_xlsx.columns


# In[17]:


data_xlsx.size #total no. of element


# In[26]:


data_xlsx.shape #no. of rows and column


# In[24]:


data_xlsx.memory_usage() #memory used by each column in bytes


# In[27]:


data_xlsx.ndim #no.of axes/array in dataframes


# ## Indexing and selecting Data 

# In[ ]:


*Python slicing operator '[]' and attribute/dot operator
 '.' are used for indexing
*Provides quick and easy access to Pandas data structure


# In[32]:


data_xlsx.head(6) #by defalt it gives first 5 rows


# In[33]:


data_xlsx.tail(6) #last n rows from data frames


# In[36]:


#to access a scalar value, the fastest ways to use the 'at' & 'iat' methods
data_xlsx.at[110,'petal_width'] #at provides label based scaler lookups


# In[38]:


data_xlsx.iat[144,2] #iat provides integer based lookups


# In[39]:


#to access a group of rows and columns by label(s).loc[] can be used
data_xlsx.loc[:,'sepal_length']


# In[ ]:




