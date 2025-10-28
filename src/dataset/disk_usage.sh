#!/bin/bash
# Script: disk_usage.sh
# Propósito: Mostra os 5 principais diretórios que mais consomem espaço
#            em um local específico (padrão: /var/log).

TARGET_DIR="${1:-/var/log}" # Usa $1 se fornecido, senão usa /var/log

if [[ ! -d "$TARGET_DIR" ]]; then
    echo "ERRO: Diretório '$TARGET_DIR' não encontrado." >&2
    exit 1
fi

echo "Verificando os 5 maiores consumidores em $TARGET_DIR..."

# Bloco lógico de pipeline (du, sort, head)
# du -sh ./* : (disk usage) -s (resumo) -h (human-readable) nos subdiretórios
# sort -rh: (sort) -r (reverso) -h (human-numeric sort)
# head -n 5: Pega os 5 primeiros

(cd "$TARGET_DIR" && du -sh ./* 2>/dev/null | sort -rh | head -n 5)

if [[ ${PIPESTATUS[0]} -ne 0 ]]; then
    echo "AVISO: Pode ter ocorrido um erro ao ler alguns diretórios (permissão?)." >&2
fi

exit 0