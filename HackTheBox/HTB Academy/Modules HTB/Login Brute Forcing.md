# Fundamentos de Segurança de senha

A eficácia dos ataques de força bruta depende da força das senhas que ele visa. Compreender os fundamentos da segurança de senhas é crucial para apreciar a importância de práticas robustas de senhas e os desafios impostos por ataques de força bruta.

**Importância das Senhas Fortes**  
Senhas são a primeira defesa contra acessos não autorizados. Senhas longas e complexas dificultam ataques de força bruta, pois aumentam exponencialmente o número de combinações possíveis.

**Características de uma Senha Forte**

1. **Comprimento**: Mínimo de 12 caracteres. Cada caractere adicional dificulta a quebra.
2. **Complexidade**: Inclua maiúsculas, minúsculas, números e símbolos.
3. **Unicidade**: Evite reutilizar senhas em diferentes contas.
4. **Aleatoriedade**: Não use palavras do dicionário, informações pessoais ou padrões previsíveis.

**Pontos Fracos Comuns**

- Senhas curtas ou baseadas em palavras comuns.
- Uso de informações pessoais.
- Reutilização de senhas.
- Padrões previsíveis como "123456" ou "qwerty".

**Políticas de Senhas**  
Organizações podem exigir comprimento mínimo, complexidade, troca periódica e histórico de senhas para reforçar a segurança. No entanto, políticas rigorosas podem levar a práticas inseguras, como anotar senhas.

**Riscos das Senhas Padrão**  
Senhas predefinidas, como "admin" ou "1234", são vulneráveis e frequentemente usadas por atacantes. Alterar essas senhas e nomes de usuário padrão é essencial para reduzir riscos.

**Força Bruta e Segurança**  
Senhas fracas facilitam ataques, enquanto senhas fortes exigem mais tempo e recursos. Para pentesters, entender a postura de segurança de senhas ajuda a identificar vulnerabilidades, selecionar ferramentas e planejar estratégias eficazes.

**Conclusão**  
Práticas robustas de senha são essenciais para proteger sistemas contra ataques de força bruta e outros métodos de invasão.

---

# Ataques de Força Bruta
### **O que é um ataque de força bruta?**

Um método em que o invasor tenta todas as combinações possíveis de caracteres até descobrir a senha correta.
### **Fórmula para calcular combinações possíveis:**

**Combinações possíveis = Tamanho do conjunto de caracteres ^ Comprimento da senha**

Exemplos:

1. **Senha de 6 caracteres (a-z):**
    - Conjunto: 26 letras minúsculas.
    - Combinações: 266≈309 milho˜es26^6 \approx 309 \text{ milhões}266≈309 milho˜es.
2. **Senha de 8 caracteres (a-z):**
    - Combinações: 268≈209 bilho˜es26^8 \approx 209 \text{ bilhões}268≈209 bilho˜es.
3. **Senha de 8 caracteres (a-z, A-Z):**
    - Conjunto: 52 caracteres (maiúsculas + minúsculas).
    - Combinações: 528≈53 trilho˜es52^8 \approx 53 \text{ trilhões}528≈53 trilho˜es.
4. **Senha de 12 caracteres (todos os caracteres ASCII):**
    - Conjunto: 94 caracteres.
    - Combinações: 9412≈475 quintilho˜es94^{12} \approx 475 \text{ quintilhões}9412≈475 quintilho˜es.

---

### **Fatores que influenciam o tempo para quebrar uma senha:**

1. **Complexidade da senha:**
    - Comprimento maior e inclusão de diferentes tipos de caracteres (letras maiúsculas, minúsculas, números e símbolos) aumentam exponencialmente o número de combinações.
2. **Poder computacional disponível:**
    - **Computador básico:** 1 milhão de tentativas/segundo.
    - **Supercomputador:** 1 trilhão de tentativas/segundo.

---

### **Exemplos práticos de tempo para quebra:**

