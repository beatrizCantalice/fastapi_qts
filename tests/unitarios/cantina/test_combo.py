import pytest
from app.cantina.combo import calcular_descontos_combo

@pytest.mark.parametrize(
    "quantidade, perfil, desconto_esperado",
    [
        (1, "estudante", 0.0),  # Menos de 2 itens, sem desconto
        (2, "estudante", 0.15),  # 2 itens, estudante
        (5, "estudante", 0.20),  # 5 itens, estudante
        (3, "professor", 0.10),  # 3 itens, professor
        (4, "visitante", 0.0),   # Menos de 2 itens, visitante
        (0, "estudante", 0.0),  # 0 itens, estudante
    ]
)
def test_calcular_descontos_combo(quantidade, perfil, desconto_esperado):
    resultado = calcular_descontos_combo(quantidade, perfil)
    assert resultado == desconto_esperado