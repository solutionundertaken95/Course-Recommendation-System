
# coding: utf-8

# In[25]:


import pandas as pd
import joblib


# In[26]:


def predict(df):


	#df=pd.read_csv("test.csv")
	#df.head()
	df=pd.DataFrame(df)
	print("data:",df)


	# In[27]:


	clf=joblib.load("ML/model.joblib")
	le=joblib.load("ML/label.joblib")


	# In[28]:


	file=open("ML/maps.txt","r")
	maps=eval(file.read())
	file.close()


	# In[29]:


	"""for i in list(maps.keys()):
		df[i].replace(maps[i],inplace=True)
		print(i)"""


	# In[34]:


	pred=le.inverse_transform(clf.predict(df))[0]


	# In[35]:


	#print(pred)
	return pred
	
#result=predict()
#print("Result:",result)

