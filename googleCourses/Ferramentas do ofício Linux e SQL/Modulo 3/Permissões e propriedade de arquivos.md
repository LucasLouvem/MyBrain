## Permissões de Arquivos e Diretórios no Linux: Um Guia para Analistas de Segurança

**A Importância das Permissões:**

- Permissões controlam o acesso a arquivos e diretórios, garantindo a segurança do sistema.
- A autorização é baseada na necessidade de conhecimento, limitando o acesso a dados confidenciais.

**Tipos de Permissões:**

- **Leitura (r):**
    - Arquivo: Permite visualizar o conteúdo.
    - Diretório: Permite listar arquivos e subdiretórios.
- **Gravação (w):**
    - Arquivo: Permite modificar o conteúdo.
    - Diretório: Permite criar, renomear e excluir arquivos.
- **Execução (x):**
    - Arquivo: Permite executar o arquivo (se for um executável).
    - Diretório: Permite acessar e navegar dentro do diretório.

**Tipos de Proprietários:**

- **Usuário (u):** Proprietário do arquivo/diretório.
- **Grupo (g):** Grupo ao qual o usuário pertence.
- **Outros (o):** Todos os outros usuários do sistema.

**Representação das Permissões:**

- Uma string de 10 caracteres representa as permissões.
- Exemplo: `drwxrwxrwx`
    - `d`: Diretório (ou `-` para arquivo).
    - `rwx`: Permissões de usuário (leitura, gravação, execução).
    - `rwx`: Permissões de grupo.
    - `rwx`: Permissões de outros.

**Verificando Permissões:**

- Comando `ls` com opções:
    - `ls -l`: Exibe permissões detalhadas.
    - `ls -a`: Exibe arquivos ocultos.
    - `ls -la`: Exibe permissões e arquivos ocultos.

**Exemplo Prático:**

1. `ls -l`: Exibe permissões de arquivos e diretórios no diretório atual.
2. `ls -a`: Exibe arquivos ocultos (começam com `.`).
3. `ls -la`: Combina as duas opções anteriores.

**Interpretação da Saída de `ls -l`:**

- A primeira coluna mostra as permissões (ex: `-rw-r--r--`).
- A segunda coluna indica o número de links físicos.
- A terceira coluna mostra o proprietário (usuário).
- A quarta coluna mostra o grupo.
- A quinta coluna mostra o tamanho do arquivo.
- A sexta coluna mostra a data de modificação.
- A sétima coluna mostra o nome do arquivo/diretório.

**Importância para Analistas de Segurança:**

- Configurar permissões adequadas protege arquivos confidenciais.
- Arquivos graváveis mundialmente (`-rwxrwxrwx`) representam riscos de segurança.
- Monitorar e auditar permissões é essencial para a segurança do sistema.

**Dicas Importantes:**

- Use `ls -l` para verificar as permissões detalhadas.
- Combine opções do `ls` para obter informações completas.
- Entenda a representação das permissões para interpretar a saída de `ls -l`.
- Monitore arquivos graváveis mundialmente e corrija as permissões, se necessário.

**Conclusão:**

Compreender e gerenciar permissões de arquivos e diretórios é fundamental para a segurança do Linux. O uso correto do comando `ls` com suas opções permite verificar e monitorar as permissões, garantindo a proteção de dados confidenciais.

# Mudança de Permissões

## Comandos de Permissão no Linux: Gerenciando Acesso com Segurança

**Permissões no Linux:**

- **Tipos de Permissões:**
    - Leitura (r): Ler conteúdo de arquivos/listar diretórios.
    - Gravação (w): Modificar arquivos/criar arquivos em diretórios.
    - Execução (x): Executar arquivos/acessar diretórios.
- **Proprietários:**
    - Usuário (u): Proprietário do arquivo.
    - Grupo (g): Grupo ao qual o usuário pertence.
    - Outros (o): Demais usuários do sistema.
- **Representação:**
    - String de 10 caracteres (ex: drwxrwxrwx).
    - O primeiro caractere indica o tipo (d: diretório, -: arquivo).
    - Os demais caracteres indicam permissões para usuário, grupo e outros (r, w, x ou -).

**Explorando Permissões Existentes:**

- **Comando `ls`:**
    - `ls -a`: Exibe arquivos ocultos.
    - `ls -l`: Exibe permissões detalhadas e outras informações.
    - `ls -la`: Combina as opções -l e -a.

**Mudando Permissões com `chmod`:**

- **Princípio do Privilégio Mínimo:** Conceder apenas o acesso necessário.
- **`chmod`**: Altera permissões de arquivos e diretórios.
- **Sintaxe:** `chmod [proprietário][operador][permissão] arquivo/diretório`.
    - **Proprietário:** u, g, o, a (todos).
    - **Operador:** + (adicionar), - (remover), = (definir).
    - **Permissão:** r, w, x.
- **Exemplos:**
    - `chmod u+rwx,g+rwx,o+rwx arquivo`: Adiciona todas as permissões.
    - `chmod u-rwx,g-rwx,o-rwx arquivo`: Remove todas as permissões.
    - `chmod u=r,g=r,o=r arquivo`: Define permissões de leitura.

**Princípio do Privilégio Mínimo em Ação:**

- Um arquivo `bonuses.txt` em um diretório de compensação.
- O usuário `hrrep1` (RH) precisa de acesso.
- Permissões atuais: `-rw-rw----`.
- Ação: `chmod g-rw bonuses.txt` (remove permissões de grupo).

**Postos-chaves:**

- Gerenciar permissões é crucial para a segurança.
- `ls` e `chmod` são ferramentas essenciais.
- O princípio do privilégio mínimo deve ser seguido.


Próximo Modulo [[Adicionar e excluir usuários]]
