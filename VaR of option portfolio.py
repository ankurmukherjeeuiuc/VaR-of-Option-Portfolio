#!/usr/bin/env python
# coding: utf-8

# In[38]:


import numpy as np
import scipy.stats as si

def bs(S,K,T,r,sigma,option):
    d1 = (np.log(S/K) + (r+((sigma**2)/2)) * T)/(sigma * np.sqrt(T))
    d2 = d1 - (sigma * np.sqrt(T))
    
    if option == 'call':
        result = (S * si.norm.cdf(d1, 0.0, 1.0) - K * np.exp(-r * T) * si.norm.cdf(d2, 0.0, 1.0))
    if option == 'put':
        result = (K * np.exp(-r * T) * si.norm.cdf(-d2, 0.0, 1.0) - S * si.norm.cdf(-d1, 0.0, 1.0))
        
    return result
    


# In[39]:


bs(101.17,100,.083333,.01,0.45,option = 'put')


# In[ ]:





# In[40]:


#ds = udt + sigmadz
def gbm(u,stdev,dt):
    dz = np.random.normal(u,stdev)
    ds = u*dt + stdev*dz    
    return ds    


# In[41]:


trials = 10000
p=[]

for i in range(trials):
    #ABC stock
    ds_ABC = gbm(0.0005*21,0.028*np.sqrt(21),21)
    y = 101.17+ds_ABC
    call_ABC =  bs(y,100,.083333,.01,0.45,option = 'call')
    put_ABC =   bs(y,100,.083333,.01,0.45,option = 'put')
    portfolio_ABC = 6000*(call_ABC + put_ABC)
    #DEF
    ds_DEF = gbm(0.0004*21,0.023*np.sqrt(21),21)
    z = 148.97+ds_DEF
    call_DEF =  bs(z,150,.083333,.01,0.37,option = 'call')
    put_DEF =   bs(z,150,.083333,.01,0.37,option = 'call')
    portfolio_DEF = 4000*(call_DEF + put_DEF)
    #Total
    total_portfolio_value = portfolio_ABC + portfolio_DEF 
    p.append(total_portfolio_value)    

#sort ascending order
p.sort()
#1% 21d Var
var_21d = p[99]
print(var_21d)


# In[ ]:




