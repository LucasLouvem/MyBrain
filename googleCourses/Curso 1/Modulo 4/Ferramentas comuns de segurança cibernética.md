### **Registros**

**O que são registros?**

- Registros são arquivos que documentam eventos que ocorrem nos sistemas de uma organização.
- Exemplo: Quando um funcionário faz login em um computador, um registro desse evento é gerado. Outro exemplo comum são logs de acessos a websites.

**Por que são importantes?**

- **Identificação de ameaças:** Eles permitem que analistas de segurança revisem atividades suspeitas, como tentativas de login falhas ou acessos não autorizados a sistemas.
- **Auditorias:** Servem como evidências em auditorias de conformidade ou investigações.

💡 **Exemplo prático:** Imagine que um analista nota vários logins falhos seguidos no registro. Isso pode indicar uma tentativa de ataque de força bruta, onde um hacker tenta adivinhar senhas repetidamente.

---

### **Ferramentas SIEM**

**O que é um SIEM?**

- O SIEM (Gerenciamento de Informações e Eventos de Segurança) é um sistema que coleta, analisa e monitora dados de registro.
- Ele organiza os dados em **tempo real** e gera **alertas automáticos** para eventos suspeitos.

#### **Como funciona na prática?**

1. **Coleta:** O SIEM reúne dados de várias fontes, como firewalls, sistemas operacionais e aplicativos.
2. **Análise:** Ele usa regras predefinidas para identificar comportamentos anormais, como acessos fora do horário usual.
3. **Resposta:** Gera alertas para que a equipe de segurança investigue e tome medidas rapidamente.

#### **Ferramentas populares:**

- **Splunk Enterprise:**
    - Plataforma auto-hospedada.
    - Usada para buscar, analisar e visualizar grandes volumes de logs.
    - Exemplo de uso: Um analista pode criar dashboards para monitorar tentativas de login em tempo real.
- **Google Chronicle:**
    - Uma solução SIEM **nativa da nuvem**.
    - Benefício: Atualizações rápidas e escalabilidade para grandes volumes de dados.
    - Exemplo de uso: Uma organização multinacional pode monitorar todas as suas filiais globalmente com o Chronicle.

#### **Por que usar SIEM?**

- Reduz o tempo que os analistas gastam vasculhando logs manualmente.
- Identifica ameaças mais rápido e com mais precisão.

💡 **Exemplo prático:** Um SIEM pode enviar um alerta se detectar múltiplos logins vindos de IPs localizados em diferentes países em um curto intervalo de tempo, o que é um indicativo de ataque.

---

### **Manuais Operacionais**

**O que são?**

- São documentos que orientam analistas sobre **como lidar com incidentes de segurança**.
- Eles descrevem o passo a passo para:
    - Identificar um incidente.
    - Responder a ele (por exemplo, bloqueando um IP malicioso).
    - Realizar ações pós-incidente, como relatórios e auditorias.

#### **Por que são importantes?**

- Garante que todos sigam um processo **padronizado**, reduzindo erros.
- Ajuda na conformidade com leis e regulamentos.

💡 **Exemplo prático:** Um manual pode instruir que, em caso de detecção de malware, o analista deve:

1. Isolar o dispositivo infectado.
2. Notificar a equipe de TI.
3. Executar uma análise completa antes de permitir que o dispositivo volte à rede.

---

### **Analisadores de Protocolo de Rede (Packet Sniffers)**

**O que são?**

- São ferramentas usadas para capturar e analisar o tráfego de rede.
- Permitem ver **o que está acontecendo em uma rede em tempo real**, incluindo os dados enviados e recebidos.

#### **Exemplos de packet sniffers:**

1. **tcpdump:**
    - Ferramenta de linha de comando usada em sistemas Linux/Unix.
    - Permite capturar pacotes e filtrá-los por critérios específicos (ex.: capturar apenas tráfego HTTP).
2. **Wireshark:**
    - Ferramenta com interface gráfica.
    - Permite análises detalhadas de pacotes, mostrando conteúdo como cabeçalhos e dados.

#### **Como eles ajudam?**

- Permitem identificar atividades incomuns, como:
    - Dispositivos na rede enviando grandes volumes de dados para servidores desconhecidos (possível exfiltração de dados).
    - Ataques como ARP spoofing, onde um invasor tenta interceptar o tráfego de outros dispositivos.

💡 **Exemplo prático:** Um analista pode usar o Wireshark para capturar o tráfego de rede e descobrir que um computador interno está enviando dados para um servidor em outro país, indicando um possível comprometimento.

---

### **Por que essas ferramentas são essenciais para analistas iniciantes?**

- **SIEMs** ajudam a priorizar ameaças, automatizando a análise de logs e dados.
- **Manuais** fornecem um caminho claro e documentado para respostas rápidas e eficazes.
- **Packet sniffers** permitem análises em tempo real para solucionar problemas e identificar ameaças.

#### **Conselho para iniciantes:**

Você não precisa ser especialista nessas ferramentas desde o início. Conforme você ganha experiência prática, vai aprendendo a interpretá-las e configurá-las de acordo com as necessidades da organização.

Próximo Modulo [[Ferramentas para proteger as operações comerciais]]
