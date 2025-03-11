## Gerenciamento de Usuários e Permissões no Linux: Um Guia Completo para Segurança

**1. Autenticação e Gerenciamento de Usuários:**

- **Autenticação**: Processo de verificar a identidade de um usuário.
- **Importância**: Controlar o acesso ao sistema, garantindo que apenas usuários autorizados tenham permissão para entrar.
- **Tarefas**: Adicionar novos usuários, excluir usuários que saíram da organização e gerenciar grupos de usuários.

**2. Usuário Root (Superusuário):**

- **Privilégios Elevados**: Pode modificar qualquer arquivo, executar qualquer programa e criar/excluir usuários.
- **Riscos de Segurança**:
    - Alvo de ataques maliciosos.
    - Facilidade de cometer erros irreversíveis.
    - Dificuldade de rastrear ações individuais.
- **Prática Ruim**: Executar comandos diretamente como root.

**3. Comando Sudo:**

- **Superuser Do**: Permite executar comandos com privilégios elevados temporariamente.
- **Vantagens**:
    - Controle de acesso mais granular.
    - Rastreamento de ações individuais.
    - Redução do risco de erros irreversíveis.
- **Arquivo Sudoers**: Define quais usuários podem usar o sudo.
- **Solicitação de Senha**: Requer a senha do usuário que executa o sudo.
- **Uso Consciente**:
    - Conceder acesso sudo apenas a quem realmente precisa.
    - Usar sudo apenas para os comandos necessários.
    - Cuidado ao copiar comandos da internet com sudo.

**4. Comandos para Gerenciamento de Usuários com Sudo:**

- **`useradd`**: Adiciona um novo usuário ao sistema.
    - `sudo useradd fgarcia`
    - Opções:
        - `-g`: Define o grupo primário.
        - `-G`: Adiciona a grupos secundários.
        - Exemplos:
            - `sudo useradd -g security fgarcia`
            - `sudo useradd -G finance,admin fgarcia`
- **`usermod`**: Modifica contas de usuário existentes.
    - Opções:
        - `-g`: Altera o grupo primário.
        - `-G`: Adiciona/substitui grupos secundários.
        - `-a`: Anexa a grupos secundários (usado com -G).
        - `-d`: Altera o diretório inicial.
        - `-l`: Altera o nome de login.
        - `-L`: Bloqueia a conta.
        - Exemplos:
            - `sudo usermod -g executive fgarcia`
            - `sudo usermod -a -G marketing fgarcia`
            - `sudo usermod -d /home/garcia_f fgarcia`
- **`userdel`**: Exclui um usuário.
    - `sudo userdel fgarcia`
    - Opção:
        - `-r`: Remove o diretório inicial do usuário.
    - Alternativa: `usermod -L` para desativar a conta.
- **`chown`**: Altera a propriedade de arquivos/diretórios.
    - `sudo chown fgarcia access.txt` (altera o proprietário do usuário)
    - `sudo chown :security access.txt` (altera o proprietário do grupo)

**5. Permissões no Linux:**

- **Tipos de Permissões**:
    - Leitura (r): Ler conteúdo de arquivos/listar diretórios.
    - Gravação (w): Modificar arquivos/criar arquivos em diretórios.
    - Execução (x): Executar arquivos/acessar diretórios.
- **Proprietários**:
    - Usuário (u): Proprietário do arquivo.
    - Grupo (g): Grupo ao qual o usuário pertence.
    - Outros (o): Demais usuários do sistema.
- **Representação**:
    - String de 10 caracteres (ex: drwxrwxrwx).
    - O primeiro caractere indica o tipo (d: diretório, -: arquivo).
    - Os demais caracteres indicam permissões para usuário, grupo e outros (r, w, x ou -).

**6. Explorando Permissões Existentes:**

- **Comando `ls`**:
    - `ls -a`: Exibe arquivos ocultos.
    - `ls -l`: Exibe permissões detalhadas e outras informações.
    - `ls -la`: Combina as opções -l e -a.

**7. Mudando Permissões com `chmod`:**

- **Princípio do Privilégio Mínimo**: Conceder apenas o acesso necessário.
- **`chmod`**: Altera permissões de arquivos e diretórios.
- **Sintaxe**: `chmod [proprietário][operador][permissão] arquivo/diretório`.
    - **Proprietário**: u, g, o, a (todos).
    - **Operador**: + (adicionar), - (remover), = (definir).
    - **Permissão**: r, w, x.
- **Exemplos**:
    - `chmod u+rwx,g+rwx,o+rwx arquivo`: Adiciona todas as permissões.
    - `chmod u-rwx,g-rwx,o-rwx arquivo`: Remove todas as permissões.
    - `chmod u=r,g=r,o=r arquivo`: Define permissões de leitura.
- **Princípio do Privilégio Mínimo em Ação**:
    - Um arquivo `bonuses.txt` em um diretório de compensação.
    - O usuário `hrrep1` (RH) precisa de acesso.
    - Permissões atuais: `-rw-rw----`.
    - Ação: `chmod g-rw bonuses.txt` (remove permissões de grupo).

**8. Conclusão:**

- O sudo é uma ferramenta poderosa, mas exige responsabilidade.
- Os comandos `useradd`, `usermod`, `userdel` e `chown` são essenciais para gerenciar usuários e permissões.
- O princípio do privilégio mínimo deve ser sempre aplicado, tanto no gerenciamento de usuários quanto no de permissões.
- O uso correto do comando `ls` com suas opções permite verificar e monitorar as permissões, garantindo a proteção de dados confidenciais e a integridade do sistema.


Próximo Modulo [[Recursos do Linux]]