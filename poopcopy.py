import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import sklearn as sk
# og is the orignal data#
og = pd.read_csv('bdata.20130222.mhci.txt', delimiter='\t')
# I only care about the sequences from humans#
human = og[og['species'] == 'human']
human['meas'].apply(math.log10) 
human['meas']= human['meas']*-1
human.rename(columns={'meas' :'pMeas'}, inplace=True)
j = []
for seq in human['sequence']:
    j.append(list(seq))
j= pd.DataFrame(j, index= human.index)
human = pd.concat([human,j],axis=1)
amino_letter = ['A','R','D','N','C','E','Q','G','H','I','L','K','M','F','P','S','T','W','Y','V']
mol_weights =  [71.09,156.19,115.09,114.11,103.15,129.12,128.14,57.05,137.14,113.16,113.16,128.17,131.19,147.18,97.12,87.08,101.11,186.12,163.18,99.14]
def min_max(x,x_min,x_max):
    z = (2)*(x-x_min)/(x_max-x_min)-1
    return(z)
sc_weights = []
for i in mol_weights:
    sc_weights.append(min_max(i,np.min(mol_weights),np.max(mol_weights)))
ltw = dict(zip(amino_letter,sc_weights))
ltw_sorted = dict(sorted(ltw.items(), key=lambda kv: kv[1]))
list_length_allele = [] # list[peptidelength][allele I care about] = dataframe holding all data for a specific length and specific 
                            #allele.
dict_pep_length = {k:v for k,v in human.groupby('peptide_length')} #dictionary sectioning humans into df for each peptide length
for i in range(len(human['peptide_length'].unique())):
    list_length_allele.append({allele:val  for allele,val in dict_pep_length[human['peptide_length'].unique()[i]].groupby('mhc')})
nine_pep = list_length_allele[1][human['mhc'].unique()[1]]
#For loop converting every letter to its min-max value
for i in range(nine_pep.shape[0]):
    for j in range(9):
        nine_pep.iloc[i,j+6]=ltw_sorted[nine_pep.iloc[i,j+6]]
nine_pep.to_csv('Length 9 Peptide Sequences Min-Max Scored by Mol Weight', sep=',')        
just_seq = pd.read_csv('just_sequence.csv')
#Building custom mexican hat wavelet#
r1= [-1/6,2/6,-1/6,0,0,0,0,0,0]
r2=[0,0,0,-1/6,2/6,-1/6,0,0,0]
r3= [0,0,0,0,0,0,-1/6,2/6,-1/6]
r4 = [-1/math.sqrt(18),-1/math.sqrt(18),1/math.sqrt(18),2/math.sqrt(18),2/math.sqrt(18),2/math.sqrt(18),-1/math.sqrt(18),-1/math.sqrt(18),-1/math.sqrt(18)]
r5= [1/math.sqrt(18),1/math.sqrt(18),1/math.sqrt(18),2/math.sqrt(18),2/math.sqrt(18),2/math.sqrt(18),1/math.sqrt(18),1/math.sqrt(18),1/math.sqrt(18)]
m_hat= pd.DataFrame([r1,r2,r3,r4,r5])
just_seq.set_index('sequence',inplace=True)
W_seq= []
for i in range(len(just_seq.index)):
    W_seq.append(np.dot(m_hat.values,just_seq.iloc[i,0:9].values))
colnames = ['cd11','cd12','cd13','cd2','ca2']
W_seq =pd.DataFrame(W_seq, index=just_seq.index, columns = colnames)
nine_pep.set_index('sequence',inplace=True)
W_seq['pMeas']=nine_pep['pMeas']
#Split data into random sets
select_random = random.sample(range(9051),9051)
n1=[]
n2=[]
n3=[]
n4=[]
n5=[]
W_ran = shuffle(W_seq)