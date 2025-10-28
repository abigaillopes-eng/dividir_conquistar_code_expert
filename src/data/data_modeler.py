class coversa:
    Human: str
    Chat: str
    
class Historico:
    #array de Conversas
    conversas = []

class DataModeler:
    
    pre_texto: str
    texto: str # Ou vai ser 
    pos_texto: str
    historico_conversa: Historico
    
    
    def __init__(self, doc_name: str, prompt: str, doc_id: str):
        self.doc_name = doc_name
        
    # Tipos de códigos:
    # Windows Batch
    # PowerShell 
    # PowerShell Core 
    # Python
    # Bash OK
    
    # 5 prompts para 10 scripts para cada linguagem
    
    
    # Modelo temporário para comparar os bashs do dataset com os códigos que temos
    # código B0N - ids para códigos em bash
    dataset_prompts = {
        #B01
        "check_status": [
            "Me dê um script bash para verificar se um site está online.",
            "Como eu posso checar o código de status HTTP (200, 404, etc.) de uma URL pelo terminal?",
            "Preciso de um exemplo de `curl` que mostre apenas o `http_code` e ignore o corpo da página.",
            "Gere um código de monitoramento simples para saber se minha API está respondendo 200 OK.",
            "Qual a melhor forma de fazer um *health check* de um endpoint usando shell script?"
        ],
        #B02
        "clean_temp": [
            "Eu preciso de um script para limpar arquivos temporários antigos.",
            "Como eu posso deletar automaticamente arquivos com mais de 7 dias em um diretório?",
            "Mostre um exemplo de comando `find` para remover arquivos por data de modificação (`mtime`).",
            "Meu disco está enchendo. Crie um script bash para limpar a pasta `/tmp` de lixo antigo.",
            "Como apagar todos os arquivos `.tmp` e `.log` mais velhos que uma semana?"
        ],
        #B03
        "backup_dir": [
            "Gere um script bash para fazer backup de um diretório.",
            "Como eu posso compactar uma pasta (usando `tar.gz`) e adicionar a data atual no nome do arquivo?",
            "Qual o comando `tar` correto para criar um arquivo compactado e movê-lo para outra pasta?",
            "Preciso de um script que automatize o backup da minha pasta `/var/www` para `/mnt/backups`.",
            "Mostre um exemplo de `tar` que usa `basename` e `date` para nomear o arquivo de backup."
        ],
        #B04
        "validate_arg": [
            "Preciso de uma função bash para validar se uma entrada é um número.",
            "Como eu verifico se o primeiro argumento (`$1`) de um script é um número inteiro?",
            "Mostre um exemplo de `if` com regex (`=~`) para checar se uma variável é numérica.",
            "Meu script quebra se o usuário digitar 'abc' em vez de '123'. Como eu impeço isso?",
            "Qual a melhor forma de fazer validação de input (type checking) em bash?"
        ],
        #B05
        "process_log": [
            "Gere um script para processar um log e contar quantos erros de cada tipo eu tenho.",
            "Como eu conto as ocorrências únicas de uma palavra específica em um arquivo de log?",
            "Qual o pipeline (usando `|`) para filtrar linhas com `grep`, extrair a última coluna com `awk` e depois contar com `uniq -c`?",
            "Preciso analisar um `access.log`. Como eu encontro os tipos de 'ERROR' mais comuns e ordeno por frequência?",
            "Script para extrair a última palavra de todas as linhas que contêm 'ERROR' e contar."
        ],
        #B06
        "update_config": [
            "Me dê um script bash para atualizar um valor em um arquivo de configuração.",
            "Como eu mudo o valor de uma variável (ex: `VERSION=1.0` para `VERSION=2.0`) dentro de um arquivo `.conf`?",
            "Qual o comando `sed -i` para substituir uma linha inteira que começa com 'KEY='?",
            "Preciso de um script de deploy que atualize a `DATABASE_URL` no meu `settings.ini`.",
            "Como editar um arquivo de texto programaticamente no bash para mudar uma configuração?"
        ],
        #B07
        "check_root": [
            "Preciso de um script que verifica se o usuário é root.",
            "Como eu faço para meu script bash parar (dar `exit`) se não for executado com `sudo`?",
            "Me dê um exemplo de `if` que usa `$(id -u)` para checar se o UID é 0.",
            "Quero adicionar uma verificação de permissão no início do meu script de instalação.",
            "Meu script falha com 'Permissão negada'. Como eu forço a execução como root no início?"
        ],
        #B08
        "loop_users": [
            "Me dê um exemplo de loop `for` em bash.",
            "Como eu itero sobre um array (lista) de strings no bash?",
            "Qual a sintaxe correta para `for USER in \"${ARRAY[@]}\"`?",
            "Preciso executar o mesmo comando para três usuários diferentes ('alice', 'bob', 'charlie'). Como fazer isso em um loop?",
            "Como processar uma lista de itens em bash?"
        ],
        #B09
        "wait_file": [
            "Preciso de um script que espera um arquivo ser criado.",
            "Como eu pauso meu script bash e só continuo a execução depois que outro processo criar o arquivo `done.txt`?",
            "Me dê um exemplo de loop `while` que usa `sleep` e `test -f` (ou `[ ! -f ]`).",
            "Meu script de deploy precisa esperar o `app.pid` existir antes de prosseguir. Como fazer essa espera?",
            "Como adicionar um timeout a um script que fica esperando por um arquivo?"
        ],
        #B10
        "disk_usage": [
            "Me dê um script que mostra o uso de disco (disk usage).",
            "Como eu encontro os 5 diretórios que mais ocupam espaço em `/var`?",
            "Qual o pipeline de comandos para `du`, `sort -rh` e `head` para achar os maiores arquivos?",
            "Meu disco está cheio. Como eu identifico quais pastas estão consumindo mais espaço?",
            "Script para listar o tamanho resumido (`du -sh`) de todos os subdireitóros e ordenar do maior para o menor."
        ]
    }

# Acessar os prompts do primeiro script
# print(dataset_prompts["B01_check_status"])