from google_menire.google_service import GoogleService
from anthropic_menire.anthropic_service import AnthropicService
from openai_menire.openAI_service import OpenAIService

class Menire:
    
    def main():
    
        while True:
        
            print("Olá! Sou uma API que chama vários LLMs!")
            
            try:
                print("1 - Anthropic")
                print("2 - Google")
                print("3 - OpenAI")
                
                escolhaOperacao = int(input("Qual LLM você quer chamar? "))
                pergunta = str(input("Qual pergunta você quer fazer?\n"))

                match escolhaOperacao:
                    case 1: 
                        # Anthropic
                        AnthropicService.chamar_claude_sonnet_4(pergunta)
                    case 2:
                        # Google
                        GoogleService.chamar_gemini_2_5(pergunta)
                    case 3:
                        # OpenAI
                        print("Desculpe, mas ainda estamos em obra para chamar essa API...")
                        # OpenAIService.chamar_gpt_3()
                    case _:
                        print("A opção inserida é inválida. Digite um número inteiro entre 1 e 3.")
            except Exception as e:
                print(f"\nOcorreu um erro na chamada da Menire: {e}")
                continue
            
            repetir = input("\nDeseja chamar outra API de LLMs? (s/n): ").strip().lower()
            if repetir != 's':
                print("Encerrando... Até a próxima!")
                break


if __name__ == "__main__":
    Menire.main()