|**Senha**|**Conjunto de caracteres**|**Combinações**|**Tempo de quebra (básico)**|**Tempo de quebra (supercomputador)**|
|---|---|---|---|---|
|6 caracteres (a-z)|Letras minúsculas|26626^6266 = 309 milhões|~5 minutos|~0,3 segundos|
|8 caracteres (a-z)|Letras minúsculas|26826^8268 = 209 bilhões|~6,9 anos|~3,5 minutos|
|8 caracteres (a-z, A-Z)|Letras maiúsculas e minúsculas|52852^8528 = 53 trilhões|~1.692 anos|~18 horas|
|12 caracteres (ASCII)|Letras, números, símbolos (94 total)|941294^{12}9412 = 475 quintilhões|~15 milhões de anos|~15 mil anos|

---

### **Dicas para criar senhas seguras:**

1. **Use comprimento maior:** Recomenda-se ao menos 12 caracteres.
2. **Varie o conjunto de caracteres:** Inclua letras maiúsculas, minúsculas, números e símbolos.
3. **Evite palavras ou padrões comuns:** Frases completas ou combinações aleatórias são melhores.
4. **Use gerenciadores de senhas:** Para criar e armazenar senhas complexas com segurança.

---

# Ataque de Dicionário

### **Ataques de Dicionário: Entendendo o Funcionamento**

#### **1. O Conceito:**

- Um **ataque de dicionário** baseia-se em explorar listas predefinidas de palavras, frases ou padrões que as pessoas costumam usar como senhas.
- Em vez de testar todas as combinações possíveis (como na força bruta), o ataque de dicionário é mais rápido porque usa entradas mais prováveis.

---

### **2. Por que os Ataques de Dicionário Funcionam?**

- **Previsibilidade Humana:** As pessoas tendem a usar senhas fáceis de lembrar, como:
    - Palavras comuns (ex.: "banana", "secret").
    - Padrões simples (ex.: "123456", "qwerty").
    - Frases populares ou contextuais (ex.: "iloveyou", "admin2023").
- **Listas Pré-compiladas:** Essas listas podem incluir:
    - Senhas populares (ex.: vazamentos de dados anteriores).
    - Palavras relacionadas ao contexto do alvo (ex.: nomes de empresas, jargões).

---

### **3. Diferença entre Força Bruta e Ataque de Dicionário:**

|**Característica**|**Ataque de Dicionário**|**Ataque de Força Bruta**|
|---|---|---|
|**Eficiência**|Mais rápido e com menos uso de recursos.|Muito mais lento e consome mais poder computacional.|
|**Foco**|Personalizável para alvos específicos.|Não é focado – tenta todas as combinações possíveis.|
|**Eficácia**|Altamente eficaz contra senhas previsíveis.|Universal, mas impraticável para senhas longas.|
|**Limitações**|Não funciona contra senhas complexas ou aleatórias.|Extremamente difícil para senhas longas/complexas.|

---

### **4. Como Construir um Ataque de Dicionário?**

#### **Passo 1: Criar ou Obter um Dicionário**

- Fontes de dicionário:
    - Arquivos de texto como o **rockyou.txt** (banco de senhas vazadas).
    - Listas específicas para o alvo (nomes, contextos, etc.).
- Ferramentas como **CeWL** podem criar dicionários personalizados com base no site do alvo.

#### **Passo 2: Usar uma Ferramenta de Ataque**

- Ferramentas como **Hydra**, **John the Ripper** ou **Hashcat** testam palavras do dicionário contra o sistema-alvo.
- Exemplo com Hydra:
    
    `hydra -l usuario -P /caminho/para/dicionario.txt <host> http-post-form "/login:username=^USER^&password=^PASS^:F=Login failed"`
    

---

### **5. Exemplo de Aplicação:**

#### Cenário:

Um invasor quer acessar o sistema de login de uma empresa chamada "TechCorp".

#### Como o invasor cria o ataque:

1. **Montando o dicionário:**
    - Adiciona palavras como:
        - "TechCorp2023".
        - "admin", "manager", "Tech123".
    - Combina com palavras comuns (ex.: "password1").
2. **Executando o ataque:**
    - Usa o dicionário em uma ferramenta para testar senhas no portal.

---

### **6. Como Prevenir Ataques de Dicionário?**

