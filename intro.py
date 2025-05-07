import pandas as pd

df = pd.read_csv('C:/Users/kaiqu/OneDrive/Área de Trabalho\Ciência de Dados/clientes.csv')

# Verificar os primeiros registros
print(df.head().to_string())

print(df.tail().to_string())

# Verificar quantidade de linhas e colunas
print('Quantidade: ', df.shape)

# Verificar tipos de dados
print('Tipagem:\n', df.dtypes)

# Checar valores nulos
print('Valores nulos:\n', df.isnull().sum())
