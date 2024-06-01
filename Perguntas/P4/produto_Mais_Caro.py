import pandas as pd
import matplotlib.pyplot as plt

file_path = 'Ecommerce_DBS.csv'
df = pd.read_csv(file_path)

colums_deleted = ['Country', 'State', 'Latitude', 'Longituide']
df = df.drop(columns=colums_deleted)

precos_maximos = df.groupby('Product Category')['Product Price'].max()

produto_mais_caro = precos_maximos.idxmax()
preco_mais_caro = precos_maximos.max()

print("Preços mais altos de cada categoria:")
print(precos_maximos)

print(f"O produto mais caro é da categoria '{produto_mais_caro}' com o preço de {preco_mais_caro:.2f}")

plt.figure(figsize=(10, 6))
plt.bar(precos_maximos.index, precos_maximos.values, color='skyblue')
plt.title('Maior Preço de Cada Categoria de Produto')
plt.xlabel('Categoria de Produto')
plt.ylabel('Maior Preço')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

