def calcular_descontos_combo(quantidade_itens: int, tipo_cliente: str) -> float:
    """Calcula a taxa percentual de desconto com base na quantidade e perfil."""
    if quantidade_itens < 2:
        return 0.0
    
    perfil = tipo_cliente.strip().lower() if tipo_cliente else ""

    if perfil == "estudante":
        if quantidade_itens >= 5:
            return 0.20  # 20% de desconto para estudantes com 5 ou mais itens
        return 0.15  # 15% de desconto para estudantes com menos de 5 itens

    if perfil == "professor":
        return 0.10  # 10% de desconto para professores

    return 0.0