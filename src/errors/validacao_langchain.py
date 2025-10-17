class ErroDeValidacaoLangchain(Exception):
    """Exceção levantada quando recebemos erro do Langchain."""
    
    def __init__(self, campo, valor_invalido, mensagem="Um valor inválido foi fornecido!"):
        
        self.campo = campo
        self.valor_invalido = valor_invalido
        
        mensagem_completa = f"{mensagem}: Campo '{campo}' recebeu o valor '{valor_invalido}'."
        
        super().__init__(mensagem_completa)