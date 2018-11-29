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
    for j in range(len(x)):  #Use this in the CrossValidation Function I am building
        if j==0:
            concat_set=[]                          
            concat_set.append(x[j])
        else:
            concat_set= concat_set
            concat_set.append(x[j])
            train_data=pd.concat(concat_set)
    return(train_data)
    
def MLE(df):
   x= df.iloc[:,0:len(df.columns)-1]    #Function that gives the MLE Regression Coefficents 
   y= df.iloc[:,len(df.columns)-1]
   theta = np.dot(np.dot(np.linalg.inv(np.dot(x.T,x)),x.T),y)
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
            y_pred = np.dot(test_data.iloc[:,0:len(test_data.columns)-1],MLE(train_data)) # MlE gives Reg Coeff
            correlations.append(np.corrcoef(y_pred,test_data.iloc[:,len(test_data.columns)-1])[0][1])
        else:
            correlations= correlations
            test_data= x[i] #FIRST select data that WONT BE IN THE TRAINING SET, 
            not_testdata = x[:i]+x[i+1:]   # NEXT REMOVE THE TEST DATA AND KEEP EVERYTHING ELSE   
            train_data= concat_train(not_testdata)  
            y_pred = np.dot(test_data.iloc[:,0:len(test_data.columns)-1],MLE(train_data))
            correlations.append(np.corrcoef(y_pred,test_data.iloc[:,len(test_data.columns)-1])[0][1])
    return(np.mean(np.array(correlations)))  

def MexHat(x):
    MexHat_Data = np.dot(x,m_hat.T)
    return(MexHat_Data)
plot_data_wavelet_AM={}
#####Amplitude Tuning Loop##########
sweep = list(np.linspace(-2,2,400)) #the first amino acid
for acid in count_df.index:
    CrossValidation_Scores= []
    for score in sweep:
        A = just_let.copy()
        ltw_sorted[acid]= score
        A.replace(ltw_sorted,inplace=True)
        colnames = ['cd11','cd12','cd13','cd2','ca2']
        MHat_Transformed= pd.DataFrame(MexHat(A), index=just_let.index, columns= colnames)
        MHat_Transformed['pMeas']= nine_pep['pMeas']
        CrossValidation_Scores.append(CrossValidation(MHat_Transformed,10))
        ltw_sorted[acid] = sweep[CrossValidation_Scores.index(max(CrossValidation_Scores))]
    
    
    plt.plot(sweep,CrossValidation_Scores)
    plt.title(str(acid))
    plt.show()    
    
    plot_data_wavelet_AM[acid]= pd.DataFrame([sweep,CrossValidation_Scores])
    

    
    
               

         
      