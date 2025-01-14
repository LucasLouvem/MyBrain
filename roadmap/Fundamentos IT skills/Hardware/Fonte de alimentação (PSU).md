A **fonte de alimentação** é um componente essencial em computadores e sistemas eletrônicos, responsável por converter energia elétrica de entrada em níveis adequados para os demais componentes. Além disso, protege contra variações de energia que poderiam danificar os equipamentos. Aqui está um detalhamento completo sobre sua **composição**, **formas de ataque** e **defesas**.

---

## **1. Composição da Fonte de Alimentação**

Uma fonte de alimentação é composta por diversas partes que trabalham em conjunto para garantir a estabilidade e eficiência do fornecimento de energia.

### **1.1 Estrutura Geral**

- **Transformador:**
    - Reduz ou aumenta a tensão elétrica, dependendo da necessidade.
    - Em fontes modernas (fontes chaveadas), é usado para isolar e ajustar a tensão de entrada.
- **Circuito Retificador:**
    - Converte corrente alternada (AC) em corrente contínua (DC).
    - Normalmente usa diodos ou pontes retificadoras.
- **Filtro de Saída:**
    - Suaviza os pulsos da corrente retificada, eliminando ondulações indesejadas.
- **Regulador de Tensão:**
    - Garante que a saída de energia seja constante e estável, independentemente de flutuações na entrada.
- **Circuito de Controle (PWM):**
    - Ajusta dinamicamente o fornecimento de energia, aumentando a eficiência e reduzindo perdas.
- **Capacitores:**
    - Armazenam e liberam energia para estabilizar a corrente.
- **Ventoinha e Dissipadores:**
    - Dissipam o calor gerado durante a conversão de energia.
- **Conectores de Saída:**
    - Cabos específicos para alimentar a placa-mãe, processador, dispositivos de armazenamento e outros periféricos.

---

### **1.2 Tipos de Fontes de Alimentação**

- **Fontes ATX:**
    - Mais comum em PCs modernos, compatível com o padrão ATX.
- **Fontes Modulares:**
    - Permitem conectar apenas os cabos necessários, melhorando a organização e fluxo de ar.
- **Fontes de Alta Eficiência:**
    - Certificações como **80 PLUS Bronze, Silver, Gold, Platinum** e **Titanium** indicam eficiência energética superior.

---

## **2. Como Atacar a Fonte de Alimentação**

Embora as fontes de alimentação pareçam menos atrativas para ataques, elas podem ser exploradas de várias formas, com consequências potencialmente severas para o sistema.

### **2.1 Ataques Elétricos**

- **Sobrecarga de Energia:**
    - Conectar dispositivos que excedam a capacidade da fonte, causando falhas ou superaquecimento.
- **Variações de Tensão:**
    - Picos de energia (surge) ou quedas de tensão (sags) podem danificar os componentes internos ou a eletrônica conectada.
- **Injeção de Ruído Elétrico:**
    - Perturbações na linha elétrica podem interferir no funcionamento de componentes sensíveis, como processadores e RAM.

---

### **2.2 Ataques Físicos**

- **Sabotagem Direta:**
    - Danificar componentes internos, como capacitores ou o circuito PWM.
    - Exemplo: Cortar cabos ou desconectar conectores essenciais.
- **Indução de Sobreaquecimento:**
    - Bloquear as aberturas de ventilação ou danificar a ventoinha para causar superaquecimento.

---

### **2.3 Ataques Indiretos**

- **Manipulação de Firmware (em fontes inteligentes):**
    - Algumas fontes modernas possuem microcontroladores que podem ser manipulados para alterar os níveis de saída.
- **Ataques à Rede Elétrica:**
    - Cortes de energia ou alterações na qualidade da linha elétrica podem causar danos à fonte.

---

## **3. Como Defender a Fonte de Alimentação**

Proteger a fonte de alimentação envolve tanto medidas físicas quanto lógicas para evitar ataques ou danos acidentais.

### **3.1 Proteções Internas**

- **Filtros de Linha:**
    - Componentes internos que reduzem ruídos e protegem contra surtos de energia.
- **Proteções Contra Sobrecarga:**
    - Circuitos que desligam automaticamente a fonte em caso de excesso de carga ou curto-circuito.
- **Capacitores de Alta Qualidade:**
    - Usar capacitores de marcas confiáveis (ex.: Nippon Chemi-Con) para garantir durabilidade.

---

### **3.2 Medidas Externas**

- **Nobreaks e Estabilizadores:**
    - Um nobreak (UPS) fornece energia de reserva e protege contra picos de tensão.
    - Estabilizadores ajustam a tensão de entrada, mas são menos comuns em setups modernos.
- **Filtros de Linha e DPS (Dispositivo de Proteção contra Surtos):**
    - Absorvem picos de energia antes que atinjam a fonte.
- **Aterramento Elétrico:**
    - Um sistema de aterramento adequado dispersa surtos de energia para o solo, protegendo a fonte e outros componentes.

---

### **3.3 Hardening Físico**

- **Restrições de Acesso:**
    - Impedir o acesso físico a servidores ou equipamentos críticos.
- **Monitoramento de Temperatura:**
    - Usar sensores e software para alertar sobre temperaturas anormais.

---

## **Exemplo Prático de Ataque e Defesa**

1. **Cenário de Ataque:**
    
    - Um atacante bloqueia as saídas de ar da fonte de alimentação, causando superaquecimento.
    - Como resultado, a fonte desliga abruptamente para proteger o sistema, interrompendo operações críticas.
2. **Defesa:**
    
    - O administrador instala um sistema de monitoramento de temperatura e ativa alarmes para condições térmicas anormais.
    - Além disso, a fonte de alimentação possui proteção contra sobreaquecimento, que desliga automaticamente o sistema antes que danos sejam causados.