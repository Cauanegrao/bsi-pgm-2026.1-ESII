def calcular_multa_com_carencia(dias_atraso, valor_dia, carencia=2):    
    dias_cobrados = max(0, dias_atraso - carencia)
    return float(dias_cobrados * valor_dia)
