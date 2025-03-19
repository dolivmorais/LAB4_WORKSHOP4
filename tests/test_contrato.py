import pytest
from datetime import datetime
from src.contrato import Vendas, CategoriaEnum

def test_vendas_com_dados_validos():
    dados_validos = {
        "email": "B2u5D@example.com",
        "data": datetime.now(),
        "valor": 100.0,
        "produto": "carro",
        "quantidade": 22,
        "categoria": "categoria1",
    }

    vendas = Vendas(**dados_validos)

    assert vendas.email == dados_validos["email"]
    assert vendas.data == dados_validos["data"]
    assert vendas.valor == dados_validos["valor"]
    assert vendas.produto == dados_validos["produto"]
    assert vendas.quantidade == dados_validos["quantidade"]
    assert vendas.categoria == CategoriaEnum.categoria1  # Correto

def test_vendas_com_dados_invalidos():
    dados_invalidos = {
        "email": "B2u5D@example.com",
        "data": datetime.now(),
        "valor": 11.6,
        "produto": "carro",
        "quantidade": 2222,
        "categoria": "catego",  # Categoria inválida
    }


    with pytest.raises(ValueError):
        Vendas(**dados_invalidos)
