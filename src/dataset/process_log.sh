#!/bin/bash
# Script: process_log.sh
# Propósito: Processa um arquivo de log, encontra linhas com "ERROR",
#           extrai a última palavra (supostamente o tipo de erro) e conta ocorrências.

LOG_FILE="$1"

if [[ ! -f "$LOG_FILE" ]]; then
    echo "Uso: $0 <caminho_do_arquivo_de_log>" >&2
    exit 1
fi

echo "Contagem de erros únicos em $LOG_FILE:"

# Bloco lógico de processamento (Pipeline)
# grep: Filtra linhas
# awk: Extrai a última coluna/palavra da linha ($NF)
# sort: Agrupa itens idênticos
# uniq -c: Conta os itens agrupados
# sort -rn: Ordena numericamente (r=reverso, n=numérico)

grep -i "ERROR" "$LOG_FILE" | awk '{print $NF}' | sort | uniq -c | sort -rn

if [[ ${PIPESTATUS[0]} -ne 0 ]]; then
    echo "AVISO: Nenhum erro encontrado ou falha no grep." >&2
fi

exit 0