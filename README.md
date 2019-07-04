# Projeto final de Desenvolvimento de Software - Universidade de Brasília

## Membros:

- Ian Fillipe Pontes Ferreira - 18/0102087
- Guilherme de Morais Richter - 18/0101617
- Ítalo Vinícius Pereira Guimarães - 18/0102656
- Lucas Rodrigues Fonseca - 18/0114077
- Eric Chagas de Oliveira - 18/0119508

# Qual o seu privilégio?

## Algumas informações:
- Criamos um site em Flask, que tem como foco a classificação do indivíduo na sociedade, classificações as quais depende de alguns fatores como a renda, gênero, sexo, estado, tamanho da família, etc.
- Para calcular a porcentagem de privilégio do usuário, utilizamos principalmente o dataframe do PNAD 2012 e outras informações externas, como classificação das classes sociais no Brasil, ranking das melhores regiões e definimos uma visão social pessimista porém muito realista em nosso meio, que seria a classificação do gênero e do sexo agrupados.
- Este site é um apêndice ao jogo desenvolvido pelos outros grupos do projeto final, com o objetivo de expor as dificuldades e privilégios da realidade social brasileira.
Este trabalho foi orientado pelo docente Prof. Fábio Macêdo Mendes: https://github.com/fabiommendes/desenvolvimento-de-software/blob/master/trabalhos/web_qual_seu_privilegio.md

## Método para cálculo do privilégio
### Analisamos a raça e o gênero em 4 diferentes níveis de porcentagem

- Mulher negra = 0%
- Homem negro = 33%
- Mulher branca = 66%
- Homem branco = 100%

### Analisamos a educação em 7 diferentes níveis de porcentagem

- Sem estudo = 0%
- Ensino fundamental incompleto = 16%
- Ensino fundamental completo = 33%
- Ensino médio incompleto = 50%
- Ensino médio completo = 66%
- Ensino superior incompleto = 83%
- Ensino superior completo = 100%

### Analisamos a região em 5 diferentes níveis de porcentagem
- Nordeste = 0%
- Norte = 25%
- Sul = 50%
- Centro-oeste = 75%
- Sudeste = 100%

### Analisamos a renda a partir do dataframe do PNAD 2012
- Calculamos a diferença salarial entre o mais rico e mais pobre e aplicamos a proporção à porcentagem do salário informado, também com base na pirâmide de renda de fonte Datafolha/nov.2013.

# Como rodar o site em sua máquina ?

Você deve ter o Python 3+* e o pipenv** instalado para rodar o site.

1º - Baixe ou clone o repositório

2º - Vá até o caminho do repositório, no caso, pelo terminal, o meu está localizado no Desktop

<a href="https://imgur.com/9caDnK6"><img src="https://i.imgur.com/9caDnK6.png" title="source: imgur.com" /></a>

3º - Digite 'pipenv shell', este comando criará um ambiente ativo, por padrão o ambiente é nomeado com o nome da pasta onde o mesmo foi criado, no nosso caso o ambiente virtual se chama: red-hot-chili-webbers

<a href="https://imgur.com/t8791qW"><img src="https://i.imgur.com/t8791qW.png" title="source: imgur.com" /></a>

4º - Digite 'pipenv install -r ./requirements.txt', este comando vai instalar todas as bibliotecas necessárias

<a href="https://imgur.com/r281BlS"><img src="https://i.imgur.com/r281BlS.png" title="source: imgur.com" /></a>

5º - Digite 'flask run', isso vai criar um servidor local para o site

<a href="https://imgur.com/EOMF1Ux"><img src="https://i.imgur.com/EOMF1Ux.png" title="source: imgur.com" /></a>

6º - Entre no link que apareceu, este é o endereço do site.

Para sair do flask no terminal digite 'Ctrl+c'

Para desativar o ambiente virtual digite 'deactivate' 

*(Se utiliza o Windows, adicione o Python na PATH)
**(utilizamos um ambiente virtual para que não instale nada que o usuário não goste em sua máquina)


### Favor Ian apagar depois

import pandas as pd
url = 'https://raw.githubusercontent.com/guilhermemoraisr/red-hot-chili-webbers/master/data/pnad2012.csv'
dados = pd.read_csv(url, index_col=0, sep=',')
df = pd.read_csv(url)

dados2 = dados.fillna(dados.mean())

dados3 = dados2.copy()

df = df.dropna(axis=0, subset=['income'])
df = df.sort_values('income')

dados3[['income', 'income_work', 'income_rent', 'income_capital']] = dados2[['income', 'income_work', 'income_rent', 'income_capital']]

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

    # Cálculo do privilégio em relação à renda do indivíduo

    rendamax = df.income.max()
    rendamin = df.income.min()

    if salario > rendamax:
        salario = rendamax
    if salario < rendamin:
        salario = rendamin

    for i, r in enumerate(df.income):
        if r>salario:
            break
    privrenda = ((i+1)/len(df.income))*100

    privfinal = ((3*privrenda)+privestado+privedu+privsexoraca)/6 

    return (privfinal.round(1))


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

