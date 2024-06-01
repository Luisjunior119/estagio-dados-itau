import pandas as pd
import matplotlib.pyplot as plt

file_path = 'Ecommerce_DBS.csv'
df = pd.read_csv(file_path)

colums_deleted = ['Country', 'State', 'Latitude', 'Longituide']
df = df.drop(columns=colums_deleted)

df['Purchase Date'] = pd.to_datetime(df['Purchase Date'], dayfirst=True)

total_vendas_por_categoria = df.groupby('Product Category')['Total Purchase Amount'].sum()

total_vendas_ordenadas = total_vendas_por_categoria.sort_values()

print("Quantidade total de vendas por categoria de produto:")
print(total_vendas_ordenadas)

categoria_menos_vendida = total_vendas_ordenadas.idxmin()
menor_venda = total_vendas_ordenadas.min()
print(f"A categoria de produto mais vendida é '{categoria_menos_vendida}' com um total de vendas de {menor_venda:.2f}")


plt.figure(figsize=(10, 6))
plt.bar(total_vendas_ordenadas.index, total_vendas_ordenadas.values, color='skyblue')
plt.title('Quantidade Total de Vendas por Categoria de Produto')
plt.xlabel('Categoria de Produto')
plt.ylabel('Quantidade Total de Vendas')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
