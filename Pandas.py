#!/usr/bin/env python
# coding: utf-8

# In[49]:


#importing pandas
import pandas as pd


# *Pandas allows us to load a spreadsheet and manipulate it programmatically in python. The central concept in pandas is the type of object called a DataFrame – basically a table of values which has a label for each row and column. Let’s load this basic CSV file containing data from a NewYork city weather:*

# In[50]:


#Here read_csv is the method for reading csv file into dataframe.
#csv file is comma-separated values
dataframe = pd.read_csv("nyc_weather.csv")
print(dataframe)


# In[51]:


#get maximum temperature 
print(dataframe["Temperature"].max())


# In[52]:


#If you want to know which days it rains
print(dataframe['EST'][dataframe['Events']=='Rain'])


# In[53]:


#printing Average wind speed
print(dataframe['WindSpeedMPH'].mean())


# *DataFrame is main object in pandas, it is used to represent data with rows and columns.*
# *DataFrame is data structure represent the data in tabular or excel spreadsheet like data*

# In[54]:


#creating dataframe from csv file
dataframe = pd.read_csv("Weather_data.csv") 
print(dataframe)


# In[55]:


#creating dataframe from tuples

weather_data = [('1/1/2017',32,6,'Rain'),('1/2/2017',35,7,'Sunny'),('1/3/2017',28,2,'Snow'),('1/4/2017',24,7,'Snow'),('1/5/2017',32,4,'Rain'),('1/6/2017',31,2,'Sunny')]
dataframe1 = pd.DataFrame(weather_data,columns=['day','temperature','windspeed','event'])
print(dataframe1)


# In[56]:


# get dimentions of table
print(dataframe.shape)


# In[57]:


#printing initial rows
print(dataframe.head())
print(dataframe.head(2))


# In[58]:


#printing last rows
print(dataframe.tail())
print(dataframe.tail(2))


# In[59]:


#printing data from 2 to 5 using slicing
print(dataframe[2:5])


# In[60]:


#printing columns of dataframe
print(dataframe.columns)


# In[61]:


#printing particular column data
print(dataframe.day)
print(dataframe.temperature)
#another way of accessing column
print(dataframe['day'])


# In[62]:


#for getting two or more columns together
print(dataframe[['day','temperature']])
print(dataframe[['day','temperature','event']])


# In[63]:


#printing maximum and minimum of temperature
print(dataframe['temperature'].max())
print(dataframe['temperature'].min())


# In[64]:


#printing statistical data of pandas
print(dataframe['temperature'].describe())


# In[65]:


#printing rows which has maximum temperature
print(dataframe[dataframe.temperature == dataframe.temperature.max()])


# In[66]:


#printing only day column which has maximum temperature
print(dataframe.day[dataframe.temperature == dataframe.temperature.max()])


# # Read and Write CSV and XLS files

# In[67]:


#read excel file 
dataframe = pd.read_excel('weather_data.xlsx')
print(dataframe)


# In[68]:


#write DataFrame to csv file
dataframe.to_csv('new.csv')


# In[69]:


#writing DataFrame to excel file
dataframe.to_excel('new.xlsx')


# In[70]:


#group by using pandas

dataframe = pd.read_csv('weather_data_cities.csv')
print(dataframe)


# In[71]:


x = dataframe.groupby('city')
print(x)


# In[72]:


for i,j in x:
    print(i)
    print(j)


# In[74]:


#printing specific group
x.get_group('new york')


# In[75]:


#printing maximum temperature from all cities
print(x.max())


# In[76]:


#other statistical operations
print(x.mean())


# In[77]:


print(x.median())


# In[79]:


print(x.describe())


# In[83]:


#concatenate of two dataframes

dataframe_1 = pd.DataFrame({
        'city':['mumbai','surat','ahmedabad'],
        'temperature':[32,45,30],
        'humidity':[80,60,78]
})

print(dataframe_1)

dataframe_2 = pd.DataFrame({
        'city':['New york','chicago','orlando'],
        'temperature':[21,14,35],
        'humidity':[68,65,75]
})

print(dataframe_2)

dataframe_3 = pd.concat([dataframe_1,dataframe_2])
print(dataframe_3)


# In[84]:


#if you want continuous index
dataframe_4 = pd.concat([dataframe_1, dataframe_2], ignore_index=True)
print(dataframe_4)


# In[86]:


#if you want to concat column wise
dataframe_5 = pd.concat([dataframe_1,dataframe_2],axis=1)
print(dataframe_5)


# In[89]:


#merge dataframes

dataframe_1 = pd.DataFrame({
        'city':['Ahmedabad','delhi','mumbai','goa'],
        'temperature':[45,32,45,78]
})

print(dataframe_1)

dataframe_2 = pd.DataFrame({
        'city':['Ahmedabad','delhi','mumbai'],
        'humidity':[115,112,78]
})

print(dataframe_2)

dataframe_3 = pd.merge(dataframe_1,dataframe_2,on='city')
print(dataframe_3)


# In[90]:


#outer join
dataframe_4 = pd.merge(dataframe_1,dataframe_2,on='city',how='outer')
print(dataframe_4)


# In[91]:


#Numerical indexing
dataframe = pd.DataFrame([1,2,3,4,5,6,7,8,9,19],index = [49,48,47,46,45,1,2,3,4,5])
print(dataframe)


# In[93]:


#till index 2
dataframe.loc[:2]


# In[94]:


#till position 2
dataframe.iloc[:2]

