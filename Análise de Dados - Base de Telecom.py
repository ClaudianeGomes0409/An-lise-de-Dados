#!/usr/bin/env python
# coding: utf-8

# # Análise de Dados com Python
# 
# ### Desafio:
# 
# Você trabalha em uma empresa de telecom e tem clientes de vários serviços diferentes, entre os principais: internet e telefone.
# 
# O problema é que, analisando o histórico dos clientes dos últimos anos, você percebeu que a empresa está com Churn de mais de 26% dos clientes.
# 
# Isso representa uma perda de milhões para a empresa.
# 
# O que a empresa precisa fazer para resolver isso?
# 
# Base de Dados: https://drive.google.com/drive/folders/1T7D0BlWkNuy_MDpUHuBG44kT80EmRYIs?usp=sharing <br>
# Link Original do Kaggle: https://www.kaggle.com/radmirzosimov/telecom-users-dataset

# In[10]:


# Passo 1: Importar a base de dados para o Python
import pandas as pd

tabela = pd.read_csv("telecom_users.csv")
display(tabela)


# In[11]:


# Passo 2: Visualizar a base de dados
# Entender quais informações estão disponiveis
# Descobrir os erros/problemas da base de dados
tabela = tabela.drop("Unnamed: 0", axis=1)  # 0 significa linha e 1 significa coluna, axis=eixo
display(tabela)


# In[16]:


# Passo 3: Tratamento das bases de dados
# Valores que são do tipo número mais o python entende como texto
print(tabela.info())  # comando para saber as informações da tabela
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce") # para transformar valor texto para número.

# Valores vazios
# Colunas vazias
tabela = tabela.dropna(how="all", axis=1) # dropna é para excluir valores especificos, all para excluir colunas completamente vazias, any é para alguns valores vazios da coluna.

# Linhas vazias
tabela = tabela.dropna(how="any", axis=0)


# In[24]:


# Passo 4: Analise exploratória 
display(tabela["Churn"].value_counts())
display(tabela["Churn"].value_counts(normalize=True).map("{:.1%}".format))


# In[35]:


# Passo 5: Olhando as colunas da nossa base de dados criar hipoteses para o motivo para o cancelamento
import plotly.express as px

for coluna in tabela.columns:
    print(coluna)
    #coluna = "MesesComoCliente"
    grafico = px.histogram(tabela, x=coluna, color="Churn")
    grafico.show()


# ### Conclusões e Ações

# Escreva aqui suas conclusões:
# 
# Clientes com famílias maiores (casados e com dependentes) tendem a cancelar menos
# 
# Será que não vale a pena a gente dar um número de graça para o filho do cliente, para o marido/esposa do cliente?
# MesesComoCliente baixo tem MUITO, mas MUITO mais chance de cancelar:
# 
# Talvez a 1ª experiência do cliente tá sendo ruim
# Talvez a gente tá trazendo clientes desqualificados
# Ideia: pode ser interessante a gente criar um programa de incentivo ao cliente nos primeiros meses
# Clientes de Fibra tem uma taxa de cancelamento muito alta:
# 
# Temos que verificar o serviço de fibra, temos algum problema ali
# Quantos mais serviços o cliente tem, menor a chance dele cancelar:
# 
# Oportunidade Gigantesca: criar um programa de incentivo aos outros serviços
# QUase todos os cancelamentos da empresa estão no contrato mensal:
# 
# Plano de incentivo ao contrato anual ou 2 anos -> vamos dar desconto pro cara do contrato anual
# Evitar Boleto Eletrônico
# 
# Incentivar os clientes a mudarem pra cartão de cre´dito ou débito automático
