## Introdução

A segurança de rede envolve a implementação de dispositivos e ferramentas para proteger uma infraestrutura contra ameaças. Esse processo de fortalecimento é chamado de **hardening** e pode ser alcançado por meio de uma abordagem chamada **defesa em profundidade**, que adiciona camadas de proteção.

## Principais Dispositivos e Ferramentas de Segurança

### 1. Firewall

**Função:**

- Filtra o tráfego de rede com base em um conjunto de regras.
- Inspeciona pacotes e permite ou bloqueia conexões com base em portas e protocolos.
- Firewalls de próxima geração (NGFWs) também inspecionam payloads de pacotes.

**Exemplo:**

- Um firewall pode bloquear conexões TCP na porta 22 para impedir acessos SSH externos.

**Limitação:**

- Apenas filtra pacotes com base em regras predefinidas, não detecta ataques sofisticados.

### 2. Sistema de Detecção de Intrusão (IDS)

**Função:**

- Monitora a atividade da rede e alerta sobre possíveis intrusões.
- Detecta ataques conhecidos através de assinaturas e pode identificar anomalias.

**Exemplo:**

- Um IDS pode detectar um ataque DDoS através de picos incomuns de tráfego.

**Limitação:**

- Apenas alerta sobre atividades suspeitas, não bloqueia tráfego malicioso.

### 3. Sistema de Prevenção de Intrusão (IPS)

**Função:**

- Monitora a rede e bloqueia tráfego malicioso automaticamente.
- Atua de forma similar ao IDS, mas com a capacidade de impedir ataques em tempo real.

**Exemplo:**

- Se um IPS detectar um ataque de injeção SQL, ele pode bloquear automaticamente o IP do atacante.

**Limitação:**

- Pode gerar falsos positivos, bloqueando tráfego legítimo.
- Se falhar, pode interromper a conexão da rede.

### 4. Gerenciamento de Eventos e Informações de Segurança (SIEM)

**Função:**

- Agrega e analisa dados de segurança de diferentes fontes em tempo real.
- Facilita a investigação de incidentes através de um painel centralizado.

**Exemplo:**

- O Splunk SIEM pode correlacionar eventos de firewall e IDS para identificar padrões de ataque.

**Limitação:**

- Apenas informa sobre possíveis ameaças, sem ações automáticas de prevenção.

## Comparativo

|Ferramenta|Vantagens|Desvantagens|
|---|---|---|
|Firewall|Filtra pacotes conforme regras|Não detecta ataques avançados|
|IDS|Identifica ataques conhecidos e anomalias|Apenas alerta, não bloqueia ataques|
|IPS|Bloqueia ataques automaticamente|Pode gerar falsos positivos|
|SIEM|Agrega dados para monitoramento centralizado|Apenas informa, sem prevenção ativa|

## Considerações Finais

A escolha dos dispositivos e ferramentas depende do nível de segurança desejado e do orçamento da organização. Uma abordagem combinada, utilizando firewall, IDS/IPS e SIEM, melhora significativamente a segurança da rede.

Próximo Modulo [[Atividade Análise do hardening de rede]]
