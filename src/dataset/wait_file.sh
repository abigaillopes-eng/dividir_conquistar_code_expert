#!/bin/bash
# Script: wait_file.sh
# Propósito: Pausa a execução do script até que um arquivo específico exista.

if [[ -z "$1" ]]; then
    echo "Uso: $0 <caminho_do_arquivo_para_esperar>" >&2
    exit 1
fi

FILE_PATH="$1"
TIMEOUT_SECONDS=60
ELAPSED=0

# Bloco lógico 'while' (loop de espera)
# [ ! -f "$FILE_PATH" ]: Testa se o arquivo NÃO (!) existe (-f)
echo "Aguardando pelo arquivo: $FILE_PATH (Timeout: $TIMEOUT_SECONDS s)"

while [[ ! -f "$FILE_PATH" ]]; do
    if [[ $ELAPSED -ge $TIMEOUT_SECONDS ]]; then
        echo "ERRO: Timeout atingido. Arquivo não encontrado." >&2
        exit 1
    fi
    
    sleep 5
    ELAPSED=$((ELAPSED + 5))
    echo "..."
done

echo "SUCESSO: Arquivo '$FILE_PATH' encontrado. Continuando."
exit 0