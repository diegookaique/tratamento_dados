# Tratar Outliers
# (Valores extremamente altos ou extremamente baixos)

import pandas as pd
from scipy import stats

pd.set_option('display.width', None)

df = pd.read_csv('clientes_limpeza.csv')

df_filtro_basico = df[df['idade'] > 100]

print('Filtro básico \n', df_filtro_basico[['nome', 'idade']])

# Identificar outliers com Z-score
z_scores = stats.zscore(df['idade'].dropna())
outliers_z = df[z_scores >= 3]
print("Outliers pelo Z-score:\n", outliers_z)

# Filtrar outliers com Z-score
df_zscore = df[(stats.zscore(df['idade'] < 3)]

# Identificar outliers com IQR
Q1 = df['idade'].quantile(0.25)
Q3 = df['idade'].quantile(0.75)
IQR = Q3 - Q1

limite_baixo = Q1 - 1.5 * IQR
limite_alto = Q3 + 1.5 * IQR
print("Limites IQR: ", limite_baixo, limite_alto)

outliers_iqr = df[(df['idade'] < limite_baixo) | (df['idade'] > limite_alto)]
print("Outliers pelo IQR:\n", outliers_iqr)

# Filtrar outliers com IQR
df_iqr = df[(df['idade] >= limite_baixo) & (df['idade'] <= limite_alto)]

limite_baixo = 0
limite_alto = 100

# Filtrar endereços inválidos
df['endereco'] = df['endereco'].apply(lambda x: 'Endereço I=inválido' df len(x.split('\n')) < 3 else x)
print ('Quantidade de  registros com endereço inválido:' , (df['endereco'] == 'Endereço inválido').sum())

print('Dados com Outliers tratados:\n', df)

# Salvar dataframe
df.to_csv('clientes_remove_outliers.csv', index=False)
