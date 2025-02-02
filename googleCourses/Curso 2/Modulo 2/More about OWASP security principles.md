## **Princípios de Segurança do OWASP**

Os analistas de segurança cibernética utilizam princípios fundamentais para **reduzir riscos e proteger dados** dentro das organizações. Esses princípios são aplicados no monitoramento de logs, análise de vulnerabilidades e implementação de controles de segurança.

Os principais princípios incluem:

1️⃣ **Minimizar a Superfície de Ataque**  
2️⃣ **Privilégio Mínimo**  
3️⃣ **Defesa em Profundidade**  
4️⃣ **Separação de Funções**  
5️⃣ **Manter a Segurança Simples**  
6️⃣ **Corrigir Problemas de Segurança Corretamente**  
7️⃣ **Estabelecer Padrões Seguros**  
8️⃣ **Falhar com Segurança**  
9️⃣ **Não Confiar nos Serviços**  
🔟 **Evitar Segurança por Obscuridade**

---

### **1️⃣ Minimizar a Superfície de Ataque**

🔹 Reduzir os pontos de entrada que um invasor pode explorar  
🔹 Desativar funções desnecessárias em aplicativos e sistemas  
🔹 Aplicar restrições de acesso e senhas mais seguras

📌 **Exemplo:** Restringir acessos a apenas usuários autorizados e remover recursos não utilizados em um sistema.

---

### **2️⃣ Privilégio Mínimo**

🔹 Garantir que os usuários tenham **apenas** o acesso necessário  
🔹 Evitar acessos administrativos desnecessários  
🔹 Revisar permissões periodicamente

📌 **Exemplo:** Um analista júnior pode visualizar logs, mas não alterar configurações de segurança.

---

### **3️⃣ Defesa em Profundidade**

🔹 Implementar **múltiplos controles de segurança** em camadas  
🔹 Utilizar MFA, firewalls, IDS e controle de permissões  
🔹 Criar barreiras que dificultam ataques

📌 **Exemplo:** Mesmo se um invasor roubar uma senha, a autenticação multifator impede o acesso.

---

### **4️⃣ Separação de Funções**

🔹 Dividir tarefas para evitar **abuso de poder** e fraudes  
🔹 Garantir que ações críticas exijam mais de uma pessoa  
🔹 Combinar esse princípio com **privilégio mínimo**

📌 **Exemplo:** Quem aprova pagamentos não deve ser o mesmo que processa a folha de pagamento.

---

### **5️⃣ Manter a Segurança Simples**

🔹 Evitar soluções de segurança excessivamente complicadas  
🔹 Facilitar o uso sem comprometer a proteção  
🔹 Equilibrar segurança e usabilidade

📌 **Exemplo:** Criar regras de senha fortes sem exigir trocas excessivas que levem usuários a anotá-las de forma insegura.

---

### **6️⃣ Corrigir Problemas de Segurança Corretamente**

🔹 Identificar **a causa raiz** de falhas  
🔹 Aplicar correções eficazes e testar suas soluções  
🔹 Garantir que **novas vulnerabilidades não sejam criadas**

📌 **Exemplo:** Após um ataque bem-sucedido, revisar logs, corrigir a falha e testar se a solução foi eficaz.

---

### **7️⃣ Estabelecer Padrões Seguros**

🔹 O estado **padrão** de um sistema deve ser **seguro por natureza**  
🔹 O usuário não deve precisar modificar configurações para obter segurança

📌 **Exemplo:** Um sistema que já exige senhas fortes e criptografadas por padrão, sem que o usuário precise ativar essas configurações manualmente.

---

### **8️⃣ Falhar com Segurança**

🔹 Se um controle de segurança falhar, ele deve cair na **opção mais segura**  
🔹 O sistema deve evitar acessos não autorizados em caso de erro

📌 **Exemplo:** Se um firewall falhar, ele deve bloquear todas as conexões em vez de liberar tudo.

---

### **9️⃣ Não Confiar nos Serviços**

🔹 **Terceiros** podem ter políticas de segurança diferentes  
🔹 Nunca assumir que fornecedores externos são seguros  
🔹 Implementar verificações e validações antes de confiar em dados de terceiros

📌 **Exemplo:** Uma companhia aérea deve validar o saldo de pontos de um cliente antes de permitir resgates.

---

### **🔟 Evitar Segurança por Obscuridade**

🔹 **Manter o código-fonte secreto não é uma estratégia confiável**  
🔹 A segurança deve depender de boas práticas, e não do sigilo  
🔹 Aplicar autenticação forte, monitoramento e políticas sólidas

📌 **Exemplo:** Em vez de esconder o código-fonte de um aplicativo, usar MFA, restrições de acesso e auditorias para proteger as contas dos usuários.

---

## **Conclusão**

Os princípios de segurança do **OWASP** ajudam a proteger empresas e usuários contra ameaças cibernéticas. Aplicá-los corretamente permite um ambiente mais seguro, reduzindo riscos e prevenindo incidentes.

Próximo Modulo [[Planeje uma auditoria de segurança]]
