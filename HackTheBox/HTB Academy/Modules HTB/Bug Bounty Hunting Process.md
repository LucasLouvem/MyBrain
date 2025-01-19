Geralmente Considerado um programa de recompensa de bugs, permitindo poder receber reconhecimento e compensação por encontrar e relatar falhas ou bugs de algum software, o bug bounty e um teste de segurança continuo e proativo que complementa auditorias internas de código e testes de penetração e conclui a estratégia de gerenciamento de vulnerabilidades de uma organização. Os programas de recompensa por bugs são bastante formais e baseados em processos. Para que um caçador de recompensas de bugs seja bem-sucedido, ele deve ser não apenas habilidoso, mas também ciente de:

- Como um programa de recompensas por bugs é estruturado
- Processos de envio e comunicação de bugs/relatórios
## Bug bounty Programs

### Tipos de Programas de Recompensa por Bugs
Os programas de recompensa podem ser separadas por **privados** ou **públicos**.

- ***Programas Privados*** => Não disponíveis publicamente. Um caçador so pode participar após receber um convite específico. A grande maioria começa privado e se torna publica depois de pegarem o jeito de receber e fazer a triagem do relatórios de vulnerabilidades.
	- Na maioria das vezes um caçador e chamado devido seu histórico de encontros de vulnerabilidades, suas consistências de descoberta valida e histórico de violação. Certos programas podem exigir uma verificação de antecedentes.

- ***Programas Públicos*** => Acessíveis por toda a comunidade Hacker.

-  ***Programas Pai/Filho*** => 
	- No contexto de **Bug Bounty**, os **Parent/Child Programs** são estruturas organizacionais que ajudam a gerenciar programas de caça a bugs em grandes organizações ou conglomerados com várias marcas, subsidiárias ou produtos. Aqui está um resumo de como eles funcionam:
	
	---
	
	**1. Parent Program (Programa Pai)**
	
	O **Parent Program** é o programa central ou principal que supervisiona e gerencia os esforços de bug bounty em toda a organização. Ele serve como ponto de entrada para os pesquisadores de segurança e atua como uma camada de abstração para simplificar a comunicação e o gerenciamento.
	
	- **Responsabilidade:**
       - Define políticas e diretrizes gerais de segurança.
    - Centraliza as recompensas (pagamentos).
    - Comunica-se diretamente com os pesquisadores de segurança.
    - Atua como um "hub" para conectar os pesquisadores aos programas filhos.
	- **Exemplo:** Uma empresa como o **Google** pode ter um programa pai que gerencie a segurança em serviços como YouTube, Gmail, e Google Cloud.
    
    ---
    
	**2. Child Programs (Programas Filhos)**
	Os **Child Programs** representam marcas, produtos ou áreas específicas da organização. Cada programa filho tem suas próprias regras, escopos e prioridades, mas está vinculado às diretrizes gerais definidas pelo programa pai.
	- **Responsabilidade:**
    - Especificar o escopo técnico para a área/produto específico.
    - Garantir que os relatórios enviados sejam avaliados por especialistas no contexto adequado.
    - Fornecer respostas e resolver vulnerabilidades detectadas pelos pesquisadores.
	- **Exemplo:** Dentro do programa pai do **Google**, você pode ter um programa filho exclusivo para **YouTube** que define quais endpoints e aplicações relacionadas ao YouTube estão no escopo.
    
    ---
    
	**Como Funciona na Prática?**
	1. **Interação Inicial:** O pesquisador submete um relatório ao **Parent Program**.
	2. **Distribuição:** O programa pai direciona o relatório ao **Child Program** relevante com base no produto ou escopo relatado.
	3. **Processamento:** O programa filho valida, analisa e resolve o bug.
	4. **Pagamento:** O pagamento pode ser gerenciado pelo programa pai ou delegado ao programa filho, dependendo da configuração.
    ---
	**Vantagens dos Parent/Child Programs**
	- **Escalabilidade:** Permite que organizações grandes gerenciem vários produtos de forma eficaz.
    - **Especialização:** Cada Child Program conta com equipes focadas em produtos ou áreas específicas.
    - **Simplificação:** Para os pesquisadores, é mais simples lidar com um ponto de contato único (o Parent Program).
---
### Código de Conduta do Programa de recompensas Por Bugs.
O registro de violação de um caçador e sempre levado em Conta. Por isso e recomendado seguir todas os códigos de conduta/politicas de cada programa de recompensa ou da plataforma(Deixe seu nome limpo.). Leia o código de conduta, não serve so para estabelecer as expectativas de comportamento, mas o torna mais eficaz e bem-sucedido na hora de enviar o relatório.

