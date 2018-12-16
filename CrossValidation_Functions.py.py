# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 14:48:18 2018

@author: RomanGutin
"""
import numpy as np
import pandas as pd
from sklearn.utils import shuffle
import matplotlib.pyplot as plt
### CrossValidation Score Functions###
def concat_train(x):  #I wrote this function to convert the list of training dataframes into a single dataframe, 
    for j in range(len(x)):  #Helper function in CrossValidation(.)
        if j==0:
            concat_set=[]                          
            concat_set.append(x[j])
        else:
            concat_set= concat_set
            concat_set.append(x[j])
            train_data=pd.concat(concat_set)
    return(train_data)
    
def MLE(df):
   x= df.iloc[:,0:len(df.columns)-1] 
   x = np.array(x.values, dtype=[('O', np.float)]).astype(np.float)                                        #Function that gives the MLE Regression Coefficents 
   y= df.iloc[:,len(df.columns)-1]
   y = np.array(y.values, dtype=[('O', np.float)]).astype(np.float)
   xT_dot_x= pd.DataFrame(np.dot(x.T,x))
   noise = 1E-6*np.random.rand(len(xT_dot_x.iloc[:,]),len(xT_dot_x.iloc[0,:]))
   theta = np.dot(np.dot(np.linalg.inv((np.dot(x.T,x))+noise),x.T),y)
   return(theta)
   
def CV_split(x,n):   #General function that splits dataframe of any size into n-parts and saves to a list called 'sets'
    sets=[]
    for i in range(n):
        if i == 0:
            sets.append(x.iloc[i:int(round(len(x)/n)),:])
        else:
            sets = sets
            sets.append(x.iloc[(i*int(round(len(x)/n))+1):(i+1)*int(round(len(x)/n)),:])
    return(sets)  

def CrossValidation(x,n): #
    I = pd.DataFrame(np.ones([len(x),1]),index= x.index,columns=['Intercept'])
    x = pd.concat([I,x],axis=1)
    x = shuffle(x)
    x = CV_split(x,n)
    correlations= []
    for i in range(len(x)):
        if i==0:
            test_data= x[i] #FIRST select data that WONT BE IN THE TRAINING SET, 
            not_testdata = x[:i]+x[i+1:]   # NEXT REMOVE THE TEST DATA AND KEEP EVERYTHING ELSE
            train_data = concat_train(not_testdata)
            X_s = np.array(test_data.iloc[:,0:len(test_data.columns)-1].values, dtype=[('O', np.float)]).astype(np.float)
            y_pred = np.dot(X_s,MLE(train_data)) # MlE gives Reg Coeff
            correlations.append(np.corrcoef(y_pred,test_data.iloc[:,len(test_data.columns)-1])[0][1])
        else:
            correlations= correlations
            test_data= x[i] #FIRST select data that WONT BE IN THE TRAINING SET, 
            not_testdata = x[:i]+x[i+1:]   # NEXT REMOVE THE TEST DATA AND KEEP EVERYTHING ELSE   
            train_data= concat_train(not_testdata)
            X_s = np.array(test_data.iloc[:,0:len(test_data.columns)-1].values, dtype=[('O', np.float)]).astype(np.float)
            y_pred = np.dot(X_s,MLE(train_data))
            correlations.append(np.corrcoef(y_pred,test_data.iloc[:,len(test_data.columns)-1])[0][1])
    return(np.mean(np.array(correlations)))  




    
    
               

         
      