from app.descontos.descontos import calcular_desconto


# valor negativo
def test_valor_negativo():
    assert calcular_desconto(-10, True) == 0


# valor exatamente 0
def test_valor_zero():
    assert calcular_desconto(0, False) == 0


# cliente VIP com valor válido
def test_cliente_vip():
    assert calcular_desconto(100, True) == 80


# cliente não VIP com valor válido
def test_cliente_nao_vip():
    assert calcular_desconto(100, False) == 90


# valor positivo muito pequeno
def test_valor_pequeno():
    resultado = calcular_desconto(0.01, False)
    assert round(resultado, 3) == 0.009


# valor maior
def test_valor_maior():
    assert calcular_desconto(200, True) == 160