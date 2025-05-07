import pandas as pd

df = pd.read_csv('C:/Users/kaiqu/OneDrive/Área de Trabalho/Ciência de Dados/clientes.csv')

pd.set_option('display.width', None)
print(df.head())

# Remover dados
df.drop('pais', axis=1, inplace=True)  # Coluna
df.drop(2, axis=0, inplace=True)  # Linha

# Normalizar campos de texto
df['nome'] = df['nome'].str.title() # Trata a primeira de letra de cada palavra para minuscula
df['endereco'] = df['endereco'].str.lower() # Todas as letras minusculas
df['estado'] = df['estado'].str.strip().str.upper() # Converte para maiuscula

# Converter tipos de dados
df['idade'] = df['idade'].astype(int)

# Tratar valores nulos (ausentes)
df_fillna = df_fillna(0)  # Substituir valores nulos por 0
df_dropna = df.dropna()  # Remover registros com valores nulos
df_dropna4 = df_dropna(thresh=4)  # Manter registro com no mínimo 4 valores não nulos
df = df.dropna(subset=['cpf'])  # Remover registro com CPF nulo

print('Valores nulos:\n', df.isnull().sum())
print('Quantidade de registros nulos com fillna:', df_fillna.isnull().sum().sum())
print('Quantidade de registros nulos com dropna:', df_dropna.isnull().sum().sum())
print('Quantidade de registros nulos com dropna4:', df_dropna4.isnull().sum().sum())
print('Quantidade de registro nulos com CPF:', df.isnull().sum().sum())

df.fillna({'estado': 'Desconhecido'}, inplace=True)
df['endereco'] = df['endereco'].fillna('Endereço não informado')
df['idade_corrigida'] = df['idade'].fillna(df['idade'].mean())
# Tratar formato de dados
df['data_corrigida'] = pd.to_datetime(df['data'], format='%d/%m/%y', errors='coerce')

# Tratar dados duplicados
print('Quantidade registros atual:', df.shape[0])
df.drop_duplicates()
df.drop_duplicates(subset='cpf', inplace=True)
print('Quantidade registros removendo as duplicadas:', len(df))

print('Dados limpos:\n', df)

# Salvar dataframe
df['data'] = df['data_corrigida']
df['idade'] = df['idade_corrigida']

df_salvar = df[['nome', 'cpf', 'idade', 'data', 'endereco', 'estado']]
df_salvar.to_csv('clientes_limpeza.csv', index=False)

print('Novo DataFrame: \n', pd.read_csv('clientes_limpeza.csv'))
