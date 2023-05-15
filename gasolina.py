# - imports;
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# - coleta de dados;
gasoline_df = pd.read_csv('gasolina.csv', sep=',')
# - grafico;
grafico = sns.lineplot(data=gasoline_df, x='dia', y='venda')
# - salvar o grafico;
plt.savefig('gasolina.png')
# mensagem de finalização
print('sucesso')