1. **Senhas Fortes:**
    - Comprimento mínimo de 12 caracteres.
    - Mistura de letras maiúsculas, minúsculas, números e símbolos.
    - Evitar palavras ou padrões comuns.
2. **Mecanismos de Defesa:**
    - Implementar **bloqueio de conta** após tentativas falhas.
    - Usar **CAPTCHA** para limitar ataques automatizados.
    - Adotar **autenticação multifator (MFA)**.
3. **Monitoramento:**
    - Usar ferramentas para identificar tentativas suspeitas de login.
    - Manter sistemas atualizados contra falhas de segurança.

---
# Ataque Hibridos

#### **Tópico Principal**: Ataques Híbridos

- **Definição**: Combinação de técnicas de **ataque de dicionário** e **força bruta** para explorar padrões previsíveis de senhas, especialmente em cenários onde os usuários são obrigados a alterar senhas periodicamente.
### **Resumo**:

- Muitas organizações exigem que os usuários alterem senhas regularmente para aumentar a segurança.
    
- No entanto, os usuários tendem a criar padrões previsíveis ao modificar senhas (ex.: adicionar números ou caracteres especiais ao final).
    
- Ataques híbridos exploram essa previsibilidade, combinando listas de palavras comuns (dicionário) e variações incrementais (força bruta).
    

#### **Pontos-Chave**:

1. **Padrões Previsíveis**: Usuários frequentemente alteram senhas de forma incremental (ex.: "Senha2023" → "Senha2024").
    
2. **Técnicas Combinadas**:
    
    - **Ataque de Dicionário**: Usa listas de senhas comuns.
        
    - **Força Bruta Direcionada**: Modifica as senhas do dicionário com variações previsíveis.
        
3. **Eficiência**: Reduz o espaço de pesquisa, aumentando as chances de sucesso.
    

#### **Exemplos**:

- Senha original: "Summer2023".
    
- Variações previsíveis: "Summer2023!", "Summer2024", "Summer2024!".
    
- Um ataque híbrido testaria essas variações rapidamente.
    

#### **Ferramentas e Comandos**:

- **Filtragem de Senhas com `grep`**:
    
    - Filtrar senhas que atendem a políticas específicas (ex.: mínimo de 8 caracteres, letras maiúsculas/minúsculas, números).
        
    - Exemplo de comandos:
        
        bash
        
        Copy
        
        grep -E '^.{8,}$' lista_senhas.txt > senhas_filtradas.txt
        grep -E '[A-Z]' senhas_filtradas.txt > senhas_maiusculas.txt
        grep -E '[a-z]' senhas_maiusculas.txt > senhas_minusculas.txt
        grep -E '[0-9]' senhas_minusculas.txt > senhas_finais.txt
        
    - Resultado: Lista reduzida de senhas prováveis.
        

#### **Links Relacionados**:

- **Ataques de Dicionário**: Técnica que usa listas de senhas comuns.
    
- **Força Bruta**: Técnica que testa todas as combinações possíveis.
    
- **Políticas de Senha**: Boas práticas para criação de senhas seguras.
    

---

### **Preenchimento de Credenciais**

#### **Tópico Principal**: Preenchimento de Credenciais (Credential Stuffing)

- **Definição**: Ataque que explora a reutilização de senhas em múltiplas contas, usando credenciais vazadas para obter acesso não autorizado.
#### **Resumo**:

- Muitos usuários reutilizam senhas em diferentes serviços.
    
- Invasores usam listas de credenciais vazadas (de violações de dados ou phishing) para testar em outros serviços.
    
- O ataque é automatizado, testando rapidamente várias combinações de usuário/senha.

#### **Pontos-Chave**:

1. **Reutilização de Senhas**: Principal vulnerabilidade explorada.
    
2. **Fontes de Credenciais**:
    
    - Violações de dados.
        
    - Listas públicas (ex.: rockyou.txt, darkweb2017-top10000.txt).
        
3. **Alvos Comuns**: Redes sociais, e-mails, bancos online, e-commerce.
    
4. **Automatização**: Ferramentas e scripts testam credenciais em massa.
#### **Exemplos**:

- Um invasor obtém a lista de credenciais "usuario:senha " de um vazamento.
    
