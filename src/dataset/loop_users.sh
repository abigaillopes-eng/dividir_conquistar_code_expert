#!/bin/bash
# Script: loop_users.sh
# Propósito: Exemplo de iteração (loop 'for') sobre uma lista estática.

# Lista de usuários pré-definida
USER_LIST=("alice" "bob" "charlie" "david")

# Função que processa a lista
process_user_list() {
    echo "Iniciando processamento de usuários..."
    
    # Bloco lógico 'for'
    # "${USER_LIST[@]}" é a forma segura de expandir um array
    for USER in "${USER_LIST[@]}"; do
        if [[ -n "$USER" ]]; then
            echo "Processando usuário: $USER"
            # Exemplo de ação: criar um diretório home (simulado)
            # mkdir -p "/home/$USER/welcome"
        fi
    done
    
    echo "Processamento concluído."
}

main() {
    process_user_list
}

main