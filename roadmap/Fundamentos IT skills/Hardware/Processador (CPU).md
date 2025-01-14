## **1. Composição do Processador**

O processador é um dos componentes mais complexos de um sistema, com várias partes que trabalham juntas para executar as instruções.

### **1.1 Unidades de Execução**

- **ALU (Arithmetic Logic Unit):**
    - Responsável por realizar operações matemáticas (adição, subtração) e lógicas (AND, OR, XOR).
    - Exemplos:
        - Um cálculo como `5 + 3` ou uma comparação entre dois valores (`x > y`) é tratado pela ALU.
- **FPU (Floating Point Unit):**
    - Processa números de ponto flutuante (números com casas decimais).
    - Muito usada em gráficos 3D e cálculos científicos.
    - Exemplo: O cálculo de raízes quadradas ou seno/cosseno em simulações físicas.

---

### **1.2 Cache**

Memória de altíssima velocidade usada para armazenar dados frequentemente acessados.

- **L1 (Level 1):**
    - Cache mais rápido, mas de menor capacidade (geralmente 32-128 KB por núcleo).
- **L2 (Level 2):**
    - Cache intermediário, maior que o L1 (256 KB - 8 MB).
- **L3 (Level 3):**
    - Compartilhado entre os núcleos de um processador, com maior capacidade (até 64 MB).
- **Exemplo de Uso:**
    - Quando um programa precisa acessar repetidamente uma variável, ela pode ser armazenada no cache, reduzindo o tempo de acesso.

---

### **1.3 Controlador de Memória**

- Gerencia a comunicação entre a CPU e a memória RAM.
- Modernos processadores incluem controladores integrados (IMC - Integrated Memory Controller) para maior eficiência.
- Exemplo: Ao abrir um aplicativo, o processador solicita instruções e dados da RAM por meio desse controlador.

---

### **1.4 Registradores**

- São pequenas áreas de armazenamento dentro da CPU que mantêm dados temporários.
- Exemplo: Quando você soma `A + B`, o processador pode armazenar `A`, `B` e o resultado diretamente nos registradores.

---

### **1.5 Clock Interno**

- Define a velocidade com que a CPU executa instruções.
- Medido em GHz (bilhões de ciclos por segundo).
- Exemplo: Uma CPU de 3.5 GHz pode teoricamente processar 3.5 bilhões de ciclos por segundo.

---

### **1.6 Arquitetura Interna**

- **Cores:**
    - Cada núcleo é como um processador independente dentro da CPU, capaz de executar tarefas separadas.
    - Exemplo: Um processador quad-core pode processar quatro tarefas simultaneamente.
- **Threads:**
    - Tecnologias como o Hyper-Threading (Intel) criam "núcleos virtuais", permitindo que cada núcleo físico processe duas tarefas simultaneamente.
- **Pipeline:**
    - Divide as instruções em etapas, como uma linha de produção. Isso aumenta a eficiência.
    - Exemplo: Uma instrução de multiplicação pode ser dividida em etapas: buscar dados, executar operação e armazenar resultado.

---

### **1.7 Tecnologias de Segurança e Virtualização**

- **Virtualização:**
    - Recursos como Intel VT-x ou AMD-V permitem que uma CPU execute múltiplos sistemas operacionais em máquinas virtuais.
- **Trusted Execution Environment (TEE):**
    - Cria áreas seguras para armazenar dados sensíveis, isolando-os de software potencialmente malicioso.
    - Exemplo: Intel SGX (Software Guard Extensions) protege chaves criptográficas e informações sensíveis.

---

## **2. Como Atacar um Processador**

### **2.1 Ataques ao Firmware e Microcódigo**

- **Firmware:** Código que controla as operações básicas do processador.
- **Exploração:** Ataques podem explorar vulnerabilidades em atualizações de microcódigo.
    - Exemplo: Um malware que reescreve o firmware pode instalar rootkits.

---

### **2.2 Execução Especulativa**

- **O que é?**
    - Técnica usada por CPUs para prever quais instruções serão executadas em seguida, aumentando o desempenho.
- **Exploração:**
    - Ataques como **Spectre** e **Meltdown** exploram falhas na execução especulativa para acessar dados sensíveis.
    - Exemplo: Um atacante pode roubar senhas armazenadas na memória do kernel.

---

### **2.3 Ataques de Side-Channel**

Ataques que exploram características físicas do processador:

- **Cache Timing Attacks:** Medem o tempo que a CPU leva para acessar o cache e inferem dados.
- **Consumo de Energia:** Monitora mudanças no consumo de energia para inferir operações.
- **Análise Eletromagnética:** Captura sinais emitidos pelo processador.

---

### **2.4 Ataques Físicos**

- **Tampering Físico:**
    - Um invasor pode tentar manipular fisicamente o processador para acessar dados protegidos.
- **Cold Boot Attack:**
    - Congelar o processador ou a RAM para preservar dados voláteis.

---

## **3. Como Defender um Processador**

### **3.1 Mitigações de Vulnerabilidades**

- Atualizar constantemente o firmware e o microcódigo.
- Aplicar patches no sistema operacional para falhas conhecidas (ex.: Spectre e Meltdown).

---

### **3.2 Proteções Contra Side-Channel**

- **Isolamento de Processos:**
    - Usar virtualização para separar ambientes.
- **Software Patching:**
    - Corrigir falhas que permitam exploração de timing e cache.
- **Técnicas Criptográficas:**
    - Evitar padrões previsíveis que possam ser inferidos por ataques.

---

### **3.3 Proteção Física**

- Usar lacres de segurança em servidores críticos.
- Implementar controle de acesso físico ao hardware.

---

### **3.4 Hardening do Sistema**

- Ativar o Secure Boot e configurar o Trusted Platform Module (TPM) para verificar a integridade do sistema.
- Desabilitar tecnologias desnecessárias no BIOS/UEFI (como Hyper-Threading em sistemas críticos).