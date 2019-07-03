import pandas as pd
url = 'https://raw.githubusercontent.com/fabiommendes/desenvolvimento-de-software/master/dados/pnad2012.csv'
dados = pd.read_csv(url, index_col=0, sep=',')

dados2 = dados.fillna(0)

dados3 = dados2.copy()

dados3[['income', 'income_work', 'income_rent', 'income_capital']] = dados2[['income', 'income_work', 'income_rent', 'income_capital']].multiply(1.4907)

# Agrupando por raça
brancos = dados3[(dados3.race == 16) | (dados3.race == 1)]
negros = dados3[(dados3.race == 2) | (dados3.race == 4) | (dados3.race == 8)]

# Agrupando por gênero
homem = dados3[(dados3.gender == 1)]
mulher = dados3[(dados3.gender == 2)]

# Agrupando por educação
sem_estudo = dados3[(dados3.education == 0) | (dados3.education == 1)]
fund_incompleto = dados3[(dados3.education == 2) | (dados3.education == 3)]
fund_completo = dados3[(dados3.education == 4) | (dados3.education == 5)]
med_incompleto = dados3[(dados3.education == 6) | (dados3.education == 7)]
med_completo = dados3[(dados3.education == 8) | (dados3.education == 9) | (dados3.education == 10)]
sup_incompleto = dados3[(dados3.education == 11) | (dados3.education == 12) | (dados3.education == 13) | (dados3.education == 14)]
sup_completo = dados3[(dados3.education == 15)]

def Escolaridade(edu):
    if edu == 1:
        return ((100 - ((100 * sem_estudo.income.mean()) / sup_completo.income.mean())).round(1))
    elif edu == 2:
        return ((100 - ((100 * fund_incompleto.income.mean()) / sup_completo.income.mean())).round(1))
    elif edu == 3:
        return (((100 - ((100 * fund_completo.income.mean()) / sup_completo.income.mean())).round(1)))
    elif edu == 4:
        return ((100 - ((100 * med_incompleto.income.mean()) / sup_completo.income.mean())).round(1))
    elif edu == 5:
        return ((100 - ((100 * med_completo.income.mean()) / sup_completo.income.mean())).round(1))
    elif edu == 6:
        return ((100 - ((100 * sup_incompleto.income.mean()) / sup_completo.income.mean())).round(1))
    elif edu == 7:        
        return ((((100 - ((100 * sem_estudo.income.mean()) / sup_completo.income.mean())) + (100 - ((100 * fund_incompleto.income.mean()) / sup_completo.income.mean())) + (100 - ((100 * fund_completo.income.mean()) / sup_completo.income.mean())) + (100 - ((100 * med_incompleto.income.mean()) / sup_completo.income.mean())) + (100 - ((100 * med_completo.income.mean()) / sup_completo.income.mean())) + (100 - ((100 * sup_incompleto.income.mean()) / sup_completo.income.mean()))) / 6).round(1))

def Genero():
    return ((100 - ((100 * mulher.income.mean()) / homem.income.mean())).round(1))

def Etnia():
    return ((100 - ((100 * negros.income.mean()) / brancos.income.mean())).round(1))


"""
#%%
import pandas as pd
#%%
url = 'https://raw.githubusercontent.com/fabiommendes/desenvolvimento-de-software/master/dados/pnad2012.csv'
dados = pd.read_csv(url, index_col=0, sep=',')
#%%
dados2 = dados.fillna(0)
#%%
dados3 = dados2.copy()
#%%
dados3[['income', 'income_work', 'income_rent', 'income_capital']] = dados2[['income', 'income_work', 'income_rent', 'income_capital']].multiply(1.4907)
#%%
brancos = dados3[(dados3.race == 16) | (dados3.race == 1)]
negros = dados3[(dados3.race == 2) | (dados3.race == 4) | (dados3.race == 8)]

#%%
sem_estudo = dados3[(dados3.education == 0) | (dados3.education == 1)]
fund_incompleto = dados3[(dados3.education == 2) | (dados3.education == 3)]
fund_completo = dados3[(dados3.education == 4) | (dados3.education == 5)]
med_incompleto = dados3[(dados3.education == 6) | (dados3.education == 7)]
med_completo = dados3[(dados3.education == 8) | (dados3.education == 9) | (dados3.education == 10)]
sup_incompleto = dados3[(dados3.education == 11) | (dados3.education == 12) | (dados3.education == 13) | (dados3.education == 14)]
sup_completo = dados3[(dados3.education == 15)]

#%%
(brancos.income.sum()) / (brancos.weight.sum())

#%%
dados3.groupby(['gender', 'education', 'race']).max()

#%% 
dados3.groupby(['gender', 'education', 'race']).min()

#%% 
dados3.groupby(['gender', 'education', 'race']).describe()

#%%  
perc =[.01 , .10, .20, .30, .40, .50, .60, .70, .80, .90] 

include =['object', 'float', 'int'] 
#%%

desc = dados3.describe(percentiles = perc, include = include) 

#%%
desc

#%%
descri = dados3["income_capital"].describe(percentiles = perc, include = include)

#%%
descri

#%%
((670.815000*brancos.income.sum()) / brancos.weight.sum()) / 50

#%%
dados3[['race', 'gender', 'income', 'weight']].describe(percentiles = perc, include = include)


#%%
((5241/2 * brancos.weight.mean())/ brancos.income.mean()) / 90

#%%
dados3[['education', 'income']].groupby('education').mean()

#%%
100 - ((100 * sem_estudo.income.mean()) / sup_completo.income.mean())
#%%
100 - ((100 * fund_incompleto.income.mean()) / sup_completo.income.mean())
#%%
100 - ((100 * fund_completo.income.mean()) / sup_completo.income.mean())
#%%
100 - ((100 * med_incompleto.income.mean()) / sup_completo.income.mean())
#%%
100 - ((100 * med_completo.income.mean()) / sup_completo.income.mean())
#%%
100 - ((100 * sup_incompleto.income.mean()) / sup_completo.income.mean())

#%%
brancos.income.mean()

#%%
negros.income.mean()

#%%
100 - ((100 * (sup_incompleto.income.mean() + med_completo.income.mean() + med_incompleto.income.mean() + fund_completo.income.mean() + fund_incompleto.income.mean() + sem_estudo.income.mean())) / sup_completo.income.mean())

#%%
homem = dados3[(dados3.race == 1)]
mulher = dados3[(dados3.race == 2)]

#%%
homem.income.mean()

#%%
mulher.income.mean()

#%%
100 - ((100 * mulher.income.mean()) / homem.income.mean())

#%%
brancos.income.mean()

#%%
negros.income.mean()

#%%
100 - ((100 * negros.income.mean()) / brancos.income.mean())

#%%
((100 - ((100 * sem_estudo.income.mean()) / sup_completo.income.mean())) + (100 - ((100 * fund_incompleto.income.mean()) / sup_completo.income.mean())) + (100 - ((100 * fund_completo.income.mean()) / sup_completo.income.mean())) + (100 - ((100 * med_incompleto.income.mean()) / sup_completo.income.mean())) + (100 - ((100 * med_completo.income.mean()) / sup_completo.income.mean())) + (100 - ((100 * sup_incompleto.income.mean()) / sup_completo.income.mean()))) / 6

#%%
"""