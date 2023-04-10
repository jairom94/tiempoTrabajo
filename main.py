import time
horaInicio = 8
horaSalida = 19
horaActual = time.strftime('%H', time.localtime()) 
#minutos = time.strftime('%M', time.localtime())
if int(horaActual) >= horaSalida:
  print('Apresurate es hora de ir a casa.')
elif (int(horaActual) > horaInicio) and (int(horaActual) < horaSalida):
  print(':( Aun queda', (horaSalida-int(horaActual)), 'antes de salir!!!')
