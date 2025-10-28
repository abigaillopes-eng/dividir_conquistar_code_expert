#!/bin/bash
# Script: validate_arg.sh
# Propósito: Script utilitário que verifica se uma entrada é numérica.

# Função de responsabilidade única para validação
is_numeric() {
    local input="$1"
    local re='^[0-9]+$' # Expressão regular para números inteiros positivos
    
    if ! [[ "$input" =~ $re ]]; then
        echo "ERRO: '$input' não é um número inteiro positivo." >&2
        return 1
    else
        echo "SUCESSO: '$input' é numérico."
        return 0
    fi
}

# Bloco principal
if [[ -z "$1" ]]; then
    echo "Uso: $0 <valor_para_testar>" >&2
    exit 1
fi

is_numeric "$1"
exit $?