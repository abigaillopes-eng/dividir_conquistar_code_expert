import pytest
from src.google_menire.google_service import GoogleService
from src.errors.validacao_langchain import ErroDeValidacaoLangchain

def test_call_google_service_unit_error():
    
    prompt = 2
    with pytest.raises(ErroDeValidacaoLangchain):
        GoogleService.chamar_gemini_2_5(prompt)
    
def test_call_google_service_unit_success():
    
    prompt = "Gere um código em python que some 300000 números, faca a divisão do menor deles por 328 e depois retorne o desvio padrão da média."
    try:
        GoogleService.chamar_gemini_2_5(prompt)
    except ErroDeValidacaoLangchain as erro:
        assert False, f"Um valor inválido foi fornecido: {erro}"
        
