import pandas as pd
import matplotlib.pyplot as plt


file_path = 'Ecommerce_DBS.csv'
df = pd.read_csv(file_path)

colums_deleted = ['Country', 'State', 'Latitude', 'Longituide']
df = df.drop(columns=colums_deleted)

df_Electronics = df[df['Product Category'] == 'Electronics']

total_eletronicos_vendidos = df_Electronics['Total Purchase Amount'].sum()

eletronicos_por_canal = df_Electronics.groupby('Source')['Total Purchase Amount'].sum()

eletronicos_por_canal = eletronicos_por_canal.sort_values(ascending=False)

print("Quantidade total de vendas de eletronicos por canal existente:")
print(eletronicos_por_canal)


plt.figure(figsize=(10, 6))
eletronicos_por_canal.plot(kind='bar', color='orange')
plt.title('Quantidade de eletronicos Vendidos por Canal')
plt.xlabel('Canal de Vendas')
plt.ylabel('Quantidade de eletronicos Vendidos')
plt.xticks(rotation=45)
plt.show()

