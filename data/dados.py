import pandas as pd
url = 'https://raw.githubusercontent.com/guilhermemoraisr/red-hot-chili-webbers/master/data/pnad2012.csv'
dados = pd.read_csv(url, index_col=0, sep=',')

dados = dados.dropna(axis=0, subset=['income'])
dados = dados.sort_values('income')

# Agrupando por raça
brancos = dados[(dados.race == 16) | (dados.race == 1)]
negros = dados[(dados.race == 2) | (dados.race == 4) | (dados.race == 8)]

# Agrupando por gênero
homem = dados[(dados.gender == 1)]
mulher = dados[(dados.gender == 2)]

# Agrupando por educação
sem_estudo = dados[(dados.education == 0) | (dados.education == 1)]
fund_incompleto = dados[(dados.education == 2) | (dados.education == 3)]
fund_completo = dados[(dados.education == 4) | (dados.education == 5)]
med_incompleto = dados[(dados.education == 6) | (dados.education == 7)]
med_completo = dados[(dados.education == 8) | (dados.education == 9) | (dados.education == 10)]
sup_incompleto = dados[(dados.education == 11) | (dados.education == 12) | (dados.education == 13) | (dados.education == 14)]
sup_completo = dados[(dados.education == 15)]

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


def MediaFinal(salario, raca, sexo, estado, edu):

    if sexo == 1 and raca == 1:
        privsexoraca=100
    if sexo == 2 and raca == 1:
        privsexoraca = 75
    if sexo == 1 and raca == 2:
        privsexoraca=50
    if sexo ==2 and raca == 2:
        privsexoraca=25
    
    if edu == 1:
        privedu = 0
    if edu == 2:
        privedu = 12.5
    if edu == 3:
        privedu = 25
    if edu == 4:
        privedu = 37.5
    if edu == 5:
        privedu = 50
    if edu == 6:
        privedu = 75
    if edu == 7:
        privedu = 100
    
    # Porcentagem de privilégio em relação à renda média de cada unidade da federação. 
    if estado == 7 or estado == 25:
        privestado = 100
    #<!--Distrito Federal e São Paulo-->
    elif estado == 19 or estado == 24 or estado == 16 or estado == 21:
        privestado = 80
    #<!--Rio de Janeiro, Paraná, Santa Catarina e Rio Grande do Sul-->
    elif estado == 11 or estado == 12 or estado == 9 or estado == 13 or estado == 8:
        privestado = 60
    #<!--Mato Grosso, Mato Grosso do Sul, Goiás, Minas Gerais e Espírito Santo-->
    elif estado == 23 or estado == 17:
        privestado = 40
    #<!--Roraima e Pernambuco-->
    elif estado == 1 or estado == 4 or estado == 22 or estado == 14 or estado == 3 or estado == 27 or estado == 18 or estado == 20 or estado == 2 or estado == 15 or estado == 26 or estado == 5 or estado == 6:
        privestado = 20
    #<!--Acre, Amazonas, Rondônia, Pará, Amapá, Tocantins, Ceará, Rio Grande do Norte, Alagoas, Paraíba, Sergipe e Bahia-->
    elif estado == 10:
        privestado = 0
    #<!--Maranhão-->

    #Cálculo do privilégio baseado na posição do PNAD
    
    dfna = dados.dropna(axis=0, subset=['income'])
    df = dfna.sort_values('income')

    lista = list(df.income)

    l = []
    for i in lista:
        if i not in l:
            l.append(i)

    for i,r in enumerate(l):
        if r>salario:
            break
    
    porc = ((i+1)/len(l))*100

    privrenda = round(porc,1)

    privfinal = ((3*privrenda)+privestado+privedu+privsexoraca)/6.0

    return (privfinal)


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
dados3.income.min()

#%%
negros.income.max()

#%%
"""