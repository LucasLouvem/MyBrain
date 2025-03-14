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