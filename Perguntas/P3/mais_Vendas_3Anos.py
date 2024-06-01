import pandas as pd
import matplotlib.pyplot as plt

file_path = 'Ecommerce_DBS.csv'
df = pd.read_csv(file_path)

colums_deleted = ['Country', 'State', 'Latitude', 'Longituide']
df = df.drop(columns=colums_deleted)

df['Purchase Date'] = pd.to_datetime(df['Purchase Date'], format='%d/%m/%Y')

ultimo_ano = pd.Timestamp.now().year - 3
df_ultimos_3_anos = df[df['Purchase Date'].dt.year >= ultimo_ano]

vendas_por_produto = df_ultimos_3_anos.groupby('Product Category')['Total Purchase Amount'].sum()

produtos_mais_vendidos = vendas_por_produto.sort_values(ascending=False)

print("Produtos mais vendidos nos últimos 3 anos:")
print(produtos_mais_vendidos)

plt.figure(figsize=(10, 6))
plt.bar(produtos_mais_vendidos.index, produtos_mais_vendidos.values, color='skyblue')
plt.title('Produtos Mais Vendidos nos Últimos 3 Anos')
plt.xlabel('Produto')
plt.ylabel('Quantidade de Vendas')
plt.xticks(rotation=65)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