- Testa essas credenciais em serviços como Gmail, Facebook e PayPal.
    
- Se o usuário reutilizou a senha, o invasor ganha acesso.
#### **Impacto**:

- Roubo de dados pessoais.
    
- Fraude financeira.
    
- Acesso a sistemas conectados.
#### **Prevenção**:

- **Senhas Únicas**: Usar senhas diferentes para cada serviço.
    
- **Autenticação Multifator (MFA)**: Adicionar uma camada extra de segurança.
    
- **Monitoramento de Vazamentos**: Verificar se suas credenciais foram expostas em violações.
#### **Links Relacionados**:

- **Phishing**: Técnica comum para obter credenciais.
    
- **Violações de Dados**: Fonte de credenciais vazadas.
    
- **Autenticação Multifator**: Método para mitigar riscos.
---
### **Conclusão**

- **Ataques Híbridos**: Exploram padrões previsíveis de senhas, combinando técnicas de dicionário e força bruta.
    
- **Preenchimento de Credenciais**: Explora a reutilização de senhas, usando credenciais vazadas para acessar múltiplas contas.
    
- **Boas Práticas**:
    
    - Evitar padrões previsíveis ao criar senhas.
        
    - Nunca reutilizar senhas.
        
    - Implementar autenticação multifator.
---
# HYDRA

### **O que é o Hydra?**

O **Hydra** é uma ferramenta de força bruta altamente eficiente e flexível, usada para testar a segurança de sistemas de autenticação. Ele suporta uma ampla variedade de protocolos, como HTTP, FTP, RDP, SSH, SMTP, e muitos outros. O Hydra é amplamente utilizado por profissionais de segurança para testar a resistência de senhas e identificar vulnerabilidades em sistemas.

Mais Sobre em [[Hydra]]

---

### **Principais Funcionalidades**:

1. **Ataques de Força Bruta**:
    
    - Testa combinações de usuário/senha em massa contra serviços de autenticação.
        
    - Pode usar listas de senhas pré-definidas ou gerar senhas automaticamente.
        
2. **Suporte a Múltiplos Protocolos**:
    
    - Funciona com mais de 50 protocolos, incluindo:
        
        - **HTTP/HTTPS**: Para formulários de login em websites.
            
        - **FTP**: Para servidores de arquivos.
            
        - **SSH**: Para acesso remoto a servidores.
            
        - **RDP**: Para conexões de área de trabalho remota no Windows.
            
        - **SMTP/POP3/IMAP**: Para servidores de e-mail.
            
        - **SMB**: Para compartilhamento de arquivos em redes Windows.
            
3. **Personalização de Ataques**:
    
    - Permite definir regras para gerar senhas (ex.: comprimento, caracteres permitidos).
        
    - Pode testar múltiplos usuários e senhas simultaneamente.
        
4. **Alta Velocidade**:
    
    - Utiliza múltiplas threads para realizar testes em paralelo, aumentando a velocidade do ataque.
        
5. **Integração com Outras Ferramentas**:
    
    - Pode ser combinado com ferramentas como **Burp Suite**, **Nmap**, e **Metasploit** para testes de penetração mais avançados.
        

---

# Login Forms
#### **1. Introdução aos Login Forms**

- **O que são?**  
    Formulários de login são mecanismos comuns de autenticação em aplicações web. Eles permitem que os usuários insiram credenciais (nome de usuário e senha) para acessar sistemas.
    
- **Estrutura básica:**  
    Um formulário de login típico consiste em:
    
    - Campos de entrada (`<input>`) para nome de usuário e senha.
        
    - Um botão de envio (`<button>` ou `<input type="submit">`).
        
    - Uma ação (`action`) que define para onde os dados são enviados (geralmente via método `POST`).
        
- **Exemplo de HTML:**
    
    <form action="/login" method="post">
      <label for="username">Username:</label>
      <input type="text" id="username" name="username"><br><br>
      <label for="password">Password:</label>
      <input type="password" id="password" name="password"><br><br>
      <input type="submit" value="Submit">
    </form>
    
    
- **Funcionamento:**  
    Quando o formulário é enviado, o navegador cria uma requisição HTTP `POST` com os dados do formulário no corpo da mensagem, codificados como `application/x-www-form-urlencoded` ou `multipart/form-data`.
    

