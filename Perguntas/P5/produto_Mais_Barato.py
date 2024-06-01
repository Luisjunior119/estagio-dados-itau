import pandas as pd
import matplotlib.pyplot as plt

# Ler o arquivo CSV
file_path = 'Ecommerce_DBS.csv'
df = pd.read_csv(file_path)

colums_deleted = ['Country', 'State', 'Latitude', 'Longituide']
df = df.drop(columns=colums_deleted)

precos_minimos = df.groupby('Product Category')['Product Price'].min()

produto_mais_barato = precos_minimos.idxmin()
preco_mais_barato = precos_minimos.min()

print("Preços mais baixos de cada categoria:")
print(precos_minimos)

print(f"O produto mais barato é da categoria '{produto_mais_barato}' com o preço de {preco_mais_barato:.2f}")

plt.figure(figsize=(10, 6))
plt.bar(precos_minimos.index, precos_minimos.values, color='skyblue')
plt.title('Menor Preço de Cada Categoria de Produto')
plt.xlabel('Categoria de Produto')
plt.ylabel('Menor Preço')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()


