#!/bin/bash
# Script: clean_temp.sh
# Propósito: Remove arquivos .tmp e .log com mais de 7 dias do diretório /tmp.

TARGET_DIR="/tmp"
DAYS_OLD=7

echo "Iniciando limpeza de arquivos antigos em $TARGET_DIR..."

# Bloco lógico principal usando 'find'
# -type f: apenas arquivos
# -mtime +$DAYS_OLD: modificados há mais de $DAYS_OLD dias
# -name "*.tmp" -o -name "*.log": corresponde a ambas extensões
# -print: (Opcional, mas bom para log)
# -delete: (Ação de remoção eficiente)

find "$TARGET_DIR" -type f \( -name "*.tmp" -o -name "*.log" \) -mtime "+$DAYS_OLD" -print -delete

if [[ $? -eq 0 ]]; then
    echo "Limpeza concluída com sucesso."
    exit 0
else
    echo "ERRO: Ocorreu um problema durante a execução do find." >&2
    exit 1
fi