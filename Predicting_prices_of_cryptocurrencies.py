#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from pandas_datareader import data as wb


# In[2]:


import matplotlib.pyplot as plt
from scipy.stats import norm
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


cryptos=['BTC-USD','ETH-USD','XRP-USD','LTC-USD','DOGE-USD']
data=pd.DataFrame()
for c in cryptos:
    data[c]=wb.DataReader(c,data_source='yahoo',start='2018-1-1')['Adj Close']


# In[4]:


data


# In[5]:


#Predicting the price of BITCOIN 


# In[6]:


mydata=pd.DataFrame()
crypto="BTC-USD"
mydata[crypto]=wb.DataReader(crypto,data_source="yahoo",start="2018-1-1")['Adj Close']


# In[7]:


mydata.head()


# In[8]:


mydata.tail()


# In[9]:


#Plot for bitcoin till date
mydata.plot(figsize=(10,6))


# In[10]:


log_of_returns=np.log(1+mydata.pct_change())


# In[11]:


log_of_returns


# In[12]:


#Plot of log(returns) till date
log_of_returns.plot(figsize=(10,6))


# In[13]:


#Calculating mean and variance of log of returns
mean=log_of_returns.mean()
print(mean)
var=log_of_returns.var()
print(var)


# In[14]:


#Calculating drift which is the first component
#drift = mean - 0.5 * variance


# In[15]:


drift=mean-(0.5*var)
drift


# In[16]:


stdev=log_of_returns.std()
stdev


# In[17]:


np.array(drift)
drift.values


# In[18]:


stdev.values


# In[19]:


#Calculating volatility of cryptocurrency , which is the second component
days=100
iterations=10


# In[20]:


daily_return=np.exp(drift.values+stdev.values*norm.ppf(np.random.rand(days,iterations)))


# In[21]:


daily_return


# In[22]:


recent_price=mydata.iloc[-1]
recent_price


# In[23]:


predicted_price=np.zeros_like(daily_return)
predicted_price


# In[24]:


predicted_price[0]=recent_price
predicted_price


# In[25]:


for day in range(1,days):
    predicted_price[day]=predicted_price[day-1]*daily_return[day]


# In[26]:


predicted_price


# In[27]:


print("The plot of predicted prices (for next 100 days) of BITCOIN by performing 10 simulations ")
plt.figure(figsize=(10,6))
plt.plot(predicted_price);


# In[28]:


#Predicting Bitcoin prices for next 6 months(180 days)


# In[29]:


days=180


# In[30]:


daily_return=np.exp(drift.values+stdev.values*norm.ppf(np.random.rand(days,iterations)))


# In[31]:


predicted_price=np.zeros_like(daily_return)
predicted_price[0]=recent_price
for day in range(1,days):
    predicted_price[day]=predicted_price[day-1]*daily_return[day]
predicted_price


# In[32]:


print("The plot of predicted prices (for next 180 days) of BITCOIN by performing 10 simulations ")
plt.figure(figsize=(10,6))
plt.plot(predicted_price);


# In[33]:


#Predicting the price of ETHEREUM


# In[34]:


mydata=pd.DataFrame()
crypto="ETH-USD"
mydata[crypto]=wb.DataReader(crypto,data_source="yahoo",start="2018-1-1")['Adj Close']


# In[35]:


mydata.tail()


# In[36]:


#Plot for ethereum till date
mydata.plot(figsize=(10,6))


# In[37]:


log_of_returns=np.log(1+mydata.pct_change())
log_of_returns


# In[38]:


#Calculating mean and variance of log of returns
mean=log_of_returns.mean()
print(mean)
var=log_of_returns.var()
print(var)


# In[39]:


#Calculating drift which is the first component
#drift = mean - 0.5 * variance


# In[40]:


drift=mean-(0.5*var)
drift


# In[41]:


stdev=log_of_returns.std()
stdev


# In[42]:


np.array(drift)
drift.values


# In[43]:


stdev.values


# In[44]:


#Calculating volatility of cryptocurrency , which is the second component
days=100
iterations=10


# In[45]:


