import pandas as pd
import matplotlib.pyplot as plt


file_path = 'Ecommerce_DBS.csv'
df = pd.read_csv(file_path)

colums_deleted = ['Country', 'State', 'Latitude', 'Longituide']
df = df.drop(columns=colums_deleted)

df_books = df[df['Product Category'] == 'Books']

total_books_vendidos = df_books['Total Purchase Amount'].sum()

livros_por_canal = df_books.groupby('Source')['Total Purchase Amount'].sum()

livros_por_canal = livros_por_canal.sort_values(ascending=False)

print("Quantidade total de vendas por dos livros por canal existente:")
print(livros_por_canal)

plt.figure(figsize=(10, 6))
livros_por_canal.plot(kind='bar', color='orange')
plt.title('Quantidade de Livros Vendidos por Canal')
plt.xlabel('Canal de Vendas')
plt.ylabel('Quantidade de Livros Vendidos')
plt.xticks(rotation=45)
plt.show()

