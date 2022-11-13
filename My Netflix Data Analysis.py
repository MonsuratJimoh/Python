#!/usr/bin/env python
# coding: utf-8

# NETFLIX DATA ANALYSIS

# In[1]:


#IMPORT ALL THE NECESSARY LIBRARIES
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


#read the cvs file
Netflix = pd.read_csv('netflix_titles.csv')


# In[3]:


Netflix


# In[4]:


Netflix = Netflix.copy() #this copies the data (continue to work with the copy of the data)


# In[5]:


Netflix  


# In[6]:


Netflix.head() #explores the first 5 rows of the data


# In[7]:


Netflix.tail() #explores the last 5 entries (rows) of the data set


# In[8]:


# exploring the numeric data (infomation) in the data set
Netflix.describe() 


# In[9]:


#Checking for the missing values (or null values)in the data
Netflix.isnull().sum()


# In[10]:


#Dropping the show_id column
Netflix = Netflix.drop(columns=('show_id'))


# In[11]:


Netflix.head()


# In[12]:


#exploring the overview of the entire data set
Netflix.info()


# In[13]:


#dropping the few null rows
Netflix= Netflix.dropna(subset = ['date_added', 'rating', 'duration'])


# In[14]:


# checking of the indicated null row as been dropped
Netflix.isnull().sum()


# In[15]:


#filling the null rows in the directors column
Netflix['director'] = Netflix['director'].fillna('Not specified')


# In[16]:


Netflix['cast'] = Netflix['cast'].fillna('Not listed')


# In[17]:


Netflix['country'] = Netflix['country'].fillna('Not indicated')


# In[18]:


#Ensuring there are no missing values
Netflix.isnull().sum()


# In[19]:


#Converting the duration to interger
Netflix['duration'] = Netflix['duration'].str.strip('min')
Netflix['duration'] = Netflix['duration'].str.strip('Season')
Netflix['duration'] = Netflix['duration'].str.strip('Seasons')


# In[20]:


Netflix.head() #displays the results of code in [24]


# In[21]:


#removing the extra white space and converting duration value to integer
Netflix['duration'] = Netflix['duration'].str.strip(' ').astype(int)


# In[22]:


Netflix.describe() #code assess the numeric data in the data set


# In[23]:


# assess the counts and data types in the 'type' column 
Netflix['type'].value_counts() 


# DISTRUBUTION OF MOVIES AND TV SHOW

# In[24]:


plt.pie(Netflix['type'].value_counts(),
        labels = Netflix['type'].value_counts().index, 
        colors = ['green', 'purple'], startangle = 90,
        autopct = '%1.1f%%',
       )
plt.legend()


# In[25]:


#the pie chart indicated that there are much more movie produced compared to TV shows


# # Top Directors

# In[26]:


#Getting the counts of directors in the data set
Netflix['director'].value_counts()  #gives the total numbers of counts of directors in the data set


# MOVIE SUBSET

# In[27]:


# SUBSET THE ENTIRE DATA TO INCLUDE ONLY MOVIE
Netflix_movie = Netflix[Netflix['type'] == 'Movie']
Netflix_movie.head()


# In[28]:


#assess the numbers of counts for directors of Movie
Netflix_movie['director'].value_counts()


# In[29]:


#some of the directors appears in twos, since some movies are directed by two people, the directors will be splited as follows:
movie_directors = Netflix_movie['director'].str.split(',', expand=True).stack()
movie_directors


# In[30]:


#counting the numbers of movie directors
movie_directors.value_counts() 


# In[31]:


#convert to dataframe
movie_directors = pd.DataFrame(movie_directors)


# In[32]:


movie_directors.head() # shows the first few(5)rows


# In[33]:


#Name the column
movie_directors.columns =['Directors'] 
movie_directors.head()


# In[34]:


#select only the known directors
movie_directors = movie_directors[movie_directors['Directors'] != 'Not specified'] 
movie_directors = movie_directors.groupby(['Directors']).size().reset_index(name='Total Movies') #CODE NOT CLEAR!!!


# In[35]:


Top_directors = pd.DataFrame(movie_directors.sort_values(by=['Total Movies'], ascending =False)).head(10)
Top_directors


# In[36]:


#Visualise the Top movie directors
sns.barplot(y='Directors', x='Total Movies', data = Top_directors, color= 'purple')
plt.title('Top Movie Director')


# In[37]:


#The plot above indicated that Rajiv Chilaka is the Topmost Movie Producer


# # Movie duration Distribution 

# In[ ]:




