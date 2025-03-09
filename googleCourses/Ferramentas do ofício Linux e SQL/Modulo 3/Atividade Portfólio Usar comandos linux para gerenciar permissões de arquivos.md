# Project Description

Este projeto tem como objetivo aprender sobre alterações e atribuições de permissões de arquivos no sistema Linux. Devemos garantir que todos os arquivos e diretórios possuam o controle correto, permitindo que apenas pessoas autorizadas possam visualizar, acessar e modificar os arquivos.

Foi utilizado o comando `chmod` com notação numérica, onde os valores representam:
- **4** → Leitura (**r**)
- **2** → Escrita (**w**)
- **1** → Execução (**x**)

Exemplo:
```shell
chmod 754 file  # Dono: rwx(7), Grupo: r-x(5), Outros: r--(4)
```

## Sumário
1. [Verificação de Detalhes de Arquivos e Diretórios](#verificacao-detalhes)
2. [Descrição da String de Permissões](#descricao-permissoes)
3. [Alteração de Permissões de Arquivos](#alteracao-permissoes-arquivos)
4. [Alteração de Permissões de Diretórios](#alteracao-permissoes-diretorios)
5. [Resumo](#resumo)

## <a id="verificacao-detalhes"></a>Verificação de Detalhes de Arquivos e Diretórios

Começamos verificando o diretório atual com o comando `pwd`, que indica que estamos em `/home/researcher2`. Com o comando `ls -la`, identificamos os arquivos de bash (fora do escopo do exercício) e o diretório `projects`. Podemos acessar esse diretório com `cd`. Para facilitar a visualização da hierarquia de arquivos, usamos o comando `tree`, resultando na seguinte estrutura:

```shell
researcher2@c2271b501145:~/projects$ tree .
.
|-- drafts
|-- project_k.txt
|-- project_m.txt
|-- project_r.txt
`-- project_t.txt

1 directory, 4 files
```

## <a id="descricao-permissoes"></a>Descrição da String de Permissões

O comando `ls -la` permite visualizar arquivos ocultos e suas permissões:

```shell
researcher2@c2271b501145:~/projects$ ls -la
total 32
drwxr-xr-x 3 researcher2 research_team 4096 Mar  9 11:24 .
drwxr-xr-x 3 researcher2 research_team 4096 Mar  9 11:49 ..
-rw--w---- 1 researcher2 research_team   46 Mar  9 11:24 .project_x.txt
drwx--x--- 2 researcher2 research_team 4096 Mar  9 11:24 drafts
-rw-rw-rw- 1 researcher2 research_team   46 Mar  9 11:24 project_k.txt
-rw-r----- 1 researcher2 research_team   46 Mar  9 11:24 project_m.txt
-rw-rw-r-- 1 researcher2 research_team   46 Mar  9 11:24 project_r.txt
-rw-rw-r-- 1 researcher2 research_team   46 Mar  9 11:24 project_t.txt
```

Explicação da string de permissões:
1. O primeiro caractere indica o tipo de arquivo (`-` para arquivos normais, `d` para diretórios).
2. Os três caracteres seguintes representam as permissões do usuário (rwx).
3. Os três seguintes indicam as permissões do grupo.
4. Os últimos três definem as permissões para outros usuários do sistema.

## <a id="alteracao-permissoes-arquivos"></a>Alteração de Permissões de Arquivos

O objetivo aqui é corrigir permissões inadequadas para aumentar a segurança:
1. O arquivo `project_k.txt` tem permissão de escrita para outros usuários, o que pode ser perigoso. Vamos remover essa permissão:
   ```shell
   chmod 664 project_k.txt
   ```
2. O arquivo `project_m.txt` é restrito e não deve ser lido ou escrito por grupos ou outros usuários:
   ```shell
   chmod 600 project_m.txt
   ```
3. O arquivo oculto `.project_x.txt` deve permitir apenas leitura para o usuário e grupo:
   ```shell
   chmod 440 .project_x.txt
   ```

## <a id="alteracao-permissoes-diretorios"></a>Alteração de Permissões de Diretórios

Queremos restringir o acesso ao diretório `drafts` para que apenas o usuário tenha permissões totais:

```shell
researcher2@c2271b501145:~/projects$ ls -l
drwx--x--- 2 researcher2 research_team 4096 Mar  9 11:24 drafts

researcher2@c2271b501145:~/projects$ chmod 700 drafts

researcher2@c2271b501145:~/projects$ ls -l
drwx------ 2 researcher2 research_team 4096 Mar  9 11:24 drafts
```

## <a id="resumo"></a>Resumo

Neste projeto, analisamos permissões de arquivos e diretórios utilizando a notação numérica do comando `chmod`. Corrigimos permissões inadequadas para melhorar a segurança do sistema, garantindo que apenas usuários autorizados possam acessar e modificar arquivos específicos.
