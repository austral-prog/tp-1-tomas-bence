def time():
    """
    Ejercicio 4 - Calculadora de Tiempo

    Dado un total de segundos, calcular e imprimir:
    1. Horas completas
    2. Minutos completos restantes
    3. Segundos restantes
    """
    total_segundos = 3665
    total_minutos = total_segundos / 60
    total_horas = total_minutos / 60
    segundos_hora= 60*60
    minutos_hora = 60
    segundos_minuto = 60
    rest_minutos = total_minutos - minutos_hora
    rest_segundos = total_segundos - segundos_hora-segundos_minuto
    print(int(total_horas))
    print(int(rest_minutos))
    print(rest_segundos)
time()
