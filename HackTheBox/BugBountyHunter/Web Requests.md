## Protocolo de Transferência de Hipertexto (HTTP)
Sendo a maioria dos aplicativos utilizados hoje em dia, tanto no computador quanto nos dispositivos móveis, a maioria das comunicações feitas pela internet e utilizando a web por meio do protocolo [[HTTP]], sendo um protocolo de nível aplicativo para acessar os recursos da World Wide Web. Sua conexão consiste em um cliente e um servidor, onde o cliente solicita algum recurso para o servidor, o servidor processa e retorna a solicitação pedida pelo usuário. A porta padrão utilizada para comunicação e a porta **80**, embora não sendo comum pode ser alterada para qualquer outra porta, dependendo da configuração do servidor Web. Quando queremos visitar um site na internet procuramos por seu **Fully Qualified Domain Name** (FQDN como um **Uniform Qualified Domain** (URL para acessar os site desejado como [youtube.com](youtube.com).

---
### URL

Os recurso solicitados são chamados através de um URL, que fornece muito mais especificações que simplesmente o site que queremos acessar. Veja sua estrutura.

![[url.png]]
O que cada componente representa:

| scheme       | http://           | Identifica o protocolo utilizado pelo cliente                                                                                                     |
| ------------ | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| user         | admin:password@   | Opcional, contém as credenciais com o login e senha separados por " **:** " separado do host por um @.                                            |
| host         | inlanefreight.com | informa o host onde o cliente quer se conectar, podendo ser um nome ou um endereço IP                                                             |
| port         | 80                | Informa a porta onde o serviço está hospedado, separado do host por " **:** "                                                                     |
| path         | /dasboard.php     | Caminho do recurso solicitado, podendo ser um arquivo ou pasta, se nada for solicitado retornara ao índice padrão                                 |
| query string | ?login=true       | string de consulta começa com um (?) e consiste em um parâmetro(por exemplo, login) e um valor (true). vários parâmetros serão separados por (&). |
| fragment     | `#status`         | Processados pelo navegador do lado cliente para localizar seções dentro do recurso principal.                                                     |
Nem todos os componentes são necessários para acessar um recurso. Os principais obrigatórios são o (scheme e o host).

---
### Fluxo HTTP

![[anatomia_http.png]]
O diagrama acima apresenta a anatomia de uma solicitação HTTP em um nível muito alto. Na primeira vez que um usuário insere o URL (`inlanefreight.com`) no navegador, ele envia uma solicitação a um servidor [[DNS]] (Domain Name Resolution) para resolver o domínio e obter seu IP. O servidor DNS procura o endereço IP `inlanefreight.com` e o retorna. Todos os nomes de domínio precisam ser resolvidos dessa maneira, pois um servidor não pode se comunicar sem um endereço IP.

**Nota:** Nossos navegadores geralmente procuram primeiro os registros no arquivo local '`/etc/hosts`' e, se o domínio solicitado não existir nele, eles entrarão em contato com outros servidores DNS. Podemos usar o '`/etc/hosts`' para adicionar registros manualmente para resolução de DNS, adicionando o IP seguido pelo nome de domínio.

Depois que o navegador obtém o endereço IP vinculado ao domínio solicitado, ele envia uma solicitação GET para a porta HTTP padrão (por exemplo, `80`), solicitando a raiz `/` caminho. Em seguida, o servidor web recebe a solicitação e a processa. Por padrão, os servidores são configurados para retornar um arquivo de índice quando uma solicitação de `/` é recebida.

Nesse caso, o conteúdo de `index.html` é lido e retornado pelo servidor Web como uma resposta HTTP. A resposta também contém o código de status (por exemplo, `200 OK` que indica que a solicitação foi processada com êxito. O navegador da Web renderiza o conteúdo `index.html` e o apresenta ao usuário.

---
### cURL

[[cURL]] (URL do cliente) é uma ferramenta e biblioteca de linha de comando que suporta principalmente HTTP junto com muitos outros protocolos. Isso o torna um bom candidato para scripts e automação, tornando-o essencial para enviar vários tipos de solicitações da web a partir da linha de comando, o que é necessário para muitos tipos de testes de penetração da web.

---
## Protocolo de Transferência de Hipertexto Seguro (HTTPS)

Na seção anterior, discutimos como as solicitações HTTP são enviadas e processadas. No entanto, uma das desvantagens significativas do HTTP é que todos os dados são transferidos em texto não criptografado. Isso significa que qualquer pessoa entre a origem e o destino pode realizar um ataque Man-in-the-middle (MiTM) para visualizar os dados transferidos.

Para combater esse problema, foi criado o protocolo [[HTTPS]] (HTTP Secure) no qual todas as comunicações são transferidas em um formato criptografado, portanto, mesmo que um terceiro intercepte a solicitação, ele não poderá extrair os dados dela. Por esse motivo, o HTTPS se tornou o esquema principal para sites na Internet, e o HTTP está sendo eliminado e, em breve, a maioria dos navegadores da Web não permitirá a visita a sites HTTP.
### cURL para HTTPS

O [[cURL]] deve lidar automaticamente com todos os padrões de comunicação HTTPS e executar um handshake seguro e, em seguida, criptografar e descriptografar os dados automaticamente. No entanto, se entrarmos em contato com um site com um certificado SSL inválido ou desatualizado, o cURL, por padrão, não prosseguirá com a comunicação para proteger contra os ataques MITM mencionados anteriormente:

Os navegadores modernos fariam o mesmo, alertando o usuário contra a visita a um site com um certificado SSL inválido.

## Cabeçalhos HTTP

Os **cabeçalhos HTTP** são informações adicionais enviadas entre o cliente (ex.: navegador) e o servidor 
durante a comunicação, para controlar e descrever aspectos da requisição ou resposta. Cada tipo de cabeçalho tem um propósito específico, e eles podem ser divididos nas categorias.

---

### 1. **General Headers (Cabeçalhos Gerais)**

Esses cabeçalhos podem ser usados em **requisições** e **respostas**, mas não estão relacionados diretamente ao conteúdo enviado ou recebido. Eles fornecem informações gerais sobre a mensagem HTTP.

**Exemplos:**

- `Cache-Control`: Especifica regras de cache (ex.: `Cache-Control: no-cache`).
- `Connection`: Gerencia a conexão entre cliente e servidor (ex.: `Connection: keep-alive`).
- `Date`: Indica a data e hora em que a mensagem foi gerada (ex.: `Date: Wed, 18 Jan 2025 16:00:00 GMT`).

---

### 2. **Entity Headers (Cabeçalhos de Entidade)**

Usados para descrever as **características do conteúdo** enviado no corpo da mensagem (payload), seja em uma requisição ou resposta.

**Exemplos:**

- `Content-Type`: Indica o tipo do conteúdo (ex.: `Content-Type: application/json`).
- `Content-Length`: Tamanho do corpo da mensagem em bytes (ex.: `Content-Length: 348`).
- `Content-Encoding`: Especifica como os dados foram codificados (ex.: `Content-Encoding: gzip`).
- `Last-Modified`: Data da última modificação do recurso (ex.: `Last-Modified: Tue, 17 Jan 2025 10:00:00 GMT`).

---

### 3. **Request Headers (Cabeçalhos de Requisição)**

Enviados pelo **cliente** para fornecer informações adicionais sobre a requisição ou sobre o cliente.

**Exemplos:**

- `User-Agent`: Informa detalhes sobre o cliente (ex.: `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)`).
- `Accept`: Indica os formatos que o cliente aceita na resposta (ex.: `Accept: application/json`).
- `Authorization`: Contém informações de autenticação (ex.: `Authorization: Bearer token123`).
- `Host`: Especifica o host e a porta do recurso solicitado (ex.: `Host: example.com`).
- `Referer`: Indica a URL de onde a requisição foi feita (ex.: `Referer: https://google.com`).

---

### 4. **Response Headers (Cabeçalhos de Resposta)**

Enviados pelo **servidor** para fornecer informações sobre a resposta, como o status da operação e metadados sobre os dados enviados.

**Exemplos:**

- `Server`: Informa o software do servidor (ex.: `Server: Apache/2.4.54`).
- `Set-Cookie`: Define cookies para serem armazenados no cliente (ex.: `Set-Cookie: sessionId=abc123; Path=/; HttpOnly`).
- `Retry-After`: Indica quanto tempo o cliente deve esperar antes de repetir a requisição (ex.: `Retry-After: 120`).
- `Location`: Usado em redirecionamentos para indicar a nova URL (ex.: `Location: https://example.com`).

---

### 5. **Security Headers (Cabeçalhos de Segurança)**

Esses cabeçalhos ajudam a proteger a aplicação contra ataques como **XSS**, **CSRF** e **clickjacking**, fornecendo controles de segurança ao navegador.

**Exemplos:**

- `Content-Security-Policy (CSP)`: Restringe os recursos que podem ser carregados (ex.: `Content-Security-Policy: default-src 'self'; img-src https://images.com`).
- `Strict-Transport-Security (HSTS)`: Força conexões HTTPS (ex.: `Strict-Transport-Security: max-age=31536000; includeSubDomains`).
- `X-Content-Type-Options`: Evita que o navegador interprete arquivos de tipos diferentes (ex.: `X-Content-Type-Options: nosniff`).
- `X-Frame-Options`: Previne clickjacking ao impedir que a página seja carregada em iframes (ex.: `X-Frame-Options: SAMEORIGIN`).
- `X-XSS-Protection`: Ativa filtros de proteção contra scripts maliciosos no navegador (ex.: `X-XSS-Protection: 1; mode=block`).

---

### Resumo

|**Tipo**|**Função**|
|---|---|
|**General Headers**|Informações gerais sobre a mensagem.|
|**Entity Headers**|Detalhes sobre o conteúdo enviado ou recebido.|
|**Request Headers**|Informações enviadas pelo cliente para o servidor.|
|**Response Headers**|Informações enviadas pelo servidor ao cliente.|
|**Security Headers**|Configurações para proteger o cliente e o servidor contra vulnerabilidades.|

---
## CRUD API

Uma **CRUD API** é uma API que implementa as operações básicas de **Create**, **Read**, **Update** e **Delete** em um sistema. Essas operações correspondem às funções fundamentais que podem ser realizadas em um recurso ou entidade, como usuários, produtos ou posts.

---

### Estrutura de uma CRUD API

Normalmente, uma CRUD API utiliza os métodos HTTP para mapear essas operações. Veja a correspondência:

|**Operação**|**Método HTTP**|**Descrição**|
|---|---|---|
|**Create**|`POST`|Cria um novo recurso.|
|**Read**|`GET`|Lê ou recupera recursos existentes.|
|**Update**|`PUT` ou `PATCH`|Atualiza um recurso existente.|
|**Delete**|`DELETE`|Remove um recurso existente.|
### Exemplo Prático: CRUD para Gerenciar Usuários

#### Recursos e Endpoints

Imagine que estamos criando uma API para gerenciar usuários, com o recurso principal `users`. Aqui estão os endpoints:

|**Operação**|**Endpoint**|**Exemplo**|
|---|---|---|
|**Create**|`POST /users`|Cria um novo usuário.|
|**Read**|`GET /users`|Lista todos os usuários.|
|**Read**|`GET /users/{id}`|Lê detalhes de um usuário.|
|**Update**|`PUT /users/{id}`|Atualiza um usuário inteiro.|
|**Update**|`PATCH /users/{id}`|Atualiza parcialmente um usuário.|
|**Delete**|`DELETE /users/{id}`|Remove um usuário.|
Para testar e interagir com uma **CRUD API** usando **cURL**, você pode usar comandos no terminal para executar as operações de **Create**, **Read**, **Update** e **Delete**. Aqui está um guia prático com exemplos para uma API de gerenciamento de usuários.

---

### Configuração Inicial

Suponha que a API esteja rodando localmente no endereço `http://localhost:3000` e o recurso principal seja `/users`.

---

### 1. **Create (POST)**

Para criar um novo recurso, usamos o método `POST` com o cURL e enviamos dados no corpo da requisição.

**Exemplo: Criar um novo usuário**

bash

CopyEdit

`curl -X POST http://localhost:3000/users \ -H "Content-Type: application/json" \ -d '{"name": "Lucas", "email": "lucas@example.com"}'`

- **`-X POST`**: Define o método HTTP.
- **`-H "Content-Type: application/json"`**: Especifica o tipo de conteúdo como JSON.
- **`-d`**: Envia os dados no corpo da requisição.

**Resposta esperada (JSON):**

json


`{     "id": 1,     "name": "Lucas",     "email": "lucas@example.com" }`

---

### 2. **Read (GET)**

#### **Ler todos os usuários**

`curl -X GET http://localhost:3000/users`

**Resposta esperada:**

json

`[     {         "id": 1,         "name": "Lucas",         "email": "lucas@example.com"     } ]`

#### **Ler um único usuário por ID**

`curl -X GET http://localhost:3000/users/1`

**Resposta esperada:**

json

`{     "id": 1,     "name": "Lucas",     "email": "lucas@example.com" }`

Vemos que o resultado é enviado como uma string JSON. Para formatá-lo corretamente no formato JSON, podemos canalizar a saída para o utilitário `jq`, que o formatará corretamente. Também silenciaremos qualquer saída cURL desnecessária com `-s`, da seguinte maneira:

```
curl -s http://<SERVER_IP>:<PORT>/api.php/city/london | jq

[
  {
    "city_name": "London",
    "country_name": "(UK)"
  }
]

```

---

### 3. **Update (PUT ou PATCH)**

#### **Atualizar todos os dados de um usuário (PUT)**

`curl -X PUT http://localhost:3000/users/1 \ -H "Content-Type: application/json" \ -d '{"name": "Lucas Silva", "email": "lucas.silva@example.com"}'`

**Resposta esperada:**

json

`{     "id": 1,     "name": "Lucas Silva",     "email": "lucas.silva@example.com" }`

#### **Atualizar apenas um campo de um usuário (PATCH)**

`curl -X PATCH http://localhost:3000/users/1 \ -H "Content-Type: application/json" \ -d '{"email": "novo.email@example.com"}'`

**Resposta esperada:**

json

`{     "id": 1,     "name": "Lucas Silva",     "email": "novo.email@example.com" }`

---

### 4. **Delete (DELETE)**

Para remover um usuário, usamos o método `DELETE` com o ID do recurso.

**Exemplo: Deletar um usuário**

`curl -X DELETE http://localhost:3000/users/1`

**Resposta esperada:**

- Código de status HTTP `204 No Content` (sem corpo de resposta).

---

### Testando CRUD API e cURL de Forma Completa

Você pode combinar os comandos acima para simular o ciclo completo de **CRUD**:

1. **Criar um usuário:**
    
    `curl -X POST http://localhost:3000/users \ -H "Content-Type: application/json" \ -d '{"name": "João", "email": "joao@example.com"}'`
    
2. **Ler todos os usuários:**
    
    `curl -X GET http://localhost:3000/users`
    
3. **Atualizar o nome do usuário:**
    
    `curl -X PATCH http://localhost:3000/users/1 \ -H "Content-Type: application/json" \ -d '{"name": "João Silva"}'`
    
4. **Deletar o usuário:**
    
    `curl -X DELETE http://localhost:3000/users/1`
    

---

### Dicas com cURL

1. **Ver cabeçalhos da resposta:** Use o parâmetro `-i` para ver cabeçalhos da resposta.
    
    `curl -i -X GET http://localhost:3000/users`
    
2. **Autenticação:** Caso a API exija autenticação, use o `-u` (usuário e senha):
    
    `curl -u username:password -X GET http://localhost:3000/users`
    
3. **Salvar resposta em um arquivo:** Redirecione a saída para um arquivo:
    
    `curl -X GET http://localhost:3000/users -o resposta.json`