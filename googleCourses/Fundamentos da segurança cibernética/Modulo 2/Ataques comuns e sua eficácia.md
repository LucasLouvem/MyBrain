Nesta leitura, você aprenderá mais sobre os métodos comuns de ataque. Familiarizar-se com os diferentes métodos de ataque _e_ com a evolução das táticas e técnicas usadas pelos agentes de ameaças o ajudará a proteger melhor as organizações e as pessoas.

# Phishing

Phishing é o uso de comunicação digital para enganar as pessoas e fazê-las revelar dados confidenciais ou instalar softwares mal-intencionados.

Alguns dos tipos mais comuns de phishing são:

- Bussiness-to-bussines Compromise (BEC):
	- Um agente de ameaças que envia uma mensagem de email que parece ser de uma fonte conhecida para fazer uma solicitação aparentemente legítima de informações, a fim de obter uma vantagem financeira.
	- **Exemplo Real**: 
		- Em 2019, a Toyota sofreu um ataque BEC que resultou na perda de 37 Milhões de dólares. Os atacantes se passaram por um fornecedor legítimo, solicitando o pagamento para uma conta falsa.
	- Como prevenir:
		- Implementar autenticação de múltiplos fatores (MFA)
		- Validar solicitações de pagamentos por meio de canais externos.

- Spear phishing:
	- Ataque de e-email mal-intencionado que tem como alvo *um* usuário específico ou um grupo de usuários. O e-mail parece ter sido originado de um fonte confiável.
	- **Exemplo Real**:
		- O ataque de spear phishing de 2016 contra o Comitê Nacional Democrata nos EUA, realizado por hackers russos, usou um e-mail disfarçado como alerta de segurança da google. levando ao vazamento de e-mails críticos durante as eleições.
	- Como Prevenir:
		- Educar os funcionários sobre identificação de e-mails suspeitos.
		- Implementar ferramentas de análise comportamental para detectar acessos anômalos.

- Whaling:
	- Uma forma de spear phishing. Os agentes da ameaça têm como alvo os executivos da empresa para obter acesso a dados confidenciais.
	- **Tática**: Email bem elaborados que simulam comunicação internas ou solicitações urgentes.

- Vishing:
	- E exploit da comunicação eletrônica de voz para obter informações confidenciais ou para se passar por uma fonte conhecida.
	- **Exemplo Real**:
		- Em 2020, Funcionários do Twitter foram vítimas de um ataque vishing, em que os atacantes se passaram por representante de TI para obter credenciais e sequestrar contas de grandes figuras públicas.
	- Prevenção:
		- Treinamento sobre verificação de chamadas.
		- Restrição de informações sensíveis por telefone.

- Smishing:
	- O uso de mensagens de texto para enganar os usuários, a fim de obter informações confidenciais ou se passar por uma fonte conhecida. 
	- **Exemplo comum**:
		- Mensagens fingindo ser de bancos ou entregas, com links maliciosos para roubar dados.
	- Prevenção:
		- Nunca clicar em links não solicitados.
		- Validar informações diretamente com a instituição.
---
# Malware

Software projetado para danificar dispositivos ou redes, geralmente visando lucro financeiro ou vantagem de inteligência.

Tipos de Malware:
1. Vírus:
	- Programa malicioso que se espalha entre computadores e pode causar danos aos dados, software e sistemas.
	- Funcionamento: 
		- Necessita de interação humana (Ex: Abrir anexos de e-mails).
	- Exemplo: 
		- O virus Melissa (1999), distribuído por e-mails, se replicava para contatos do catálogo de endereços.
	- prevenção:
		- Usar software antivirus atualizado:
		- Implementar politicas rigorosas de download de arquivos.
