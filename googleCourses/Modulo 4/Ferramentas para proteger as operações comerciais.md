#### **Kit de ferramentas de um analista de segurança nível básico**

O kit de ferramentas de um analista de segurança depende das necessidades específicas da organização. Essas ferramentas são fundamentais para que o analista possa monitorar, identificar e responder a riscos, vulnerabilidades e incidentes de segurança. Além disso, um bom analista deve estar familiarizado com ferramentas padrão da indústria e ser capaz de aprender rapidamente novas ferramentas.

---

### **Ferramentas SIEM**

**O que são?**

- Ferramentas SIEM (Gerenciamento de Informações e Eventos de Segurança) são aplicativos que coletam e analisam registros de eventos dos sistemas de uma organização.
- Elas permitem identificar ameaças com rapidez, reduzindo o tempo que seria necessário para analisar manualmente grandes volumes de dados.

**Características principais:**

- **Painéis interativos:** Organizam e apresentam dados visualmente em categorias, facilitando a identificação de padrões e anomalias.
- **Alertas automáticos:** Detectam atividades suspeitas, como tentativas de invasão, vulnerabilidades ou riscos.
- **Opções de hospedagem:** Podem ser locais (on-premises) ou na nuvem. Soluções na nuvem são mais simples de configurar e manter, enquanto soluções locais podem ser preferidas por empresas com mais experiência em segurança.

💡 **Exemplo prático:** Imagine uma ferramenta SIEM configurada para alertar sobre múltiplas tentativas de login falhas vindas de IPs diferentes. Isso pode ser um indicativo de ataque de força bruta.

---

### **Analisadores de protocolo de rede (sniffers de pacotes)**

**O que são?**

- Ferramentas que capturam e analisam o tráfego de dados em uma rede, permitindo monitorar informações enviadas e recebidas pelos dispositivos conectados.

**Exemplos:**

1. **Wireshark:**
    - Ferramenta gráfica amplamente usada para análise de pacotes.
    - Útil para identificar falhas de comunicação ou comportamentos anômalos, como ataques man-in-the-middle.
2. **tcpdump:**
    - Ferramenta de linha de comando que captura pacotes diretamente do terminal.
    - Ideal para análises rápidas e específicas, como monitorar apenas um tipo de tráfego.

💡 **Exemplo prático:** Um analista pode usar o Wireshark para verificar se há pacotes saindo da rede para servidores não autorizados, indicando uma possível exfiltração de dados.

---

### **Manuais Operacionais (Playbooks)**

**O que são?**

- Guias que fornecem procedimentos detalhados para responder a incidentes de segurança ou realizar tarefas operacionais. Garantem que os analistas sigam processos padronizados, reduzindo erros.

#### **Tipos de Manuais Importantes**

1. **Cadeia de custódia:**
    
    - Documenta a posse e o controle das evidências durante toda a investigação.
    - Exige o registro detalhado de quem teve acesso às evidências e por quê.
    - Garante que as evidências sejam confiáveis e aceitas em um processo legal.
2. **Proteção e preservação de evidências:**
    
    - Descreve como lidar com evidências digitais frágeis e voláteis.
    - Segue a **ordem de volatilidade**, que prioriza o armazenamento de dados mais propensos a serem perdidos (ex.: memória RAM).
    - Reforça a importância de criar cópias para preservar os dados originais.

💡 **Exemplo prático:** Em uma investigação de violação de dados, o manual pode instruir o analista a:

- Preservar primeiro os dados da memória RAM, pois serão perdidos se o sistema for desligado.
- Registrar cada passo da coleta de evidências para evitar contestação legal.

---

### **Lições-chave**

1. **Ferramentas SIEM:** Automação e visualização de dados ajudam a identificar ameaças rapidamente.
2. **Sniffers de pacotes:** Permitem o monitoramento em tempo real do tráfego de rede, auxiliando na detecção de anomalias.
3. **Manuais operacionais:** Garantem padronização e preservação adequada de evidências durante investigações forenses.

Se as investigações forenses interessam a você, considere explorar mais ferramentas e técnicas, como análise de sistemas de arquivos e ferramentas de recuperação de dados. Essas habilidades complementam o trabalho de proteção e resposta a incidentes.