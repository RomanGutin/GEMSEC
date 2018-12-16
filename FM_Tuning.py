# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 13:56:44 2018

@author: RomanGutin
"""
import pandas as pd
import numpy as np
#Frequency Tuning Loop
amino_letter = ['A','R','D','N','C','E','Q','G','H','I','L','K','M','F','P','S','T','W','Y','V']
length_scores =[4,8,6,6,5,7,7,4,7,5,6,8,7,8,5,5,5,9,8,5] 
FM_df = pd.DataFrame(0, index= just_let.index, columns= range(0,81))
FM_score_dict = dict(zip(amino_letter,length_scores))

#splitting amino letter into new independent variables based on its length score#
fm_letter_dict ={}
for letter in amino_letter:
    new_vars =[]
    for i in range(FM_score_dict[letter]):
        new_vars.append(letter+str(i+1))
    fm_letter_dict[letter]=new_vars
        
#generate new FM_tuned dataframe        
for seq in FM_df.index:
    letter_list= list(seq) 
    for letter in letter_list: 
        for var in fm_letter_dict[letter]:
            row= FM_df.loc[seq,:]
            spot= row[row==0].index[0]
            FM_df.loc[seq,spot]= var


FM_df= pd.read_csv('Frequency Tuned Dataset') #data after frequency tuning wit
FM_df.set_index('sequence', inplace= True)
FM_df_arr = np.array(FM_df.values, dtype=[('O', np.float)]).astype(np.float)


  #New letter to weight holding the new FM tuned variables
ltw_fm_MLE={}
for amino in amino_letter:
    for var in fm_letter_dict[amino]:
        ltw_fm_MLE[var]= ltw_AM_n[amino]
     

ltw_fm_MLE = np.load('ltw_fm_MLE.npy').item() 

    