daily_return=np.exp(drift.values+stdev.values*norm.ppf(np.random.rand(days,iterations)))
daily_return


# In[46]:


recent_price=mydata.iloc[-1]
recent_price


# In[47]:


predicted_price=np.zeros_like(daily_return)
predicted_price


# In[48]:


predicted_price[0]=recent_price
predicted_price


# In[49]:


for day in range(1,days):
    predicted_price[day]=predicted_price[day-1]*daily_return[day]


# In[50]:


predicted_price


# In[51]:


print("The plot of predicted prices (for next 100 days) of ETHEREUM by performing 10 simulations ")
plt.figure(figsize=(10,6))
plt.plot(predicted_price);


# In[52]:


#Predicting ETHEREUM prices for next 6 months(180 days)


# In[53]:


days=180


# In[54]:


daily_return=np.exp(drift.values+stdev.values*norm.ppf(np.random.rand(days,iterations)))
predicted_price=np.zeros_like(daily_return)
predicted_price[0]=recent_price
for day in range(1,days):
    predicted_price[day]=predicted_price[day-1]*daily_return[day]
predicted_price


# In[55]:


print("The plot of predicted prices (for next 180 days) of ETHEREUM by performing 10 simulations ")
plt.figure(figsize=(10,6))
plt.plot(predicted_price);


# In[56]:


#Predicting the price of RIPPLE


# In[57]:


mydata=pd.DataFrame()
crypto="XRP-USD"
mydata[crypto]=wb.DataReader(crypto,data_source="yahoo",start="2019-1-1")['Adj Close']
mydata.tail()


# In[58]:


#Plot for Ripple till date
mydata.plot(figsize=(10,6))


# In[59]:


log_of_returns=np.log(1+mydata.pct_change())
log_of_returns


# In[60]:


#Calculating mean and variance of log of returns
mean=log_of_returns.mean()
print(mean)
var=log_of_returns.var()
print(var)


# In[61]:


#Calculating drift which is the first component
#drift = mean - 0.5 * variance


# In[62]:


drift=mean-(0.5*var)
drift


# In[63]:


stdev=log_of_returns.std()
stdev


# In[64]:


np.array(drift)
drift.values


# In[65]:


stdev.values


# In[66]:


#Calculating volatility of cryptocurrency , which is the second component
days=100
iterations=10


# In[67]:


daily_return=np.exp(drift.values+stdev.values*norm.ppf(np.random.rand(days,iterations)))
daily_return


# In[68]:


recent_price=mydata.iloc[-1]
recent_price


# In[69]:


predicted_price=np.zeros_like(daily_return)


# In[70]:


predicted_price[0]=recent_price


# In[71]:


for day in range(1,days):
    predicted_price[day]=predicted_price[day-1]*daily_return[day]


# In[72]:


predicted_price


# In[73]:


print("The plot of predicted prices (for next 100 days) of RIPPLE by performing 10 simulations ")
plt.figure(figsize=(10,6))
plt.plot(predicted_price);


# In[74]:


#Predicting Ripple prices for next 6 months(180 days)


# In[75]:


days=180


# In[76]:


daily_return=np.exp(drift.values+stdev.values*norm.ppf(np.random.rand(days,iterations)))
predicted_price=np.zeros_like(daily_return)
predicted_price[0]=recent_price
for day in range(1,days):
    predicted_price[day]=predicted_price[day-1]*daily_return[day]
predicted_price


# In[77]:


print("The plot of predicted prices (for next 180 days) of RIPPLE by performing 10 simulations ")
plt.figure(figsize=(10,6))
plt.plot(predicted_price);


# In[78]:


#Predicting the price of LITECOIN


# In[79]:


mydata=pd.DataFrame()
crypto="LTC-USD"
mydata[crypto]=wb.DataReader(crypto,data_source="yahoo",start="2019-1-1")['Adj Close']
mydata.tail()


# In[80]:


#Plot for Litecoin till date
mydata.plot(figsize=(10,6))


# In[81]:


log_of_returns=np.log(1+mydata.pct_change())
log_of_returns


# In[82]:


