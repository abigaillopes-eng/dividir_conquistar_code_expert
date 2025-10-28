#!/bin/bash
# Script: check_root.sh
# Propósito: Um script de guarda (guard clause) que impede a execução 
#            se o usuário não for root (UID 0).

# Função de verificação de permissão
check_root() {
    # $(id -u) retorna o ID numérico do usuário
    if [[ $(id -u) -ne 0 ]]; then
        echo "ERRO: Este script deve ser executado como root." >&2
        return 1
    fi
    return 0
}

# Bloco principal de execução
check_root
if [[ $? -ne 0 ]]; then
    exit 1 # Sai se a verificação de root falhar
fi

echo "Executando como root. Prosseguindo com a tarefa..."
# (O resto do script viria aqui)
exit 0