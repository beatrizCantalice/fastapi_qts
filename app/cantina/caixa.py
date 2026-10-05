from app.cantina.combo import calcular_descontos_combo
from app.cantina.embalagem import calcular_taxa_embalagem

def processar_venda(
        valor_bruto:float,
        quantidade_itens:int,
        tipo_cliente:str,
        levar_viagem:bool
) -> dict:
    """Processa a venda da cantina integrando regras de desconto e embalagem."""
    if valor_bruto <= 0 or quantidade_itens <= 0:
        return {
            "sucesso": False,
            "motivo": "dados da venda inválidos",
            "total_final": 0.0,
        }