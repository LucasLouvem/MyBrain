Os **periféricos** são dispositivos externos conectados a um sistema de computação, usados para entrada, saída ou armazenamento de dados. Eles desempenham funções importantes para interagir com o hardware e software de um computador. Abaixo está um detalhamento completo sobre sua **composição**, **formas de ataque** e **defesas**.

---

## **1. Composição dos Periféricos**

Os periféricos são variados e podem ser classificados em categorias principais:

### **1.1 Periféricos de Entrada**

São usados para enviar dados para o computador.

- **Teclado:**
    - Composto por switches (mecânicos ou membranas) que acionam sinais elétricos.
    - Controlador interno traduz os sinais em dados legíveis para o sistema.
- **Mouse:**
    - Sensores ópticos ou laser detectam movimentos.
    - Circuitos interpretam cliques e movimentos, enviando dados ao computador.
- **Microfone:**
    - Converte som em sinais elétricos usando membranas sensíveis a vibrações.
    - Circuitos de amplificação melhoram a qualidade do som.

---

### **1.2 Periféricos de Saída**

Exibem ou transmitem informações processadas pelo computador.

- **Monitor:**
    - Painel LCD, LED ou OLED.
    - Inclui circuitos de controle e backlights para gerar imagens.
- **Caixas de Som/Headsets:**
    - Alto-falantes convertem sinais elétricos em som.
    - Amplificadores internos aumentam a potência do áudio.

---

### **1.3 Periféricos de Entrada e Saída**

Desempenham ambas as funções.

- **Impressoras Multifuncionais:**
    - Incluem mecanismos de impressão e scanners.
    - Controladores gerenciam o fluxo de dados entre o dispositivo e o computador.
- **Pen Drives e Discos Externos:**
    - Incluem memória flash ou HDDs para armazenar dados.
    - Conectados via USB, com controladores que gerenciam a transferência de dados.

---

### **1.4 Periféricos de Rede**

Permitem comunicação em rede.

- **Webcams:**
    - Sensores captam imagens e vídeos.
    - Incluem micro-controladores para compressão de vídeo em tempo real.
- **Dispositivos Wi-Fi/Bluetooth:**
    - Usam módulos de rádio para comunicação sem fio.

---

## **2. Como Atacar Periféricos**

Os periféricos, por serem frequentemente conectados via portas externas como USB ou Bluetooth, são vulneráveis a diversos tipos de ataques.

### **2.1 Ataques a Periféricos de Entrada**

- **Keyloggers:**
    - Dispositivos conectados ao teclado para capturar entradas do usuário.
    - Alternativamente, malwares podem interceptar dados digitados.
- **Mousejacking:**
    - Exploração de falhas em dispositivos sem fio (mouse ou teclado) para injetar comandos maliciosos.

---

### **2.2 Ataques a Periféricos de Saída**

- **Exploração de Monitores:**
    - A interceptação de sinais de vídeo (ex.: em conexões VGA ou HDMI) pode expor informações sensíveis.
    - Ataques a portas de monitores inteligentes para acesso remoto.
- **Vazamento de Áudio:**
    - Microfones de headsets podem ser ativados sem permissão.

---

### **2.3 Ataques a Periféricos de Armazenamento**

- **Dispositivos USB Maliciosos:**
    - Dispositivos USB falsificados (ex.: Rubber Ducky) podem injetar scripts maliciosos automaticamente.
- **Ataques de Firmware:**
    - Modificação no firmware de pen drives ou discos externos pode transformá-los em vetores de ataque.
- **Cold Boot Attack:**
    - Recuperação de dados residuais armazenados em dispositivos externos.

---

### **2.4 Ataques a Periféricos de Rede**

- **Hijacking de Webcams:**
    - Malwares podem assumir o controle de webcams, capturando imagens sem o conhecimento do usuário.
- **Interferência em Dispositivos Bluetooth/Wi-Fi:**
    - Ataques como bluesnarfing podem roubar dados transmitidos por dispositivos sem fio.

---

## **3. Como Defender Periféricos**

### **3.1 Proteções Gerais**

- **Atualizações de Firmware:**
    - Manter o firmware atualizado protege contra vulnerabilidades exploradas em ataques.
- **Monitoramento de Portas:**
    - Usar software de segurança para monitorar conexões USB e bloquear dispositivos não autorizados.
- **Criptografia de Comunicação:**
    - Dispositivos que usam Wi-Fi ou Bluetooth devem empregar protocolos seguros (ex.: WPA3 ou BLE com criptografia).

---

### **3.2 Defesas Específicas**

#### Periféricos de Entrada

- **Teclados e Mouses:**
    - Prefira dispositivos com comunicação criptografada.
    - Use detectores de keyloggers para identificar conexões maliciosas.
- **Microfones:**
    - Cubra ou desconecte fisicamente o microfone quando não estiver em uso.

#### Periféricos de Saída

- **Monitores:**
    - Use filtros de privacidade para evitar espionagem visual.
    - Monitore conexões a portas HDMI/VGA.
- **Áudio:**
    - Mute ou desconecte caixas de som quando não forem necessárias.

#### Periféricos de Armazenamento

- **Proteção USB:**
    - Desative portas USB não utilizadas na BIOS/UEFI.
    - Use bloqueadores físicos de porta USB.
- **Criptografia:**
    - Armazene dados sensíveis em dispositivos criptografados.

#### Periféricos de Rede

- **Webcams:**
    - Use tampas de segurança para bloquear a lente.
    - Monitore permissões de aplicativos que acessam a câmera.
- **Bluetooth/Wi-Fi:**
    - Desative dispositivos sem fio quando não estiverem em uso.
    - Realize auditorias regulares de dispositivos emparelhados.

---

## **Exemplo Prático de Ataque e Defesa**

1. **Cenário de Ataque:**
      - Um pen drive aparentemente legítimo é conectado a um computador. Ele contém um payload que executa comandos maliciosos (ex.: criar backdoors).
2. **Defesa:**
	-  O sistema possui uma política que bloqueia automaticamente dispositivos USB desconhecidos.
    - O administrador executa uma varredura no pen drive com software antivírus antes de liberar sua conexão.