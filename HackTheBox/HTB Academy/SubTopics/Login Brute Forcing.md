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
