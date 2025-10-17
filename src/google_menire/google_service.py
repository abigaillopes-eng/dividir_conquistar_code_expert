from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from src.errors.validacao_langchain import ErroDeValidacaoLangchain

class GoogleService():

    def chamar_gemini_2_5 (prompt: str):
        
        load_dotenv()

        if not os.getenv("GOOGLE_API_KEY"):
            print("ERRO: A variável de ambiente GOOGLE_API_KEY não está configurada.")
            print("Por favor, verifique seu arquivo .env.")
            exit()
        else:

            llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

            # Para definir a Persona e as Regras de Conduta
            INSTRUCAO_SISTEMA_CODIGO = """
            Você é um Engenheiro de Software Sênior e um assistente especializado em **somente** gerar código-fonte, scripts e exemplos de programação.

            SUA ÚNICA FUNÇÃO É ESCREVER CÓDIGO.
            Você é capaz de gerar código em qualquer linguagem popular (Python, Java, Bash, C, C++, JavaScript, Ruby, R, Go, Rust, SQL, etc.).

            **REGRAS DE CONDUTA INEGOCIÁVEIS:**
            1.  **Geração de Código:** Para qualquer solicitação de programação, você deve fornecer o código-fonte COMPLETO, funcional e seguindo as melhores práticas da linguagem solicitada.
            2.  **Formato:** O código deve estar **sempre** encapsulado em um bloco Markdown de código (Ex: ```bash...``` ou ```python...```).
            3.  **Restrição de Escopo (Guardrail):** Se a pergunta **NÃO** for sobre programação, codificação, algoritmos, ou estruturas de dados, você deve responder **EXATAMENTE** a seguinte frase:
                "Eu sou uma api para gerar códigos, por favor me pergunte algo relacionado à programação."
            4.  **Clareza:** Nunca inicie sua resposta com uma introdução de texto; vá direto ao bloco de código, a menos que a Regra 3 se aplique.
            """
            
            # O pedido de código
            TAREFA_ESPECIFICA = """
            Crie um script Bash completo, eficiente e resiliente para a seguinte tarefa:

            [DESCRIÇÃO DA TAREFA: Monitore o uso de disco em '/' e envie uma notificação para 'admin@empresa.com' se o uso for superior a 90%. O script deve ser executado pelo cron.]

            **Requisitos Adicionais (Bash):**
            - Shebang e Robustez: O script deve começar com #!/usr/bin/env bash e usar `set -euo pipefail`.
            - Função de Erro: Crie uma função chamada `erro_handler` que registra o erro (linha e comando que falhou) e sai com código de falha. Use `trap`.
            - Variáveis: Use aspas duplas em todas as variáveis (`"$VAR"`) e declare variáveis globais em letras maiúsculas.

            Após o bloco de código, inclua a seção 'Análise de Boas Práticas' explicando o uso do `trap` e de `set -euo pipefail`.
            """

            # Formato LangChain Padronizado (Tuplas de role, content)
            # Exemplo de mensagem_valida
            # \\TODO: tirar isso daqui
            mensagem_valida = [
                ("system", INSTRUCAO_SISTEMA_CODIGO),
                ("user", TAREFA_ESPECIFICA)
            ]

        try:
            if prompt is not None:
                prompt = str(prompt)
                
                mensagem_para_modelo = [
                    ("system", INSTRUCAO_SISTEMA_CODIGO),
                    ("user", prompt)
                ]
                
                #ai_msg = llm.invoke(messages_para_llm)
                ai_msg = llm.invoke(mensagem_para_modelo)

                print(f"\n--- Resposta do Gemini  ---")
                print("\n" + ai_msg.content)
                print("\n--------------------------")
                return ai_msg.content
            
        except Exception as e:
            print(f"\nOcorreu algum erro na chamada do Gemini: {e}")
            raise ErroDeValidacaoLangchain (e)

if __name__ == "__main__":
    GoogleService