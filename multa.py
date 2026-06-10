def calcular_multa_com_carencia(dias_atraso, valor_dia, carencia=2):
    if dias_atraso <= carencia:
        return 0.0
    
    dias_cobrados = dias_atraso - carencia
    return float(dias_cobrados * valor_dia)