#Calculating mean and variance of log of returns
mean=log_of_returns.mean()
print(mean)
var=log_of_returns.var()
print(var)


# In[83]:


#Calculating drift which is the first component
#drift = mean - 0.5 * variance


# In[84]:


drift=mean-(0.5*var)
drift


# In[85]:


stdev=log_of_returns.std()
stdev


# In[86]:


np.array(drift)
drift.values


# In[87]:


stdev.values


# In[88]:


#Calculating volatility of cryptocurrency , which is the second component
days=100
iterations=10


# In[89]:


daily_return=np.exp(drift.values+stdev.values*norm.ppf(np.random.rand(days,iterations)))
daily_return


# In[90]:


recent_price=mydata.iloc[-1]
recent_price


# In[91]:


predicted_price=np.zeros_like(daily_return)


# In[92]:


predicted_price[0]=recent_price


# In[93]:


for day in range(1,days):
    predicted_price[day]=predicted_price[day-1]*daily_return[day]


# In[94]:


predicted_price


# In[95]:


print("The plot of predicted prices (for next 100 days) of LITECOIN by performing 10 simulations ")
plt.figure(figsize=(10,6))
plt.plot(predicted_price);


# In[96]:


#Predicting Litecoin prices for next 6 months(180 days)


# In[97]:


days=180


# In[98]:


daily_return=np.exp(drift.values+stdev.values*norm.ppf(np.random.rand(days,iterations)))
predicted_price=np.zeros_like(daily_return)
predicted_price[0]=recent_price
for day in range(1,days):
    predicted_price[day]=predicted_price[day-1]*daily_return[day]
predicted_price


# In[99]:


print("The plot of predicted prices (for next 180 days) of LITECOIN by performing 10 simulations ")
plt.figure(figsize=(10,6))
plt.plot(predicted_price);


# In[100]:


#Predicting the price of DOGECOIN


# In[101]:


mydata=pd.DataFrame()
crypto="DOGE-USD"
mydata[crypto]=wb.DataReader(crypto,data_source="yahoo",start="2018-1-1")['Adj Close']
mydata.tail()


# In[102]:


#Plot for Dogecoin till date
mydata.plot(figsize=(10,6))


# In[103]:


log_of_returns=np.log(1+mydata.pct_change())
log_of_returns


# In[104]:


#Calculating mean and variance of log of returns
mean=log_of_returns.mean()
print(mean)
var=log_of_returns.var()
print(var)


# In[105]:


#Calculating drift which is the first component
#drift = mean - 0.5 * variance


# In[106]:


drift=mean-(0.5*var)
drift


# In[107]:


stdev=log_of_returns.std()
stdev


# In[108]:


np.array(drift)
drift.values


# In[109]:


stdev.values


# In[110]:


#Calculating volatility of cryptocurrency , which is the second component
days=100
iterations=10


# In[111]:


daily_return=np.exp(drift.values+stdev.values*norm.ppf(np.random.rand(days,iterations)))
daily_return


# In[112]:


recent_price=mydata.iloc[-1]
recent_price


# In[113]:


predicted_price=np.zeros_like(daily_return)


# In[114]:


predicted_price[0]=recent_price


# In[115]:


for day in range(1,days):
    predicted_price[day]=predicted_price[day-1]*daily_return[day]


# In[116]:


predicted_price


# In[117]:


print("The plot of predicted prices (for next 100 days) of DOGECOIN by performing 10 simulations ")
plt.figure(figsize=(10,6))
plt.plot(predicted_price);


# In[118]:


#Predicting Dogecoin prices for next 6 months(180 days)


# In[119]:


days=180


# In[120]:


daily_return=np.exp(drift.values+stdev.values*norm.ppf(np.random.rand(days,iterations)))
predicted_price=np.zeros_like(daily_return)
predicted_price[0]=recent_price
for day in range(1,days):
    predicted_price[day]=predicted_price[day-1]*daily_return[day]
predicted_price


# In[121]:


print("The plot of predicted prices (for next 180 days) of DOGECOIN by performing 10 simulations ")
plt.figure(figsize=(10,6))
plt.plot(predicted_price);


# In[ ]:




