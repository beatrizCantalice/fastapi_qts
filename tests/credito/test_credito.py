import pytest

from app.credito.credito import classificar_credito

@pytest.mark.parametrize(
    "renda_mensal, score_credito, restrito, retorno_esperado",
    [
        (0, 88, True, "renda invalida"),
        (-7, -32, True, "renda invalida"),
        (89, -2, False, "score invalido"),
        (467, 2000, False, "score invalido"),
        (167, 700, True, "reprovado"),
        (245, 200, False, "reprovado"),
        (210, 567, False, "aprovado padrao"),
        (400, 998, False, "aprovado premium")
    ],
)

def test_classificar_credito(
    renda_mensal, score_credito, restrito, retorno_esperado
):
    assert classificar_credito(renda_mensal, score_credito, restrito) == retorno_esperado