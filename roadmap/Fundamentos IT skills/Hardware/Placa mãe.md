### **1. Composição da Placa-Mãe**

A placa-mãe é composta por diversos subsistemas e componentes, incluindo:

- [[Processador (CPU)]] => O local onde o processador é instalado.
- [[Chipset Placa Mãe.png]] => Controla a comunicação entre o processador, memória, dispositivos de armazenamento e periféricos. É dividido em _northbridge_ (agora integrado na CPU em muitos sistemas modernos) e _southbridge_.
- [[Memoria Ram]] Slots que conectam módulos de memória RAM à placa-mãe.
- **Slots de Expansão:** Incluem PCIe (usados para placas de vídeo, placas de rede, etc.) e PCI.
- **BIOS/UEFI:** Firmware essencial para inicializar o sistema e configurar os componentes de hardware.
- **Controladores e Interfaces:**
    - [[Sata.png]] e [[NVME.png]]: Para conexões de dispositivos de armazenamento.
    - USB ([[USB.png]]), Ethenet e Áudio ([[Ethenet,Audio.png]]): Para periféricos.
- **Barramentos:** Canais que transportam dados entre componentes, como o _Front-Side Bus_ (FSB) ou barramentos PCIe.
- **Reguladores de Tensão:** Garantem que os componentes recebam a energia na voltagem correta.
- **[[Bateria CMOS.png]]:** Alimenta a memória CMOS, que armazena as configurações do BIOS/UEFI.
- **Portas e Conectores:** Incluem GPIO, headers USB, portas traseiras, etc.

---

### **2. Como Atacar uma Placa-Mãe**

Ataques podem explorar vulnerabilidades tanto no firmware quanto no hardware. Exemplos incluem:

#### **Ataques ao Firmware (BIOS/UEFI):**

- **Ataque de Firmware Malicioso:** Modificação do firmware para incluir _rootkits_ que controlam o sistema desde o momento da inicialização.
    - _Exemplo:_ Malware como o [**LoJax**]([LoJax: o primero rootkit do UEFI em uso que é descoberto, cortesia do grupo Sednit](https://www.welivesecurity.com/br/2018/09/27/lojax-o-primero-rootkit-do-uefi-em-uso-que-e-descoberto-cortesia-do-grupo-sednit/)) infecta o UEFI para persistência em sistemas, mesmo após a formatação.

#### **Injeção de Falhas Físicas:**

- **Manipulação de Barramentos:** Ataques no barramento PCIe ou USB podem interceptar ou injetar dados maliciosos.
    - _Exemplo:_ Dispositivos maliciosos como o [Rubber Ducky]([Faça um Rubber Ducky com Arduino](https://www.dio.me/articles/faca-um-rubber-ducky-com-arduino)) podem explorar conexões USB.

#### **Ataques à CMOS:**

- **Reset de CMOS:** Um atacante pode remover a bateria CMOS para limpar senhas do BIOS, caso a máquina tenha proteção fraca.

#### **Ataques de Side-Channel:**

- **Escuta Eletromagnética:** Extração de dados através de sinais eletromagnéticos emitidos pelos componentes da placa-mãe.

#### **Ataques Físicos:**

- **Backdoors de Hardware:** Inclusão de componentes ou circuitos maliciosos durante a fabricação.
    - _Exemplo:_ Casos reportados de backdoors em chips usados por grandes fornecedores.

---

### **3. Como Defender uma Placa-Mãe**

Defender a placa-mãe envolve medidas preventivas e reativas contra ataques físicos e lógicos.

#### **Proteção ao Firmware (BIOS/UEFI):**

- **Atualizações Regulares:** Manter o firmware atualizado para corrigir vulnerabilidades.
- **Secure Boot:** Ativar o Secure Boot para verificar a integridade do sistema durante a inicialização.
- **Senha do BIOS:** Configurar senhas fortes para proteger as configurações do BIOS.

#### **Proteção Física:**

- **Controle de Acesso:** Garantir que o hardware esteja em locais seguros e restritos.
- **Lacres de Segurança:** Utilizar lacres para detectar abertura física não autorizada do gabinete.
- **Isolamento:** Isolar fisicamente conexões críticas (como GPIO ou barramentos expostos).

#### **Monitoramento e Auditoria:**

- **Ferramentas de Análise de Firmware:** Usar ferramentas como [CHIPSEC]([CHIPSEC: A Trusted Analysis Suite is Evolving for New Firmware Threats and Modern Architectures | by Intel | Intel Tech | Medium](https://medium.com/intel-tech/chipsec-a-trusted-analysis-suite-is-evolving-for-new-firmware-threats-and-modern-architectures-39a10474a57a)) ou [Binwalk]([Analysing and extracting firmware using Binwalk 3.1.0 in 2025 | by Anindya Sankar Roy | Medium](https://fr3ak-hacks.medium.com/analysing-and-extracting-firmware-using-binwalk-982012281ff6)) para verificar a integridade do firmware.
- **Log de Eventos:** Configurar logs de eventos no BIOS para identificar atividades suspeitas.

#### **Hardening de Hardware e Software:**

- **Desativação de Portas Não Utilizadas:** Desabilitar portas USB e PCIe não utilizadas para reduzir a superfície de ataque.
- **Firewalls de Hardware:** Implementar firewalls que monitoram comunicações no nível da placa-mãe.

---

### **Exemplo Prático de Ataque e Defesa**

1. **Ataque:** Um adversário utiliza um malware para infectar o UEFI de um sistema com o LoJax.
    
    - _Impacto:_ O malware persiste no sistema mesmo após a reinstalação do SO.
2. **Defesa:**
    
    - Ativar o Secure Boot para garantir a integridade do sistema.
    - Atualizar o firmware da placa-mãe para eliminar vulnerabilidades conhecidas.
    - Usar ferramentas como CHIPSEC para auditar o firmware regularmente.