import numpy as np
import pandas as pd
import plotly.express as px

  
     
#Média Calculada    
#Calcular a média do K/D por jogador
kd_por_player = jogadores_brasileiros.groupby('player')['K/D'].mean().reset_index()

# Filtrar jogadores com média de K/D acima de 1.10
kd_acima_de_110 = kd_por_player[kd_por_player['K/D'] > 1.10]

#Criar o gráfico interativo
fig = px.bar(kd_acima_de_110, x='player', y='K/D', title='Jogadores com Média de K/D Acima de 1.10',
             labels={'player': 'Jogador', 'K/D': 'Média de K/D'})

# Mostrar o gráfico
fig.show()



#Quantidade de Pistolas
# Contar os valores da coluna (pistol_played)
pistol_counts = df['pistol_played'].value_counts().reset_index()
pistol_counts.columns = ['pistol_played', 'count']

# Criar o gráfico de barras básico
fig = px.bar(pistol_counts, x='pistol_played', y='count')

# Mostrar o gráfico
fig.show()
     
   
   
     
 #Maiores Jogadas com Pistolas   
 # Contar os valores da coluna 'pistol_played'
pistol_counts = df['pistol_played'].value_counts().head(14).reset_index()
pistol_counts.columns = ['pistol_played', 'count']

# Criar o gráfico de barras básico com Plotly
fig = px.bar(pistol_counts, x='pistol_played', y='count',
             title='10 Maiores Jogadas com Pistolas', labels={'pistol_played': 'Pistol Played', 'count': 'Jogadas'}, color='count')

# Mostrar o gráfico
fig.show()
     
     
     
 #Contagem de Defesa Maiores Jogadas   e gráfico de barras 
 # Contar os valores da coluna 'def_played'
def_counts = df['def_played'].value_counts().reset_index()
def_counts.columns = ['def_played', 'count']

# Criar o gráfico de barras básico com Plotly
fig = px.bar(def_counts, x='def_played', y='count',
             title='Contagem de Defesas Jogadas',
             labels={'def_played': 'Defesa Jogada', 'count': 'Quantidade'})

# Mostrar o gráfico
fig.show()    
     
   
   
#Contagem de valores na coluna com relação a defesa
#Contar os valores da coluna (def_played) e ordenar pelo índice
def_counts = df['def_played'].value_counts().sort_index().reset_index()
def_counts.columns = ['round', 'count']

# Criar o gráfico de linha básico com Plotly
fig = px.line(pistol_counts, x='round', y='count',
              title='Tendência de Jogadas com Pistolas',
              labels={'round': 'Número da Rodada', 'count': 'Quantidade de Jogadas'},
              markers=True)

# Mostrar o gráfico
fig.show()
 
 
#Contagem de valores da coluna com relação ao ataque 
# Contar os valores da coluna 'def_played'
def_counts = df['atk_played'].value_counts().reset_index()
def_counts.columns = ['atk_played', 'count']

# Criar o gráfico de barras básico com Plotly
fig = px.bar(def_counts, x='atk_played', y='count',
             title='Contagem de Ataques Jogadas',
             labels={'atk_played': 'Ataque Jogada', 'count': 'Quantidade'})

# Mostrar o gráfico
fig.show()      
     
     


import pandas as pd
import plotly.express as px

# Dados fornecidos
data = {
    'País': ['Estados Unidos', 'Japão', 'Alemanha', 'Turquia', 'Brasil', 'França', 'Coreia do Sul', 'Reino Unido', 'Espanha', 'China'],
    'Jogadores': [581, 378, 367, 361, 326, 324, 309, 278, 264, 231]
}

# Criar DataFrame
df = pd.DataFrame(data)

# Criar gráfico de pizza
fig = px.pie(df, values='Jogadores', names='País', title='Porcentagem de Jogadores de Valorant por País e que mais tem  títulos',
             color_discrete_sequence=px.colors.sequential.RdBu)

# Destacar o país com mais títulos
fig.update_traces(pull=[0.1 if country == 'Coreia do Sul' else 0 for country in df['País']],
                  textinfo='percent+label')

# Mostrar gráfico
fig.show()
        