import pandas as pd


file_path = 'Ecommerce_DBS.csv'
df = pd.read_csv(file_path)

missing_values = df.isnull().sum()
print(missing_values)

colums_deleted = ['Country', 'State', 'Latitude', 'Longituide']
df = df.drop(columns=colums_deleted)

# Exibir as primeiras linhas do dataframe resultante
print("DataFrame após exclusão das colunas:")
print(df.head())

# Você pode continuar sua análise aqui
# Exemplo: Estatísticas descritivas
print("\nEstatísticas descritivas:")
print(df.describe())
