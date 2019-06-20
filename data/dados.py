#%%
import pandas as pd

#%%
url = 'https://raw.githubusercontent.com/fabiommendes/desenvolvimento-de-software/master/dados/pnad2012.csv'
df = pd.read_csv(url, index_col=0)
df.mean()

#%%
df

#%%
df_edu = df.groupby('education').mean()

#%%
df_edu[['income', 'income_work', 'income_rent', 'income_capital']].plot.line()

#%%
df_gen = df.groupby('gender').mean()

#%%
df_gen[['income', 'income_work', 'income_rent', 'income_capital']].plot.line()

#%%
df_race = df.groupby('gender').mean()

#%%
df_race[['income', 'income_work', 'income_rent', 'income_capital']].plot.line()

#%%
df_edu[['income', 'income_work', 'income_rent', 'income_capital']].max()

#%%
df_edu[['income', 'income_work', 'income_rent', 'income_capital']].min()

#%%
df_edu[['income', 'income_work', 'income_rent', 'income_capital']].mean()


#%%
df.groupby('gender').max()

#%%
df.groupby('gender').min()

#%%
df.groupby('gender').mean()

#%%
df.groupby('race').max()

#%%
df.groupby('race').min()

#%%
df.groupby('race').mean()

#%%
df.groupby('education').max()

#%%
df.groupby('education').min()

#%%
df.groupby('education').mean()


