#!/bin/bash
# Script: backup_dir.sh
# Propósito: Cria um arquivo .tar.gz de um diretório de origem e o move para um diretório de destino.

# Validação de argumentos
if [[ $# -ne 2 ]]; then
    echo "Uso: $0 <diretorio_origem> <diretorio_destino>" >&2
    exit 1
fi

SRC_DIR="$1"
DEST_DIR="$2"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
# basename extrai o nome do diretório (ex: /var/log -> log)
BACKUP_NAME="backup_$(basename "$SRC_DIR")_$TIMESTAMP.tar.gz"
DEST_FILE="$DEST_DIR/$BACKUP_NAME"

# Verifica se a origem existe
if [[ ! -d "$SRC_DIR" ]]; then
    echo "ERRO: Diretório de origem '$SRC_DIR' não encontrado." >&2
    exit 2
fi

# Garante que o destino exista
mkdir -p "$DEST_DIR"

# Bloco lógico de backup (tar e mv)
echo "Criando backup de $SRC_DIR..."
tar -czf "$BACKUP_NAME" -C "$(dirname "$SRC_DIR")" "$(basename "$SRC_DIR")"

if [[ $? -eq 0 ]]; then
    echo "Movendo $BACKUP_NAME para $DEST_DIR..."
    mv "$BACKUP_NAME" "$DEST_FILE"
    echo "Backup concluído: $DEST_FILE"
    exit 0
else
    echo "ERRO: Falha ao criar o arquivo tar." >&2
    rm -f "$BACKUP_NAME" # Limpa o arquivo tar parcial
    exit 3
fi