## Hypertext Transfer Protocol (HTTP)

Sendo o principal protocolo para comunicação na Word Wide Web, definindo as regras para transmissão de informações entre clientes, como navegadores e servidores web. Trabalha na camada de aplicação do modelo [[OSI]], baseando em cliente-servidor, onde o cliente faz a requisição e o servidor responde.
### Características principais do HTTP
1. Sem estado(Stateless):
	1. No HTTP cada requisição e considerada uma nova, ela não salva os estados de requisições anteriores, para lidar com isso, tecnologias utilizam de cookies e sessões. 
2. Baseado em Texto:
	1. Utiliza texto puro em sua transferência de dados o que permite que seja facilmente compreendido por humanos, tornando fácil de depurar e analisar.
3. Protocolo de requisição-resposta:
	1. Cliente: O cliente faz uma requisição para o servidor.(Ex. uma página da web)
	2. Servidor: O servidor então retorna com os dados da solicitação ou mensagem de erro.
---
### Estrutura de uma requisição HTTP

Uma requisição tem os seguintes componentes.
- Linha de requisição:
	- Especifica o método HTTP, o recurso solicitado(URL) e a versão do protocolo. Exemplo( `GET /index.html HTTP/1.1` )
- Cabeçalhos:
	- Informações adicionais sobre a requisição, como o tipo de conteúdo aceito e sobre informações do cliente. Exemplo `User-Agent: Mozilla/5.0`
- Corpo(Opcional):
	- Contém dados enviados na requisição, como formulários em um método `POST`.
---
### Estrutura de uma resposta HTTP

As respostas HTTP têm:
- Linha de status:
	- Indica o status do processamento com um código. Ex: `200 = Success, 404 = Not found e etc`, e uma mensagem. Exemplo: `HTTP/1.1 200 ok`
- Cabeçalhos:
	- Informações adicionais sobre o tipo de resposta como o tipo de conteúdo e tamanho: Exemplo: `Content-Type: text/html`
- Corpo(Opcional):
	- Contém o recurso solicitado, como um HTML, JSON ou outro tipo de dado.
---
### Métodos HTTP

Os métodos definem a ação a ser realizada no servidor:
- GET: Recupera dados de um servidor.
- POST: Envia dados para o servidor.
- PUT: Atualiza ou cria um recurso no servidor.
- DELETE: Remove um recurso do servidor.
- PATCH: Realiza uma atualização parcial de um recurso.
- HEAD: Recupera o cabeçalho sem o corpo.
- OPTIONS: Descobre as opções de comunicações disponíveis para um recurso.
---
### Códigos de Status HTTP

Os códigos de de status são divididos em categorias. 

1. 1XX (Informacional): Indica que a requisição está sendo processada.
2. 2XX (Sucesso): Indica que a requisição foi feita com sucesso. (e.g., 200 OK).
3. 3XX (Redirecionamento): Indica que o cliente deve tomar outra ação (e.g., 301 Moved Permanently).
4. 4XX (Erro do cliente): A requisição está incorreta (e.g., 404 Not Found).
5. 5XX (Erro do servidor): Ocorreu um problema no servidor. (e.g., 500 Internal Server Error).
---
### Versões do HTTP

1. HTTP/0.9 => Simples e limitado, usado apenas para transferir arquivos.
2. HTTP/1.0 => Introduziu cabeçalhos, métodos e tipos de mídia.
3. HTTP/1.1 => Melhorou o desempenho com conexões persistentes e suporte a cache.
4. HTTP/2 => Adicionou multiplexação, compressão de cabeçalhos e maior eficiência.
5. HTTP/3 => Utiliza QUIC (baseado em [[UDP]]) para maior velocidade e confiabilidade.
---
### Segurança no HTTP

O protocolo HTTP por ser feito em texto puro e inseguro pois qualquer um que capturasse os pacotes poderia ler todo o conteúdo facilmente, então pode ser utilizado uma Camada com TLS(Transport Layer Security) para criar o HTTPS, o que permite transferência criptografada, garantindo a confidencialidade, Integridade e autenticação dos dados. 