---

#### **2. Como o Hydra Funciona com Login Forms**

- **O que é o Hydra?**  
    O Hydra é uma ferramenta de força bruta que automatiza tentativas de login em formulários web, testando combinações de nomes de usuário e senhas.
    
- **Módulo `http-post-form`:**  
    Especificamente projetado para atacar formulários de login que usam o método `POST`.
    
- **Estrutura do Comando do Hydra:**
    
    hydra [options] target http-post-form "path:params:condition_string"
    
    - **`path`:** Caminho do endpoint de login (ex: `/login`).
        
    - **`params`:** Parâmetros do formulário (ex: `user=^USER^&pass=^PASS^`).
        
    - **`condition_string`:** Condições para identificar sucesso (ex: `S=302`) ou falha (ex: `F=Invalid credentials`).
        

---

#### **3. Condições de Sucesso e Falha**

- **Condição de Falha (`F=`):**  
    Usada para identificar tentativas de login inválidas. Por exemplo, se o servidor retorna "Invalid credentials" após uma falha:
    
    hydra ... http-post-form "/login:user=^USER^&pass=^PASS^:F=Invalid credentials"
    
- **Condição de Sucesso (`S=`):**  
    Usada para identificar tentativas de login válidas. Por exemplo, se o servidor redireciona com código `302` ou exibe "Dashboard":
    
    hydra ... http-post-form "/login:user=^USER^&pass=^PASS^:S=302"
    
    ou
    
    hydra ... http-post-form "/login:user=^USER^&pass=^PASS^:S=Dashboard"
    

---

#### **4. Coleta de Informações para o Ataque**

Antes de usar o Hydra, é essencial analisar o formulário de login para obter:

- **Método HTTP:** Geralmente `POST`.
    
- **Campos do formulário:** Nomes dos campos de usuário e senha (ex: `username` e `password`).
    
- **Respostas do servidor:** Mensagens de erro ou redirecionamentos.
    
- **Ferramentas para Análise:**
    
    1. **Ferramentas de Desenvolvedor do Navegador:**  
        Inspecione o código HTML do formulário e monitore as requisições na aba "Network".
        
    2. **Proxies como Burp Suite ou OWASP ZAP:**  
        Interceptam o tráfego entre o navegador e o servidor, permitindo analisar requisições e respostas em detalhes.
        

---

#### **5. Construindo o Ataque com Hydra**

- **Passo a Passo:**
    
    1. Identifique o caminho do endpoint de login (ex: `/login`).
        
    2. Determine os parâmetros do formulário (ex: `username` e `password`).
        
    3. Defina as condições de sucesso ou falha com base nas respostas do servidor.
        
    4. Use listas de palavras (wordlists) para nomes de usuário e senhas.
        
- **Exemplo Prático:**  
    Suponha que:
    
    - O endpoint de login é `/login`.
        
    - Os campos são `username` e `password`.
        
    - A mensagem de erro é "Invalid credentials".
        
    
    O comando do Hydra seria:
    
    hydra -L userlist.txt -P passlist.txt 192.168.1.1 http-post-form "/login:username=^USER^&password=^PASS^:F=Invalid credentials"
    

---

#### **6. Boas Práticas e Considerações**

- **Testes Responsáveis:**  
    Sempre obtenha permissão antes de realizar testes de força bruta em sistemas.
    
- **Otimização:**  
    Use listas de palavras eficientes e ajuste as opções do Hydra (ex: número de threads) para melhorar o desempenho.
    
- **Proteção Contra Ataques:**  
    Implemente medidas como CAPTCHA, bloqueio de IP após várias tentativas falhas e uso de tokens CSRF para proteger formulários de login.
    

---

### **Pontos Chave:**

1. **Login Forms** são alvos comuns para ataques de força bruta devido à sua simplicidade e uso generalizado.
    
2. O **Hydra** é uma ferramenta poderosa para automatizar tentativas de login, mas requer configuração cuidadosa.
    
3. **Condições de sucesso e falha** são essenciais para o Hydra identificar credenciais válidas.
    
