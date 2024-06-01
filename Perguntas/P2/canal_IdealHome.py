import pandas as pd
import matplotlib.pyplot as plt


file_path = 'Ecommerce_DBS.csv'
df = pd.read_csv(file_path)

colums_deleted = ['Country', 'State', 'Latitude', 'Longituide']
df = df.drop(columns=colums_deleted)

df_Home = df[df['Product Category'] == 'Home']

total_casas_vendidas = df_Home['Total Purchase Amount'].sum()

casas_por_canal = df_Home.groupby('Source')['Total Purchase Amount'].sum()

casas_por_canal = casas_por_canal.sort_values(ascending=False)

print("Quantidade total de vendas de casas por canal existente:")
print(casas_por_canal)


plt.figure(figsize=(10, 6))
casas_por_canal.plot(kind='bar', color='orange')
plt.title('Quantidade de casas Vendidos por Canal')
plt.xlabel('Canal de Vendas')
plt.ylabel('Quantidade de casas Vendidas')
plt.xticks(rotation=45)
plt.show()

