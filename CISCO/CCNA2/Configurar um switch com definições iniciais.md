## Sequencia de inicialização do Switch

Antes de configurar um Switch ele precisa ser ativado e passar pela sequência de inicialização de cinco etapas. Depois que um Switch e ligado ele passa pela seguinte ordem.

1.  **Teste inicial (POST)** → O switch faz uma checagem básica para ver se seus componentes essenciais (CPU, memória e armazenamento) estão funcionando bem.
2. **Carregador de inicialização (Boot Loader)** → Um pequeno programa dentro do switch é ativado para continuar o processo de inicialização.
3. **Configuração da CPU** → Esse programa ajusta a CPU, dizendo a ela como usar a memória corretamente.
4. **Ativação do armazenamento (Flash)** → O switch acessa seu sistema de arquivos interno, onde ficam os arquivos necessários para rodar o sistema operacional.
5. **Carregamento do IOS** → Finalmente, O Sistema operacional do switch(IOS) é carregado, e o switch fica pronto para ser usado.

## O comando Boot System

- O que acontece quando o switch liga?
	- Ele tenta encontrar um sistema operacional para carregar. Primeiro, ele olha a variável chamada *BOOT*

- Se a variável BOOT estiver configurada:
	- O switch segue as instruções dessa variável para encontrar e carregar o sistema operacional correto(IOS).

- Se a variável BOOT não estiver configurada:
	- Ele ira procurar  o primeiro executável na memória *flash* e tenta carregá-lo automaticamente.

- Onde fica o sistema operacional(IOS):
	- Nos switches Catalyst 2960, o IOS normalmente fica dentro de uma pasta com o mesmo no do arquivo(sem a extensão `.bin`)

- E os arquivos de configuração?
	- Depois que carrega o IOS, o switch lê as configurações salvas no arquivo startup-config(também chamado `config.text`) localizado na memória *flash*. Esse arquivo contém as configurações das interfaces e outros ajustes do sistema. 

- Como ver ou mudar Isso?
	 - Para definir manualmente o arquivo de inicialização, usamos o comando:
    
 ```perl
	boot system flash:/<caminho do arquivo IOS>.bin`
```
    
- Para verificar qual arquivo está sendo usado para inicializar, usamos:
```sql
	show boot
```

Resumindo: O switch primeiro tenta usar a variável BOOT para encontrar o IOS. Se não encontrar, busca um arquivo padrão na memória flash. Depois que o IOS carrega, ele aplica as configurações salvas no startup-config. 🚀

# Alternar Indicadores LED

Os switches Cisco Catalyst possuem várias luzes de LED indicando seus status. No qual permite monitorar rapidamente o desempenho e a atividade do switch. Interruptores de diferentes modelos e conjuntos de recursos terão LEDs diferentes e sua colocação no painel diferentes podem ser variadas.

Tipos de botões:
	O botão "MODE" -> usado para alternar pelo status da porta(Porta duplex, velocidade da porta, e se suportado o status Power over Ethernet(POE) dos LEDs da porta).

- 1 SYST -> Mostra se o sistema está recebendo energia e está funcionando corretamente.
	- LED Desligado -> Sistema desligado.
	- LED Verde -> Sistema funcionando normalmente.
	- LED âmbar -> Sistema está recebendo energia, mas não está funcionando corretamente.
- 2 RPS -> Mostra o Status RPS (Sistema redundante de fonte).
	- LED Apagado -> RPS desativado ou não conectado corretamente.
	- LED Verde -> Conectado e pronto para fornecer energia reserva
	- LED Piscando Verde -> RPS conectado mas não disponível pois está fornecendo energia para outro dispositivo.
	- LED Amarelo -> RPS em modo de espera ou em condição de falha.
	- LED piscando âmbar -> Fonte de alimentação interna do comutador falhou e o RPS está fornecendo energia.
- 3 STAT -> LED de status da porta, indica que o modo do status da porta está dependendo da cor.
	- LED de Status da porta verde -> Modo padrão, indica o modo de status da porta está selecionado, quando selecionado, os LEDs de porta exibirão cores com significados diferentes.
	- LED Apagado -> Não a link ou a porta foi desligada administrativamente.
	- LED Verde -> Um link está presente.
	- LED piscando verde -> Há atividade na porta e a porta está enviando ou recebendo dados.
	- LED estiver alternando entre verde-âmbar -> Há uma falha de link.
	- LED Amarelo -> Porta bloqueada para garantir que não exista nenhum loop no domínio de encaminhamento e que este não esteja enviando dados(Portas ficarão nesse estado por aproximadamente 30 segundos após serem ativadas).
	- LED piscando âmbar -> Porta será bloqueada para evitar um possível loop de domínio de encaminhamento.
- 4 DUPLX -> LED da porta duplex
	- LED da porta duplex Verde -> Modo duplex ligado.
	- LED desligados -> Modo Semi-duplex.
	- LED verde -> estará no modo full-duplex.
- 5 SPEED -> Indica que o modo de velocidade da porta está selecionado. Quando selecionado, os LEDs exibirão cores diferentes com significados diferentes.
	- LED apagado -> Porta operando a 10 Mbps.
	- LED verde -> Porta operando a 100 Mbps.
	- LED piscando verde -> Porta operando a 1000 Mbps.
- 6 PoE -> Led do modo Power over Ethernet (PoE) - Se suportado, um LED de modo PoE estará presente.
	- LED desligado -> Modo PoE não selecionado e que nenhuma das portas foi negada energia ou colocada em uma condição de falha.
	- LED piscando âmbar -> Modo PoE não selecionado, mas pelo menos uma das portas foi negada energia ou tem uma falha PoE.
	- LED verde -> indica que o PoE foi selecionado e os LEDs da porta exibirão cores com significados diferentes.
		- LED da porta 