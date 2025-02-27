## **Passo 1: Estruturar o Banco de Dados**

Precisamos definir as tabelas e relacionamentos essenciais. Para o MVP, podemos começar com:

### **Tabelas principais:**

✅ **Usuários** (`users`): ID, nome, e-mail, senha hash, 2FA, data de criação.  
✅ **Consultas** (`queries`): ID, usuário ID, e-mail consultado, data da consulta, status (vazado/não vazado).  
✅ **Notificações** (`notifications`): ID, usuário ID, mensagem, status (lida/não lida).

**O que fazer:**

1. Escolher o banco de dados: **PostgreSQL ou MongoDB**?
2. Criar um diagrama do banco de dados (pode usar Draw.io ou dbdiagram.io).
3. Criar os scripts SQL (se for relacional) ou definir a estrutura JSON (se for NoSQL).

---

## **Passo 2: Criar o Backend Básico com API de Consulta**

O backend precisa de uma API que permita:  
✅ **Registro e Login de Usuários** (com JWT e 2FA).  
✅ **Consulta de credenciais vazadas** (API Have I Been Pwned ou outra fonte).  
✅ **Salvar histórico de consultas** para o usuário.

**O que fazer:**

1. Escolher a tecnologia: **Laravel (PHP) ou Express (Node.js)?**
2. Criar um servidor básico com rotas iniciais (`/register`, `/login`, `/check-leak`).
3. Integrar a API externa para verificação de vazamentos.

---

## **Passo 3: Definir Autenticação e Segurança**

A segurança do projeto é essencial. O plano inicial inclui:  
✅ **JWT para autenticação**.  
✅ **2FA (Autenticação em Dois Fatores)** para reforçar a segurança.  
✅ **Criptografia de senhas com bcrypt**.

**O que fazer:**

1. Implementar JWT para autenticação segura.
2. Configurar bcrypt (ou outro método seguro) para senhas.
3. Implementar 2FA via **Google Authenticator ou SMS**.

---

### **Próximos Passos**

1️⃣ Escolher banco de dados e tecnologia do backend.  
2️⃣ Criar o modelo de banco de dados.  
3️⃣ Criar um repositório Git e iniciar a estrutura básica do backend.