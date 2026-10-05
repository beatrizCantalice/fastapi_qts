import time, pytest
from app.faturamento.cobranca import processar_cobranca

@pytest.mark.parametrize(
    "valor_base, plano, dias_atraso, final_esperado",
    [
        (-1, "BASICO", -20, -1.00),
        (0, "PREMIUM", -50, -1.0),
        (506.00, "EMPRESARIAL", -90, -1.0),
        (200.00, "         ", 0, -2.00),
        (450.00, "PREMI  UM", 0, -2.00),
        (300.00, "EM PRESA RIal", 0, -2.00),
        (420.00, "BASICO", 0, 420.00),
        (500.00, "PREMIUM", 0, 450.00),
        (630.00, "EMPRESARIAL", 0, 504.00),
        (750.00, "BASICO", 30, 867.5),
        (890.00, "EMPRESARIAL", 31, 957.72),
        (759.00, "PREMIUM", 90, 1322.89),

    ],
)

def test_processar_cobranca_atividade(
    valor_base, plano, dias_atraso, final_esperado
):
    assert processar_cobranca(valor_base, plano, dias_atraso) == final_esperado


def test_tempo_processamento_cobranca():
    inicio = time.perf_counter()
    resultado = processar_cobranca(100.0)
    fim = time.perf_counter()
    tempo_decorrido = fim - inicio

    assert resultado is True

    # O tempo deve ser inferior a 100 milissegundos (0.1 segundos) 
    assert tempo_decorrido < 0.1