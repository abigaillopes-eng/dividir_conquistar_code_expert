from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI

class OpenAIService():
    # \\TODO: Implementar corretamente, usando a chave da OpenAI
    def chamar_gpt_3():
        
        load_dotenv()

        if not os.getenv("OPENAI_API_KEY"):
            print("ERRO: A variável de ambiente OPENAI_API_KEY não está configurada.")
            print("Por favor, verifique seu arquivo .env.")
            exit()
        else:

            llm = ChatOpenAI(model="gemini-2.5-flash")

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
            mensagem_valida = [
                ("system", INSTRUCAO_SISTEMA_CODIGO),
                ("user", TAREFA_ESPECIFICA)
            ]

            # Teste de Guardrail
            mensagem_invalida = [
                ("system", INSTRUCAO_SISTEMA_CODIGO),
                ("user", "Quantos anos tem o Michael Jackson?")
            ]

        try:
            #ai_msg = llm.invoke(messages_para_llm)
            ai_msg = llm.invoke(mensagem_invalida)

            print(f"\n--- Resposta do GPT  ---")
            print("\n" + ai_msg.content)
            print("\n--------------------------")
            
        except Exception as e:
            print(f"\nOcorreu um erro na chamada do GPT: {e}")


if __name__ == "__main__":
    OpenAIService.chamar_gpt_3()