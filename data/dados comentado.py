import pandas as pd


url = 'https://raw.githubusercontent.com/fabiommendes/desenvolvimento-de-software/master/dados/pnad2012.csv'
df = pd.read_csv(url, index_col=0, sep=',')
df.mean()


df


df_edu = df.groupby('education').mean()

#PLOT 1 RENDA POR EDUCAÇÃO
#df_edu[['income', 'income_work', 'income_rent', 'income_capital']].plot.line()

#MÉDIA DE CADA VARIÁVEL SEPARADO POR GÊNERO
df_gen = df.groupby('gender').mean()

#PLOT 2 RENDA POR GÊNERO
#df_gen[['income', 'income_work', 'income_rent', 'income_capital']].plot.line()

#MÉDIA DE CADA VARIÁVEL SEPARADO POR RAÇA
df_race = df.groupby('race').mean()

#PLOT 3 RENDA POR RAÇA
#df_race[['income', 'income_work', 'income_rent', 'income_capital']].plot.line()

#MÁX DENTRE AS RENDAS
df_edu[['income', 'income_work', 'income_rent', 'income_capital']].max()

#MIN DENTRE AS RENDAS
df_edu[['income', 'income_work', 'income_rent', 'income_capital']].min()

#MÉDIAS DAS RENDAS
df_edu[['income', 'income_work', 'income_rent', 'income_capital']].mean()

#DATAFRAME COM OS VALORES MÁXIMOS DE RENDA SEPARADOS POR GÊNERO, RAÇA E EDUCAÇÃO
df.groupby(['gender', 'race']).max()

#DATAFRAME COM OS VALORES MÍNIMOS DE RENDA SEPARADOS POR GÊNERO, RAÇA E EDUCAÇÃO
df.groupby(['gender', 'race']).min()

#DATAFRAME COM OS VALORES MÉDIOS DE RENDA SEPARADOS POR GÊNERO, RAÇA E EDUCAÇÃO
df.groupby(['gender', 'race']).mean()

#DATAFRAME COM OS VALORES MÁXIMOS DE RENDA SEPARADOS POR GÊNERO E EDUCAÇÃO
df.groupby(['gender', 'education']).max()