4. **Análise prévia** do formulário (via inspeção HTML ou proxies) é crucial para configurar o ataque corretamente.
    
5. **Boas práticas** garantem que os testes sejam éticos e eficientes.
---
# Medusa
### **O que é Medusa (Brute-Force)?**

Medusa é uma ferramenta de **força bruta** de alto desempenho usada para testar a segurança de sistemas de autenticação. Ela suporta uma variedade de protocolos, como SSH, FTP, HTTP, MySQL, RDP, entre outros. É uma alternativa ao Hydra, mas com algumas diferenças em termos de desempenho e funcionalidades.

Mais Sobre em [[Medusa]]

---

### **1. Introdução: Segurança em Web Services**

SSH e FTP são protocolos amplamente usados para acessar remotamente servidores e transferir arquivos. No entanto, autenticações baseadas apenas em senhas são vulneráveis a ataques de força bruta. O **Medusa** é uma ferramenta que permite automatizar tentativas de login para descobrir credenciais fracas.

---

### **2. Compreendendo os Protocolos**

- **[[SSH]] (Secure Shell)**: Protocolo seguro para acesso remoto e transferência de arquivos, protegendo dados com criptografia. Porém, senhas fracas ainda representam um risco.
- **[[FTP]] (File Transfer Protocol)**: Usado para transferir arquivos entre cliente e servidor, mas pode transmitir credenciais em **texto claro**, tornando-se um alvo fácil para interceptação e ataques de força bruta.

---

### **3. Ataque a um Servidor SSH com Medusa**

#### **Comando de ataque:**

`medusa -h <IP> -n <PORT> -u sshuser -P 2023-200_most_used_passwords.txt -M ssh -t 3`

#### **Explicação dos parâmetros:**

- `-h <IP>` → IP do alvo.
- `-n <PORT>` → Porta do SSH (padrão 22).
- `-u sshuser` → Nome do usuário-alvo.
- `-P 2023-200_most_used_passwords.txt` → Lista de senhas comuns em 2023.
- `-M ssh` → Módulo SSH do Medusa.
- `-t 3` → Três tentativas simultâneas (maior velocidade, mas pode ativar medidas de segurança).

Se o ataque for bem-sucedido, o Medusa exibirá a senha correta, permitindo que o atacante faça login via SSH:

`ssh sshuser@<IP> -p PORT`

---

### **4. Expansão do Ataque: Explorando Serviços Abertos**

Após obter acesso ao SSH, o atacante pode verificar portas abertas no sistema:

`netstat -tulpn | grep LISTEN`

Se identificar um **FTP ativo na porta 21**, pode usar o **Nmap** para confirmar:

`nmap localhost`

Se o FTP estiver disponível, o próximo passo é atacar esse serviço.

---

### **5. Ataque ao Servidor FTP**

Se houver um diretório `/home/ftpuser`, é provável que "ftpuser" seja um usuário válido. O ataque pode ser adaptado:

`medusa -h 127.0.0.1 -u ftpuser -P 2020-200_most_used_passwords.txt -M ftp -t 5`

#### **Principais mudanças:**

- `-h 127.0.0.1` → O alvo é o próprio sistema local.
- `-u ftpuser` → Usuário-alvo do FTP.
- `-M ftp` → Módulo FTP do Medusa.
- `-t 5` → Cinco tentativas simultâneas para maior eficiência.

Se bem-sucedido, o atacante terá acesso ao FTP e poderá extrair arquivos ou enviar malwares.

---

### **6. Conclusão e Defesa**

Este cenário ilustra como credenciais fracas podem ser exploradas. Para se proteger:

- Utilize **senhas fortes** e autenticação de dois fatores (2FA).
- Restrinja **tentativas de login** e utilize **firewalls**.
- Substitua o **FTP tradicional por SFTP** (FTP sobre SSH) para criptografar credenciais.

Esse módulo destaca a necessidade de segurança reforçada em serviços web, protegendo sistemas contra ataques automatizados.

---
# Custom Word lists
#### **Wordlists Personalizadas (Custom Wordlists)**

