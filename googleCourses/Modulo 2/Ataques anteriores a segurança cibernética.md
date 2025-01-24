## Primeiros Ataque a Malware e lições aprendidas

1. Ataques Clássicos: Uma visão geral
	- Muitos ataques atuais são evoluções ou adaptações de métodos antigos.
	- Entender ataques históricos ajuda a antecipar e lidar com ameaças modernas
---
2. Termos chaves:
	- Virus de computador:
		- Códigos maliciosos que interfere nas operações do computador, danifica dados e se anexa a programas ou documentos para se espalhar.
	- Malware
		- Softwares projetados para prejudicar dispositivos ou redes, incluindo vírus, worms, ransomware, entre outros.
---
3. Exemplos de Ataques Marcantes
- Vírus Brain (1986):
	- Criadores: Irmãos Alvi.
	- Intenção Original:
		- Rastreamento de cópias ilegais de software médico.
		- prevenção de uso de licenças piratas.
	- Impacto Real:
		- Infectava computadores que utilizavam software pirata.
		- espalhava-se por discos inseridos nos computadores infectados
		- em poucos meses, atingiu computadores globalmente.
	- Consequências:
		- Redução de produtividade.
		- Interrupção significativa nas operações comerciais.
	- Lições Aprendidas
		- Necessidade de planejamento para manter a segurança e produtividade no setor de computação.
- Worm Morris (1988):
	- Criador: Robert Morris.
	- Objetivo:
		- Medir o tamanho da internet, instalando em computadores conectados.
	- Problema:
		- O worm não verificava se já havia infectado determinado computador, o que ocasionava em se reinstalar continuamente.
	-  Resultados:
		- Sobrecarga de memória nos dispositivos.
		- Computadores travados e 10% da internet afetada ( cerca 6 mil máquinas).
	- Custos:
		- Milhões de dólares em danos devido a interrupções e esforços de recuperação.
	- Legado:
		- Criação das equipes CERT(Computer Emergency Response Teams):
			- Inicialmente focadas em responder incidentes de segurança.
			- Hoje desempenham funções ampliadas, incluindo detecção e resposta proativas.
---
4. Impacto no Setor de Segurança
	- Ataque como Brain e Morris moldaram a segurança cibernética moderna, destacando:
		- A necessidade de equipes dedicadas e ferramentas especializadas.
		- A importância de estratégias preventivas e reativas para proteger sistemas e dados.
___
5. Próximos Passos no Estudo
	- Estudo das **evoluções dos ataques na era digital**.
	- Prática com **ferramentas de detecção e resposta**.
---
## Ataques Notáveis na era digital

1. Expansão da internet e a Nova era do Malware
	- Com a internet confiável de alta velocidade o malware passou a se espalhar digitalmente, sem a necessidade de discos físicos.
	- Isso abriu portas para ataques globais em larga escala, utilizando da rede para maximizar o alcance.
---
2. Casos Notáveis de Ataque Digitais
	- LoveLetter (2000);
		- Criador: Onel De Guzman.
		- Objetivo:
			- Roubar credenciais de login na internet
			- Aproveitar a falta de suspeitas de usuários em relação a emails desconhecidos.
		- Funcionamento:
			- Ele enviava um email com o assunto "eu te amo" e um anexo chamado "Carta de amor para você!".
			- Abrindo o anexo:
				1. Escaneava o catálogo de endereços de emails da vitima
				2. Enviava o malware automaticamente através dele para espalhar
				3. Instalava um programa para roubar os dados de senhas e informações.
		- Impacto:
			- 45 Milhões de computadores infectados globalmente
			- Estimativa de 10 Bilhões de Dólares em danos
		- Lições Aprendidas:
			- Primeiro exemplo conhecido de engenharia social, uma técnica que manipula e explora o erro humano para acessar informações confidenciais.
---
## Engenharia social:

- Definição: uso de manipulação para obter informações privadas ou acesso indevido
- Cenário Atual:
	- Crescimento devido ao aumento de dados públicos em mídias sociais.
	- Conveniência X privacidade:  A Priorização da conveniência frequentemente leva a vulnerabilidades.
- Papel dos profissionais de Segurança:
	- Educar usuários sobre os riscos.
	- Implementar treinamentos internos regulares, especialmente sobre Phishing(Técnica de obter Informações Sensíveis por e-mail enganosos.)
---
3. Violação da Equifax (2017)
	- O que aconteceu:
		- Um dos maiores vazamentos de dados pessoais conhecidos.
		- cerca de 143 milhões de registros comprometidos, afetando cerca de 40% da população americana.
	- Dados Roubados:
		- Números de previdência social, datas de nascimento, números de carteira de motoristas, endereços residenciais e números de cartão de créditos.
	- Causas
		- Vulnerabilidades não corrigidas pela empresa.
		- Falhas em corrigir vulnerabilidades conhecidas durante meses antes do ataque
	- Impacto financeiro:
		- Multa de 575 milhões de dólares para cobrir reclamações de clientes e sanções governamentais.
	- Lições Aprendidas:
		- Enfatizou o alto custo financeiro de falhas de segurança.
		- Alertou empresas sobre a necessidade de medidas preventivas e pro atividade.
---
4. Reflexões e Aprendizados para o Futuro
	- Impacto na Segurança:
		- Ataques como o LoveLetter e a violação da Equifax moldaram o setor.
		- Ressaltaram a importância de medidas preventivas, educação dos usuários e respostas rápidas.
	- Preparação para Profissionais de Segurança:
		- Monitorar tendências, padrão e metodologias de ataque.
		- adaptação constante às mudanças no cenário de ameaças.
		- Comunicação eficaz dos riscos e participações em treinamentos de conscientização
	- Importância do trabalho:
		- O impacto da segurança vai além de sistemas e dados: ela protege vidas e privacidades.
---
