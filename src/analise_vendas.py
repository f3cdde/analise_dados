import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o conjunto de dados
df = pd.read_csv('/app/data/vendas.csv')

# Exibir as primeiras linhas do DataFrame
print(df.head())

# Converter a coluna 'Data' para o tipo datetime
df['Data'] = pd.to_datetime(df['Data'])

# Agrupar os dados por mês e somar as vendas
df['Mês'] = df['Data'].dt.to_period('M')
vendas_mensais = df.groupby('Mês')['Vendas'].sum()

# Plotar as vendas mensais
plt.figure(figsize=(10, 6))
sns.barplot(x=vendas_mensais.index.astype(str), y=vendas_mensais.values, palette='viridis')
plt.title('Vendas Mensais')
plt.xlabel('Mês')
plt.ylabel('Total de Vendas')
plt.xticks(rotation=45)
plt.tight_layout()

# Salvar o gráfico como uma imagem
plt.savefig('/app/data/vendas_mensais.png')
print("Gráfico salvo como 'vendas_mensais.png'")
