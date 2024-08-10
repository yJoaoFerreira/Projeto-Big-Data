import pandas as pd
import re

def regex(preco):
    if pd.isna(preco):
        return ""
    preco_str = str(preco)
    preco_sem_rs = re.sub(r'R\$', '', preco_str).strip()
    preco_alterado = re.sub(r',', '.', preco_sem_rs)
    return preco_alterado

Dados = pd.read_excel('/content/Dados Não Sensíveis (1).xlsx')

Coluna = Dados['Preco']

Dados2 = []

for valor in Coluna:
    Dados2.append(regex(valor))

Dados['Preco_Tratado'] = Dados2

Dados3 = Dados

Dados3 = Dados3.fillna(0)



Dados4 = Dados3.query('Bairro != 0').query('DataDeEntrega != 0').query('FormaDePagamento != 0').drop(columns=['NomeCompleto','Telefone','LocalizacaoFixa','Rua','Complemento','Numero','CEP'])
Dados4
Dados4.to_excel('/content/Dados Tratados (3).xlsx')
