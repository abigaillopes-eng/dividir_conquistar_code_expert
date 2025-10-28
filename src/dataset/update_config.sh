#!/bin/bash
# Script: update_config.sh
# Propósito: Usa 'sed' para atualizar uma chave em um arquivo .conf.

# Validação de entrada
if [[ $# -ne 3 ]]; then
    echo "Uso: $0 <arquivo.conf> <CHAVE> <NOVO_VALOR>" >&2
    exit 1
fi

CONFIG_FILE="$1"
KEY="$2"
NEW_VALUE="$3"

if [[ ! -f "$CONFIG_FILE" ]]; then
    echo "ERRO: Arquivo '$CONFIG_FILE' não encontrado." >&2
    exit 2
fi

# Bloco lógico 'sed'
# -i: Edita o arquivo "in-place" (no local)
# "s/^KEY=.*/KEY=NEW_VALUE/":
#   s = substitui
#   ^KEY= -> Linhas que começam (^) com a CHAVE seguida de =
#   .* -> Corresponde a qualquer coisa (o valor antigo)
#   KEY=NEW_VALUE -> O novo texto
echo "Atualizando $KEY em $CONFIG_FILE..."
sed -i "s/^${KEY}=.*/${KEY}=${NEW_VALUE}/" "$CONFIG_FILE"

echo "Atualização concluída."
exit 0