2. Worms:
	- Programa independente, se replica com o objetivo de se espalhar, diferente do virus um worm é um programa malicioso independente que se replica e se espalha automaticamente pela rede.
	- Exemplo: 
		- O worm Stuxnet, Projetado para sabotar o programa nuclear iraniano, explorava vulnerabilidades no windows sem necessidade de intervenção humana.
	- Prevenção:
		- Aplicar patches de segurança regulamente.
		- Monitorar tráfego de rede para identificar comportamento anômalo.
3. Ransomware:
	- Software usado para extorsão por meio de sequestro de dados digitais usando criptografia, cobrando um resgate para restabelecer acesso aos dados.
	- Exemplo real: 
		- O ataque WannaCry (2017), criptografou dados em sistemas Windows, exigindo pagamento em bitcoin.
	- Prevenção:
		- Backups regulares e offline.
		- Segmentação de redes para limitação a propagação
4. Spyware:
	- Malware que espia computadores e dispositivos para coletar dados pessoais.
	- Exemplos: 
		- Pegasus, um spyware usado para invadir dispositivos de jornalistas e ativistas, coletando informações sem consentimento.
	- Prevenção:
		- Restringir permissões de aplicativos.
		- Usar firewall para bloquear comunicação não autorizada.
5. 
---
# Engenharia social

Manipulação psicológica para explorar o erro humano e obter acesso não autorizado.

Tipos de Engenharia Social:

1. Phishing de Mídia Social:
	- Exemplo real: 
		- ataques onde agentes coletam informações no Linkedin para personalizar e-mails maliciosos direcionados a funcionários de alto escalão.
	- Prevenção:
		- Configurar perfis de mídia social para limitar informações visíveis publicamente.
2. Ataque de Watering Hole:
	-  Funcionamento: 
		- Atacantes comprometem sites populares entre alvos específicos (ex: um fórum técnico).
	- Exemplo: 
		- Em 2013, um watering hole atacou empresas de tecnologia infectando um site popular entre desenvolvedores.
	- Prevenção:
		- Verificação de segurança em sites frequentemente usados.
3. USB Baiting:
	- Funcionamento:
		- Dispositivos USB infectados são deixados propositalmente em locais estratégicos.
	- Exemplo: 
		- O ataque de Stuxnet também utilizou drives USB para infectar sistemas isolados.
	- Prevenção:
		- Proibir o uso de dispositivos USB desconhecidos.
4. Engenharia social Física:
	- Exemplo: Um atacante se disfarça como técnico de manutenção para acessar áreas restritas.
	- Prevenção:
		- Implantar identificação biométrica ou cartões de acesso.
		- Treinamento sobre verificação de credenciais.
---
Princípios de Engenharia Social:
1. Autoridade:
	- Ex: Um falso "chefe" solicitando transferências financeiras urgentes.
	- Contramedidas: Confirmar solicitações com outros colegas.
2. Intimidação:
	- Ex: Ameaçar alguém para colocar um pendrive infectado no servidor da empresa.
3. Consenso/prova social:
	- Muitas pessoas acreditam no que os outros estão fazendo, e invasores se aproveitam disso para ganhar confiança e fingir que são legítimos.
	- Ex: Dizer para um funcionário fornecer acesso a dados privados pois outros funcionários ja lhe deram acesso.
4. Confiança:
	- Os invasores estabelecem um relacionamento emocional com usuários que para obter informações pessoais.
5. Urgência:
	- Ex: "Se você não responder agora, sua conta sera suspensa."
	- Contramedidas: Treinamento para lidar com solicitações urgentes.
6. Familiaridade:
	- Ex: Atacantes estabelecendo um falso relacionamento ao longo do tempo para explorar a confiança da vítima.
7. Escassez:
	- Ex: "Somente os 50 primeiros que responderem poderão ter acesso ao benefício."
### **Conclusão**

Como profissional de segurança, é essencial:

- **Educar continuamente usuários e organizações.**
- Identificar e gerenciar riscos de **phishing, malware e engenharia social**.
- Manter-se atualizado com novas táticas e adaptar estratégias de defesa.
Próximo modulo
[[Os Oitos domínios de segurança do CISSP]]
