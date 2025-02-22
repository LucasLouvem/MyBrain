# Summary
- O Ataque foi baseado em um Flood de pacotes ICMP o que acarretou em um DDoS, derrubando os servidores por 2 (Duas Horas). O tráfego legitimo de outros usuário foram bloqueados impedindo o acesso aos recursos da rede. A equipe de segurança bloqueou os pacotes ICMP e desligou os serviços não críticos. Após uma investigação foi descoberto que o ataque explorou uma configuração incorreta do firewall. Para mitigar incidentes futuros, foram implementadas novas regras de firewall mais restritivas, monitoramento avançado de tráfego e um sistema IDS/IPS para filtragem de pacotes suspeitos.

# Identify
- Ativos afetados: Rede interna, servidores de aplicação e serviços de marketing digital.
- Ameaça identificada: Ataque DDoS através de flood de pacotes ICMP
- Vulnerabilidade explorada: Firewall mal configurado o qual permite tráfego ICMP sem restrição.
- Impacto: Interrupção dos serviços de rede por duas horas no qual afetou operações internas e clientes.

# Protect
- Regras de firewall aprimoradas: Implementação de limitação de taxa de envios para pacotes ICMP.
- Controle de acesso: Fazer a validação do endereço IP de origem para evitar ataques de spoofing.
- Treinamento: Fazer treinamento com a equipe de segurança para identificar e responder rapidamente a ataques de DDoS.
- Implementação de tecnologias: Implementar tecnologias como IDS/IPS para identificar padrões suspeitos no tráfego de rede.

# Detect
- Monitoramento contínuo: Implementação de software de monitoramento de tráfego para detecção de padrões anômalos.
- Ferramentas de detecção: Fazer o uso de ferramentas SIEM para realização de análise de logs.
- Alertas automatizados: Configuração de alertas em tempo real para tráfego anormal, reduzindo o tempo de resposta agilizando o serviço.
# Respond
- Plano de resposta ao incidente:
	- Bloquear imediatamente pacotes ICMP suspeitos pelo firewall.
	- Isolar os serviços criticos da rede para mitigar o impacto.
	- Comunicação interna rápida ao informar a equipe técnica e operacional.
- Analise pós-incidente:
	- Revisar logs para determinar a origem do ataque.
	- Ajustes nas regras do firewall mais rigidas conforme o necessario.
	- Relatar detalhadamente para documentar o incidente das ações tomadas
# Recover
- Restaurar serviços críticos: Priorização maxima ao recuperar os serviços essenciais da empresa
- Melhorias no plano de recuperação: Criar um plano de respostas mais ágil para minimizar futuros ataque impedindo interrupções.
- Backup e redundância: Garantia de backups atualizados para recuperação rápida dos sistemas
- Revisão de processos: Realizar uma atualização das politicas de segurança para reforçar a resiliencia contra ataque DDoS.

# Reflections/Notes