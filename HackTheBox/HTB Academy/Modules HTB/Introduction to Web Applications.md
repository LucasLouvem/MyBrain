# Introdução

Aplicativos web, são executados em navegadores, geralmente adotando a arquitetura cliente-servidor para lidar e executar solicitações. Possuindo o front-end na parte do cliente e outros componentes back-end que são executados no lado do servidor. 
Os aplicativos Web podem ser desenvolvido por qualquer desenvolvedor web e hospedados online em qualquer serviço de hospedagem comum.

---
## Aplicativos da Web vs Sites

Antigamente tínhamos paginas chamadas páginas estáticas no qual todo o conteúdo não era personalizado em tempo real. O que significa que toda página que fosse necessária ter alguma modificação deveria ser feita manualmente por um programador do lado back-end. Também conhecidas como Web 1.0.

Por outro lado, a maioria dos sites utiliza aplicativos da web ou a Web 2.0 pois possui conteúdo dinâmico que muda de acordo com a interação do usuário. a diferença de um aplicativo web para uma página web são que eles são totalmente funcionais e executar vários tipos para o usuário final, além de serem modulares, executando em qualquer tamanho de janela e rodando em qualquer plataforma sem ser otimizado.

![[WebsiteVsWebApp.png]]

---

## Aplicativos Web vs Aplicativos de Sistema Operacional Nativos.

Os aplicativos Web diferente dos de SO, não precisam ser instalados no sistema o que economiza armazenamento de espaço para o usuário final, além de possuir a facilidade se rodar em qualquer sistema operacional através do navegador pois as ferramentas não são executadas no computador da pessoa e sim remotamente no servidor que proporciona a ferramenta.

Outra vantagem e que na hora de atualizar fica mais fácil pois todos estão utilizando a mesma versão do serviço e não e necessário cada usuário ter que atualizar individualmente, podendo ser atualizados através de um Unico local (O servidor Web).

Por outro lado os aplicativos de SO tem suas vantagens em relação a Velocidade de operação e a capacidade de utilizar bibliotecas nativas do sistema operacional e hardware local. O que eleva a rapidez pois tem um vinculo mais profundo com o computador não ficando limitado ao recursos utilizados pelo navegador.

Porém com a tecnologia atual tem sido maior o número de aplicativos híbridos e progressivos. tornado mais rápidos que os aplicativos da Web regulares e mais capazes.

---

## Distribuição De aplicativos da Web

Existem muitos aplicativos da Web de código aberto usados por organizações em todo o mundo que podem ser personalizados para atender às necessidades de cada organização. Alguns aplicativos da Web de código aberto comuns incluem:

