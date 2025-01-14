A **memória RAM (Random Access Memory)** é um componente essencial em qualquer sistema computacional. Ela armazena temporariamente dados e instruções que o processador precisa acessar rapidamente durante a execução de tarefas. Por ser uma memória volátil, os dados são apagados quando o computador é desligado. Vamos explorar em detalhes sua **composição**, **vulnerabilidades** e **defesas**.

---

## **1. Composição da Memória RAM**

A RAM é composta de vários componentes e tecnologias que influenciam sua capacidade, velocidade e funcionamento.

### **1.1 Estrutura Básica**

- **Células de Memória:**
    - Cada célula de memória armazena um bit (0 ou 1). As células são organizadas em matrizes.
    - Componentes:
        - **Transistor:** Controla a leitura/escrita de dados na célula.
        - **Capacitor:** Armazena a carga elétrica representando o bit.
- **Bancos de Memória:**
    - Divisões internas que permitem acesso simultâneo a múltiplos dados, aumentando a eficiência.

---

### **1.2 Tipos de RAM**

- **DRAM (Dynamic RAM):**
    - Armazena dados em capacitores que precisam ser recarregados constantemente.
    - É o tipo mais comum usado em computadores.
- **SRAM (Static RAM):**
    - Não precisa de recarga constante, mas é mais cara e usada em caches.
- **DDR (Double Data Rate):**
    - Transferência de dados em ambos os ciclos do clock.
    - Gerações: DDR3, DDR4, DDR5 (cada uma com maior velocidade e menor consumo de energia).

---

### **1.3 Componentes Auxiliares**

- **Controlador de Memória (IMC):**
    - Gerencia o acesso à RAM e está integrado em processadores modernos.
- **Clock e Latência:**
    - Clock: Determina a frequência de operação (ex.: 3200 MHz).
    - Latência (ex.: CL16): Mede o atraso entre um comando e sua execução.

---

## **2. Como Atacar a Memória RAM**

Por ser um componente crucial que armazena dados temporários, a RAM é alvo de diversos ataques:

### **2.1 Ataques de Software**

- **Exfiltração de Dados Temporários:**
    - Dados como chaves criptográficas, credenciais e arquivos abertos podem ser extraídos da RAM.
    - _Exemplo:_ Um malware pode escanear a RAM para capturar senhas em texto simples.
- **Ataques a Memória Compartilhada:**
    - Processos diferentes podem compartilhar a mesma área de RAM. Um atacante pode explorar vulnerabilidades para acessar dados de outros processos.

---

### **2.2 Ataques de Side-Channel**

- **Rowhammer:**
    - Consiste em acessar repetidamente células próximas para induzir bit flips (alteração de bits de 0 para 1 ou vice-versa).
    - Impacto: Permite escalar privilégios ou comprometer dados armazenados.

---

### **2.3 Ataques Físicos**

- **Cold Boot Attack:**
    - A memória RAM mantém dados por alguns segundos após o desligamento. Um atacante pode resfriar os módulos para prolongar esse tempo e extrair dados.
    - Exemplo: Congelar os módulos de RAM com spray de ar comprimido invertido e usar ferramentas para ler os dados preservados.

---

## **3. Como Defender a Memória RAM**

Defender a RAM requer uma combinação de medidas físicas, lógicas e de configuração.

### **3.1 Proteções contra Exfiltração**

- **RAM Encryption:**
    - Alguns processadores modernos (como os da linha AMD EPYC) suportam criptografia de RAM. Isso protege os dados mesmo em caso de ataques físicos.
- **Isolamento de Memória:**
    - Utilizar tecnologias como Intel SGX ou ARM TrustZone para isolar áreas da memória.

---

### **3.2 Mitigações Contra Ataques Rowhammer**

- **TRR (Target Row Refresh):**
    - Refresca automaticamente linhas adjacentes para prevenir bit flips.
- **ECC (Error-Correcting Code):**
    - Detecta e corrige automaticamente erros de um único bit.

---

### **3.3 Proteções Físicas**

- **Controle de Acesso Físico:**
    - Garantir que servidores estejam em locais protegidos contra acesso não autorizado.
- **Descarte Seguro de RAM:**
    - Evitar que módulos antigos sejam reutilizados ou vendidos sem serem destruídos fisicamente.

---

### **3.4 Hardening do Sistema**

- **Memória Volátil e Virtualização:**
    - Usar virtualização para separar as memórias de processos diferentes.
- **Configuração de Swap:**
    - Configurar a memória swap no disco com criptografia para proteger dados paginados.

---

## **Exemplo Prático de Ataque e Defesa**

1. **Ataque:** Um atacante executa Rowhammer para corromper uma área de memória pertencente a outro processo e escalar privilégios.
    
    - Impacto: Ele obtém acesso root ao sistema.
2. **Defesa:**
    
    - Utilizar módulos de RAM com ECC para corrigir erros induzidos.
    - Configurar a BIOS/UEFI para habilitar TRR.
    - Monitorar logs de eventos para detectar acessos anômalos à RAM.