Se quiser se tornar um Caçador conhecido, precisa equilibrar o profissionalismo e capacidade técnica.

---

### Estrutura do programa de Recompensas Por Bugs.
Já é hora de vermos como é um programa de recompensas por bugs. Navegue até [a lista de programas de recompensas por bugs do HackerOne](https://hackerone.com/bug-bounty-programs) para examinar alguns programas de recompensas por bugs. Tome o [Alibaba BBP](https://hackerone.com/alibaba?type=team) e [o Programa de Pesquisa de Vulnerabilidade da Amazon](https://hackerone.com/amazonvrp?type=team) como exemplos e analise sua "Política".

De acordo com o HackerOne: A [seção de políticas](https://docs.hackerone.com/programs/policy-and-scope.html) permite que as organizações publiquem informações sobre seu programa para comunicar os detalhes sobre seu programa aos hackers. As organizações normalmente publicam uma política de divulgação de vulnerabilidades com orientações sobre como desejam receber informações relacionadas a possíveis vulnerabilidades em seus produtos ou serviços online. A política também inclui o [escopo](https://docs.hackerone.com/programs/defining-scope.html) do programa, que lista itens que os hackers podem testar e enviar relatórios. Muitas vezes, é definido pelo nome de domínio para aplicativos da web ou pelos aplicativos móveis específicos da App Store / Play Store que uma empresa cria.

Um programa de recompensas por bugs geralmente consiste nos seguintes elementos:

| Vendor Response SLAs          | Define quando e como o fornecedor responderá                                                                                                  |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| Access                        | Define como criar ou obter contas para fins de pesquisa                                                                                       |
| Eligibility Criteria          | Por exemplo, ser o primeiro relator de uma vulnerabilidade a ser elegível, etc.                                                               |
| Responsible Disclosure Policy | Define cronogramas de divulgação, ações de coordenação para divulgar com segurança uma vulnerabilidade, aumentar a segurança do usuário, etc. |
| Rules of Engagement           |                                                                                                                                               |
| Scope                         | Intervalos de IP no escopo, domínios, vulnerabilidades, etc.                                                                                  |
| Out of Scope                  | Intervalos de IP fora do escopo, domínios, vulnerabilidades, etc.                                                                             |
| Reporting Format              |                                                                                                                                               |
| Rewards                       |                                                                                                                                               |
| Safe Harbor                   |                                                                                                                                               |
| Legal Terms and Conditions    |                                                                                                                                               |
| Contact Information           |                                                                                                                                               |

---
### Encontrando programas de recompensa por bugs

Um dos melhores recursos online para identificar programas de recompensa por bugs de sua preferência é o [Diretório do HackerOne](https://hackerone.com/directory/programs). O diretório do HackerOne pode ser usado para identificar organizações que possuem um programa de recompensas por bugs e informações de contato para relatar vulnerabilidades que você encontrou eticamente.

---
## Writing a Good Report
Ao documentas nossas descobertas devemos ser claros e precisos, de um forma que a equipe de triagem ou segurança possa entender. Deverá ser mostrado sobre a vulnerabilidade informações sobre e seu passo a passo para poder reproduzir.

As vezes dependendo de empresas de pequeno porte, devemos dizer de maneira mais simples sem tantos termos técnicos para poderem entender o gravidade de cada vulnerabilidade.

Os elementos essenciais para um relatório são(A ordem pode mudar.)

| Vulnerability Title       | Incluindo o tipo de vulnerabilidade, domínio/parâmetro/endpoint afetado, impacto, etc.                                     |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| CWE & CVSS score          | Para comunicar as características e a gravidade da vulnerabilidade.                                                        |
| Vulnerability Description | Melhor compreensão da causa da vulnerabilidade.                                                                            |
| Proof of Concept (POC)    | Etapas para reproduzir a vulnerabilidade de forma clara e precisa.                                                         |
| Impact                    | Explica o que e até onde um invasor poderá chegar ao explorar a falha, e quais os tipos de impactos e a gravidade do dano. |
| Remediation               | Opcional em programas de recompensas de bugs, **mas** é bom ter                                                            |
Relatórios bem feitos, podem diminuir muito o tempo de uma equipe de triagem e segurança na hora de reproduzir a falha. 

---

### Por que CWE & CVSS