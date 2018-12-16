# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 21:53:00 2018

@author: RomanGutin
"""
import numpy as np
import pandas as pd
plot_data={}
#####AM_Tuning With Wavelet
def AM_W(x,first,last,steps):
    sweep = list(np.linspace(first,last,(last-first)/steps)) #the first amino acid
    for acid in count_df.index:
        CrossValidation_Scores= []
        for score in sweep:
            A = x.copy()
            ltw_AM[acid]= score
            A.replace(ltw_AM,inplace=True)
            MHat_Transformed= pd.DataFrame(W(A), index=just_let.index)
            MHat_Transformed['pMeas']= nine_pep['pMeas']
            MHat_Transformed['pMeas']= nine_pep['pMeas']
            CrossValidation_Scores.append(CrossValidation(A,10))
            ltw_AM[acid] = sweep[CrossValidation_Scores.index(max(CrossValidation_Scores))]
    
    
    plt.plot(sweep,CrossValidation_Scores)
    plt.title(str(acid))
    plt.show()    
    
    plot_data[acid]= pd.DataFrame([sweep,CrossValidation_Scores])
#AM Tuned Scores Pre FM#    
ltw_AM_w = np.load('AM Scores of Wavelet Transformed Pre FM.npy').item()
ltw_AM_n = np.load('AM Scores Not Wavelet Transformed.npy').item()


####AM Not Wavelet Transformed
def AM(Dataframe,dict_scores,first,last,steps):
    sweep = list(np.linspace(first,last,(last-first)/steps)) #the first amino acid
    for var in dict_scores.keys():
        print('Variable: '+ var)
        CrossValidation_Scores= []
        for score in sweep:
            A = Dataframe.copy()
            dict_scores[var]= score
            A.replace(dict_scores,inplace=True)
            A['pMeas']= nine_pep['pMeas']
            CrossValidation_Scores.append(CrossValidation(A,10))
            print(str(score) + '  ' + 'CrossValidation: ' + str(CrossValidation_Scores[-1]))
        dict_scores[var] = sweep[CrossValidation_Scores.index(max(CrossValidation_Scores))]
        
        
        plt.plot(sweep,CrossValidation_Scores)
        plt.title(str(var))
        plt.show()    
        
        plot_data[var]= pd.DataFrame([sweep,CrossValidation_Scores])