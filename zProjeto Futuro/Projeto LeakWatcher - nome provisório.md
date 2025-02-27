# 🔥 **Projeto**

## 🎯 **Objetivo**

Criar uma plataforma SaaS que permite aos usuários **verificar e monitorar** se suas credenciais foram vazadas em leaks públicos.

## ⚙️ **Funcionalidades do MVP (Versão Inicial)**

✅ **Verificação de Vazamento**: O usuário insere um e-mail e o sistema retorna se ele já foi vazado.  
✅ **Histórico de Consultas**: O usuário pode visualizar as consultas anteriores.  
✅ **Cadastro e Login**: O usuário pode criar uma conta para salvar suas consultas.  
✅ **Notificações**: O sistema envia alertas quando um novo vazamento for detectado.

## 🏗️ **Arquitetura e Tecnologias**

### **Frontend**

📌 React (Next.js) ou Vue.js → Interface responsiva  
📌 Tailwind CSS → Estilização rápida e leve

### **Backend**

📌 PHP (Laravel) ou Node.js (Express) → API principal  
📌 PostgreSQL ou MongoDB → Banco de dados para armazenar usuários e logs  
📌 JWT + 2FA → Segurança na autenticação

### **Infraestrutura**

📌 Azure (para aprendizado e escalabilidade) ou DigitalOcean  
📌 Docker → Facilitar deploy e gerenciamento  
📌 Grafana + Prometheus → Monitoramento de requisições

### **Fontes de Dados**

🔍 APIs como **Have I Been Pwned (HIBP)** ou coleta de dumps públicos.

---

## 🚀 **Roadmap Inicial**

### **Fase 1: Planejamento e Infraestrutura**

✅ Estruturar banco de dados  
✅ Criar backend básico com API de consulta  
✅ Definir autenticação e segurança

### **Fase 2: Desenvolvimento do MVP**

✅ Criar interface simples (input de e-mail + resultado da consulta)  
✅ Implementar integração com fontes de dados  
✅ Criar sistema de notificações

### **Fase 3: Testes e Beta**

✅ Testes de segurança e desempenho  
✅ Beta fechado para ajustes

### **Fase 4: Lançamento e Expansão**

✅ Plano de monetização (freemium, API para empresas, etc.)  
✅ Melhorias na UX/UI e novas funcionalidades

---

## 🎯 **Próximos Passos**

1️⃣ **Definir um nome final para o projeto** (ou seguir com _LeakWatcher_).  
2️⃣ **Criar o repositório e organizar as tarefas**.  
3️⃣ **Começar pelo backend** (estruturar API e banco de dados).