#!/bin/bash
# Script: check_status.sh
# Propósito: Verifica o status HTTP de uma URL passada como argumento.

# Função de responsabilidade única para verificar o status
check_status() {
    local url="$1"
    
    # -s (silencioso), -o /dev/null (descarta saída do corpo), -w (formata a saída)
    HTTP_STATUS=$(curl -s -o /dev/null -w "%{http_code}" "$url")
    
    if [[ "$HTTP_STATUS" -eq 200 ]]; then
        echo "SUCESSO: $url retornou HTTP $HTTP_STATUS"
        return 0
    else
        echo "ERRO: $url retornou HTTP $HTTP_STATUS"
        return 1
    fi
}

# Função principal que gerencia a execução e validação de entrada
main() {
    local target_url="$1"
    
    if [[ -z "$target_url" ]]; then
        echo "Uso: $0 <URL_completa>" >&2
        exit 1
    fi
    
    check_status "$target_url"
    # O código de saída do script será o código de retorno da função check_status
    exit $?
}

# Executa a função principal passando todos os argumentos do script
main "$@"