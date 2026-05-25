def calcular_desconto(valor: float, cliente_vip: bool):

    if valor <= 0:
        return 0

    if cliente_vip:
        return valor * 0.8

    return valor * 0.9