- Listas padrão como **rockyou** e **SecLists** são amplas, mas podem ser **ineficientes** para alvos específicos.
- Para aumentar a eficiência, é melhor **criar wordlists personalizadas** com base no contexto do alvo.
- Exemplo: Se o alvo é "Thomas Edison", uma wordlist genérica pode não conter o nome correto. Criar uma lista baseada nas convenções da empresa aumenta as chances de sucesso.

#### **Username Anarchy (Geração de Nomes de Usuário)**

- **Usernames são imprevisíveis** e podem conter variações como:
    - Nome + Sobrenome (janesmith, smithjane, jane.smith)
    - Abreviações e iniciais (js, j.s., s.j.)
    - Leetspeak (j4n3, 5m1th)
    - Elementos pessoais (hobbies, ano de nascimento, apelidos)
- Ferramenta **Username Anarchy** automatiza a criação de nomes de usuário possíveis.
- **Instalação e uso:**
    
    bash
    
    CopyEdit
    
    `sudo apt install ruby -y git clone https://github.com/urbanadventurer/username-anarchy.git cd username-anarchy ./username-anarchy Jane Smith > jane_smith_usernames.txt`
    
- Saída: Uma lista extensa de usernames combinando padrões comuns e personalizações.

#### **CUPP (Common User Passwords Profiler)**

- Foca na criação de **wordlists de senhas personalizadas** baseadas em informações do alvo.
- Usa **OSINT** (redes sociais, registros públicos, blogs) para coletar dados.
- **Exemplo de perfil de alvo:**
    - Nome: Jane Smith
    - Apelido: Janey
    - Data de nascimento: 11/12/1990
    - Namorado: Jim (apelido: Jimbo)
    - Pet: Spot
    - Empresa: AHI
    - Interesses: Hacking, pizza, golfe
- **Saída do CUPP:**
    - jane, Jane, j4n3
    - jane1990, janey1990, smith1990
    - jane!, janesmith123, janesmith!
    - smith2708, janesmith@2024
    - j4n3_1990, 5m1th!

#### **Conclusão**

- Criar **wordlists personalizadas** com Username Anarchy e CUPP aumenta a eficiência dos ataques de força bruta.
- **Username Anarchy** gera variações de nomes de usuário.
- **CUPP** gera listas de senhas altamente relevantes com base no perfil do alvo.
- Combinar essas técnicas **economiza tempo e aumenta as chances de sucesso** em ataques de senha.
---
# Skills Assessment I and II

Aqui foi pedido para confirmar seu aprendizado, apos fornecer uma lista de senha e usuários,  foi feito um ataque com hydra na paginá web com o seguinte comando 
```
hydra -L top-usernames-shortlist.txt -P 2023-200_most_used_passwords.txt <IP> http-get / -s <Port>

```
me fornecendo as credenciais após o acesso a pagina, foi me entregue um usuário chamado <satwossh> onde terminamos a parte 1.

Na parte 2, precisamos descobri a senha do usuário encontrado no ultimo (satwossh) para conexão ssh, então rodamos o comando.

	hydra -l satwossh -P <wordlist.txt> ssh://<IP> -s <PORT>

A senha encontrada foi password1, após a conexão via ssh com o user e pass, podemos utilizar 

	ssh satwossh@<IP> -p <PORT>

caso o serviço esteja rodando na porta padrão não e necessário especificar a porta, porém não e o caso nessa aula.

Após se conectar podemos ver um arquivo txt de reporte de incidente onde diz que o usuário thomas smith teve um comportamento suspeito em uma atividade FTP, com esse nome podemos usar a ferramenta "Anarchy" para gerar nomes de usuario para tentar quebrar a senha utilizando

	./username-anarchy thomas smith > nomes.txt

gerando um arquivos com variações dos nomes, vamos procurar por sua senha no servidor FTP, utilizando o hydra para descobrir sua senha e estando na mesma rede que o usuário, colocamos.

	hydra -L nomes.txt -P passwords.txt ftp://localhost

Descobrindo que a senha do usuario e "chocolate!", podemos acessar seu servidor FTP com 

	ftp localhost

Vai pedir o usuário e senha, após inserir ambos temos acesso e podemos pegar a flag para a resposta do exercício.


