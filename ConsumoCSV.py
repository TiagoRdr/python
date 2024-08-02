import pandas as pd

df_vendas = pd.read_csv('csv_vendas.csv', sep=',')


def soma_venda(df):
    total_venda = df.groupby('Número da Venda')['Total de Venda'].sum()
    return total_venda











somado = soma_venda(df_vendas)

somado.to_csv('total_por_venda.csv', header=True, sep=';')
#print(df_vendas['Número da Venda'])
