""" VARIÁVEIS, CONSTANTE E COMPLEXIDADE DE CÓDIGO """

"""
CONSTANTE = 'Variáveis' que não vão mudar
Muitas condições no mesmo if (ruim)
      <- Contagem de complexidade (ruim)
"""

speed_car = 61 # Velocidade atual do carro
position_car = 100 # Local (KM) em que o carro está na estrada

TRAFFIC_RADAR = 60 # Velocidade máxima do radar
POSITION_RADAR = 100 # Local (KM) onde o radar 1 está na estrada
RADAR_RANGE = 1 # A distância onde o radar pega

if speed_car > TRAFFIC_RADAR:
  print('The car crossed the radar threshold')

if position_car >= (POSITION_RADAR - RADAR_RANGE) and position_car <= (POSITION_RADAR + TRAFFIC_RADAR) and speed_car > TRAFFIC_RADAR:
  print('Car fined by radar')

""" CODIGO OTIMIZADO """

speed_car = 61 # Velocidade atual do carro
position_car = 100 # Local (KM) em que o carro está na estrada
fined_car = \
  position_car >= (POSITION_RADAR - RADAR_RANGE) \
  and position_car <= (POSITION_RADAR + TRAFFIC_RADAR) \
  and speed_car > TRAFFIC_RADAR

TRAFFIC_RADAR = 60 # Velocidade máxima do radar
POSITION_RADAR = 100 # Local (KM) onde o radar 1 está na estrada
RADAR_RANGE = 1 # A distância onde o radar pega

if speed_car > TRAFFIC_RADAR:
  print('The car crossed the radar threshold')

if fined_car:
  print('Car fined by radar')