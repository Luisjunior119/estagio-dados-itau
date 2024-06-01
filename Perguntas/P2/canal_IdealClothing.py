import pandas as pd
import matplotlib.pyplot as plt


file_path = 'Ecommerce_DBS.csv'
df = pd.read_csv(file_path)

colums_deleted = ['Country', 'State', 'Latitude', 'Longituide']
df = df.drop(columns=colums_deleted)

df_Clothing = df[df['Product Category'] == 'Clothing']

total_roupas_vendidas = df_Clothing['Total Purchase Amount'].sum()

roupas_por_canal = df_Clothing.groupby('Source')['Total Purchase Amount'].sum()

roupas_por_canal = roupas_por_canal.sort_values(ascending=False)

print("Quantidade total de vendas de roupas por canal existente:")
print(roupas_por_canal)


plt.figure(figsize=(10, 6))
roupas_por_canal.plot(kind='bar', color='orange')
plt.title('Quantidade de roupas vendidas por Canal')
plt.xlabel('Canal de Vendas')
plt.ylabel('Quantidade de roupas Vendidas')
plt.xticks(rotation=45)
plt.show()

