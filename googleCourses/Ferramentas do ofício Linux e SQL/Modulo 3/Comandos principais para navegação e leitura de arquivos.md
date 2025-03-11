## Navegando no Sistema de Arquivos Linux

**A Importância da Navegação no Linux:**

- Analistas de segurança precisam navegar pelos sistemas de arquivos para:
    - Localizar e analisar registros de servidores (logs).
    - Verificar configurações de arquivos.
    - Investigar acessos não autorizados.

**O Filesystem Hierarchy Standard (FHS):**

- Organiza os dados no Linux de forma hierárquica, como uma árvore.
- O diretório raiz (`/`) é o ponto de partida.
- Subdiretórios se ramificam a partir da raiz.
- Barras (`/`) são usadas para representar a hierarquia (ex: `/home/analista/logs`).

**Comandos de Navegação:**

- `pwd`: Exibe o diretório de trabalho atual.
- `ls`: Lista arquivos e diretórios no diretório atual.
- `cd`: Altera o diretório de trabalho.

**Exemplo Prático:**

1. `pwd`: Exibe `/home/analista`.
2. `ls`: Lista os arquivos e diretórios em `/home/analista`.
3. `cd logs`: Altera o diretório para `/home/analista/logs`.
4. `pwd`: Exibe `/home/analista/logs`.

**Comandos para Ler Conteúdo de Arquivos:**

- `cat`: Exibe o conteúdo completo de um arquivo.
- `head`: Exibe as primeiras 10 linhas de um arquivo.

**Exemplo Prático:**

1. `cat access.txt`: Exibe todo o conteúdo do arquivo `access.txt`.
2. `head access.txt`: Exibe as 10 primeiras linhas do arquivo `access.txt`.

**Dicas Importantes:**

- Utilize o comando `man comando` para obter informações sobre os comandos.
- Pratique a navegação e a leitura de arquivos no Linux para aprimorar suas habilidades.
- Utilize a tecla `Tab` para autocompletar nomes de arquivos e diretórios.

**Conclusão:**

A navegação no sistema de arquivos Linux é uma habilidade fundamental para analistas de segurança. O domínio dos comandos `pwd`, `ls`, `cd`, `cat` e `head` permite realizar tarefas essenciais na análise de registros e investigação de incidentes.

Próximo Modulo [[Navegar no Linux e ler o conteúdo dos arquivos]]
