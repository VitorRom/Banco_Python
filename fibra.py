def recomendar_plano(consumo_mensal):
  """
  Função que recomenda o plano de internet ideal com base no consumo mensal de dados.

  Argumentos:
    consumo_mensal: Valor float que representa o consumo médio mensal de dados em GB.

  Retorno:
    String contendo o plano de internet recomendado.
  """

  if consumo_mensal <= 10:
    plano_recomendado = "Plano Essencial Fibra - 50Mbps"
  elif consumo_mensal <= 20:
    plano_recomendado = "Plano Prata Fibra - 100Mbps"
  else:
    plano_recomendado = "Plano Premium Fibra - 300Mbps"

  return plano_recomendado

# Solicita ao usuário que insira o consumo médio mensal de dados:
consumo = float(input())

# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:
print(recomendar_plano(consumo))