- [WordPress](https://wordpress.com/)
- [OpenCart](https://www.opencart.com/)
- [Joomla](https://www.joomla.org/)

Existem também aplicativos da Web proprietários de 'código fechado', que geralmente são desenvolvidos por uma determinada organização e depois vendidos para outra organização ou usados por organizações por meio de um modelo de plano de assinatura. Alguns aplicativos da Web de código fechado comuns incluem:

- [Wix](https://www.wix.com/)
- [Shopify](https://www.shopify.com/)
- [DotNetNuke](https://www.dnnsoftware.com/)

---

## Riscos de Segurança em Aplicativos Web

#### **1. Desafios e Vulnerabilidades**

- **Acessibilidade ampla:** Aplicativos web são acessíveis globalmente e possuem uma vasta superfície de ataque.
- **Ferramentas automatizadas:** Disponíveis para explorar vulnerabilidades, facilitando ataques.
- **Complexidade crescente:** Aplicativos mais avançados aumentam o risco de vulnerabilidades críticas.

#### **2. Impactos dos Ataques**

- **Perdas significativas:** Danos financeiros e interrupções nos negócios.
- **Comprometimento de dados:** Ataques podem acessar dados confidenciais armazenados em servidores e bancos de dados.

#### **3. Importância da Segurança**

- **Testes regulares:** Identificar e corrigir vulnerabilidades imediatamente.
- **Validação do patch:** Garantir que as correções não introduzam novas falhas.
- **Práticas de codificação seguras:** Implementação em todas as fases do desenvolvimento.

---

### Teste de Penetração em Aplicativos Web

#### **1. Necessidade**

- Fundamental para proteger aplicativos internos e voltados à Internet.
- Requer entendimento das tecnologias e camadas do aplicativo.

#### **2. Metodologia**

- **Guia OWASP:** Amplamente utilizado como referência para testes de segurança.
- **Análise de Front-end:** Revisar HTML, CSS e JavaScript para vulnerabilidades como:
    - **Sensitive Data Exposure**
    - **Cross-Site Scripting (XSS)**
- **Interação Navegador-Servidor:** Avaliar tecnologias usadas no servidor e explorar falhas.
- **Cobertura máxima:** Testar em perspectivas autenticada e não autenticada.

---

### Resumo de Boas Práticas

1. Realizar **testes frequentes de segurança**.
2. Implementar **códigos seguros** desde o início do desenvolvimento.
3. Utilizar metodologias reconhecidas como o **OWASP Testing Guide**.
4. Avaliar todas as camadas e tecnologias do aplicativo.

Um dos procedimentos mais comuns é começar revisando os componentes de front-end de um aplicativo da Web, como `HTML`, `CSS` e `JavaScript` (também conhecido como trindade de front-end), e tentar encontrar vulnerabilidades como [Sensitive Data Exposure](https://owasp.org/www-project-top-ten/2017/A3_2017-Sensitive_Data_Exposure) e [Cross-Site Scripting (XSS).](https://owasp.org/www-project-top-ten/2017/A7_2017-Cross-Site_Scripting_(XSS)) Depois que todos os componentes de front-end forem completamente testados, normalmente revisaremos a funcionalidade principal do aplicativo da Web e a interação entre o navegador e o servidor da Web para enumerar as tecnologias que o servidor da Web usa e procurar falhas exploráveis. Normalmente, avaliamos os aplicativos Web de uma perspectiva não autenticada e autenticada (se o aplicativo tiver funcionalidade de login) para maximizar a cobertura e revisar todos os cenários de ataque possíveis.

---

## Atacando Aplicativos da Web

#### **1. Contexto Geral**

- Quase todas as empresas possuem aplicativos web no perímetro externo.
- Aplicativos variam de sites simples a sistemas complexos com múltiplos níveis de usuários.
- Aplicativos web oferecem uma ampla superfície de ataque e estão em constante mudança.
- Alterações simples podem introduzir vulnerabilidades catastróficas, como execução remota de código (RCE) ou acesso a dados confidenciais.

---

#### **2. Vulnerabilidades Comuns**

1. **Injeção de SQL**
    
    - Exploração de entradas inseguras.
    - Impactos: acesso a dados confidenciais, manipulação de arquivos no banco de dados, RCE.
    - Cenário: Extração de e-mails do Active Directory para ataques de pulverização de senha.
2. **Inclusão de Arquivo (LFI/RFI)**
    
    - Leitura de código-fonte para descobrir páginas ou funcionalidades ocultas.
    - Impacto: acesso não autorizado e potencial RCE.
3. **Upload Irrestrito de Arquivos**
    
    - Upload de arquivos maliciosos devido à validação inadequada.
    - Impacto: controle total do servidor web.
4. **IDOR (Referência Direta de Objetos) Insegura**
    
    - Acesso indevido a recursos de outros usuários ao manipular identificadores.
    - Exemplo: Alterar IDs em URLs para editar dados de outro usuário.
5. **Controle de Acesso Quebrado**
    
    - Escalonamento de privilégios devido a má implementação de permissões.
    - Exemplo: Manipulação do parâmetro `roleid` durante registro para criar usuários com privilégios administrativos.

---

#### **3. Abordagem para Segurança**

- Estude e entenda o funcionamento dos aplicativos web e suas diferentes tecnologias.
- Familiarize-se com vulnerabilidades comuns e suas implicações.
- Use uma abordagem iterativa para aprender e aplicar o conhecimento.

---

#### **4. Importância do Conhecimento**

- O domínio sobre ataques web diferencia profissionais de segurança e pentesters.
- Entender vulnerabilidades permite encontrar falhas que outros podem ignorar.
- Ataques a aplicativos web são uma parte recorrente de testes e avaliações.

**Resumo Final:** Dominar ataques web exige estudo aprofundado sobre o funcionamento de aplicações e suas vulnerabilidades. Aplicar esses conceitos em cenários práticos ajudará a identificar e explorar falhas de segurança, protegendo empresas contra ameaças reais.