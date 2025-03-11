**Gerenciadores de Pacotes no Linux: A Chave para Instalar Aplicativos**

**O que são Pacotes?**

- Pacotes são como "caixas" de software que contêm tudo o que é necessário para instalar um programa.
    - **Exemplo:** Imagine que você quer instalar o programa "LibreOffice" (um pacote de aplicativos de escritório). O pacote "LibreOffice" incluirá o programa em si, além de outros arquivos necessários para que ele funcione corretamente, como bibliotecas de fontes e arquivos de configuração.

**Gerenciadores de Pacotes:**

- São ferramentas que automatizam a instalação, atualização e remoção de pacotes.
    - **Exemplo:** Em vez de procurar e baixar manualmente todos os arquivos necessários para o "LibreOffice", você pode usar um gerenciador de pacotes para fazer isso com um único comando. O gerenciador de pacotes também se certificará de que todas as dependências (outros pacotes necessários) sejam instaladas.

**Tipos de Gerenciadores:**

- A escolha do gerenciador depende da distribuição Linux que você está usando.
    - **Distribuições Debian (como Ubuntu e Kali Linux):**
        - Utilizam o "dpkg" (um gerenciador de pacotes de baixo nível).
        - Usam arquivos com a extensão ".deb".
            - **Exemplo:** Um arquivo de pacote do LibreOffice para Ubuntu poderia se chamar "libreoffice_7.3.2-0ubuntu3_amd64.deb".
        - Utilizam o "APT" (Advanced Package Tool) para gerenciar os pacotes de forma mais automatizada.
            - **Exemplo:** Para instalar o LibreOffice no Ubuntu, você pode usar o comando "sudo apt install libreoffice" no terminal.
    - **Distribuições Red Hat (como Fedora e CentOS):**
        - Utilizam o "RPM" (Red Hat Package Manager).
        - Usam arquivos com a extensão ".rpm".
            - **Exemplo:** Um arquivo de pacote do LibreOffice para Fedora poderia se chamar "libreoffice-7.3.2-1.fc36.x86_64.rpm".
        - Utilizam o "YUM" (Yellowdog Updater Modified) ou o "DNF" (Dandified Yum) para gerenciar os pacotes de forma mais automatizada.
            - **Exemplo:** Para instalar o LibreOffice no Fedora, você pode usar o comando "sudo dnf install libreoffice" no terminal.

**Ferramentas de Gerenciamento:**

- "APT" e "YUM/DNF" são ferramentas que facilitam o uso dos gerenciadores de pacotes via linha de comando.
    - **Exemplo:** Além de instalar programas, você pode usar o "APT" para atualizar todos os pacotes instalados no seu sistema com o comando "sudo apt upgrade".

**Pontos-chave:**

- Gerenciadores de pacotes simplificam a instalação e o gerenciamento de software no Linux.
- A escolha do gerenciador e das ferramentas depende da distribuição Linux.
- É essencial que o profissional de segurança cibernética, tenha conhecimento sobre os gerenciadores de pacote, pois durante suas atividades, ele ira necessitar instalar e remover programas.

Próximo Modulo [[Introdução ao shell]]
