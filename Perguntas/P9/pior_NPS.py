import pandas as pd
import matplotlib.pyplot as plt

file_path = 'Ecommerce_DBS.csv'
df = pd.read_csv(file_path)

colums_deleted = ['Country', 'State', 'Latitude', 'Longituide']
df = df.drop(columns=colums_deleted)

media_nps_por_categoria = df.groupby('Product Category')['NPS'].mean()

media_nps_ordenada = media_nps_por_categoria.sort_values()

print("Média de NPS por categoria de produto (do pior para o melhor):")
print(media_nps_ordenada)

plt.figure(figsize=(10, 6))
plt.bar(media_nps_ordenada.index, media_nps_ordenada.values, color='orange')
plt.title('Média de NPS por Categoria de Produto (do pior para o melhor)')
plt.xlabel('Categoria de Produto')
plt.ylabel('Média de NPS')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()