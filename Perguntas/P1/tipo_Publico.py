import pandas as pd
import matplotlib.pyplot as plt


file_path = 'Ecommerce_DBS.csv'
df = pd.read_csv(file_path)

colums_deleted = ['Country', 'State', 'Latitude', 'Longituide']
df = df.drop(columns=colums_deleted)


print("Estatísticas Descritivas para Idade:")
print("\nContagem de Gênero:")
print(df['Gender'].value_counts())
plt.figure(figsize=(12, 6))


media_idade_mulheres = df[df['Gender'] == 'Female']['Customer Age '].mean()
media_idade_homens = df[df['Gender'] == 'Male']['Customer Age '].mean()

print("Média de Idade de Todas as Mulheres:", media_idade_mulheres)
print("Média de Idade de Todos os Homens:", media_idade_homens)

quantidade_genero = df['Gender'].value_counts()
quantidade_mulheres = quantidade_genero['Female']
quantidade_homens = quantidade_genero['Male']

plt.figure(figsize=(8, 6))
plt.bar(['Mulheres', 'Homens'], [quantidade_mulheres, quantidade_homens], color=['pink', 'blue'])
plt.title('Distribuição da Quantidade de Homens e Mulheres no Ecommerce')
plt.xlabel('Gênero')
plt.ylabel('Quantidade')
plt.show()

plt.figure(figsize=(8, 6))
plt.bar(['Mulheres', 'Homens'], [media_idade_mulheres, media_idade_homens], color=['pink', 'blue'])
plt.title('Média de Idade de Homens e Mulheres no Ecommerce')
plt.xlabel('Gênero')
plt.ylabel('Média de Idade')
plt.show()