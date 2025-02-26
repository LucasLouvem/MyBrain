Além das ferramentas SIEM, sniffers de pacotes e playbooks, um analista de segurança também precisa de conhecimentos em **linguagens de programação** e **sistemas operacionais**. Esses conhecimentos ajudam a automatizar tarefas, analisar dados e monitorar sistemas de forma mais eficiente.

---

### **1. Linux: O Sistema Operacional Preferido para Segurança**

O **Linux** é um sistema operacional de código aberto amplamente utilizado em segurança cibernética. Diferente do Windows e macOS, o Linux se baseia fortemente na **linha de comando**, permitindo um controle maior sobre o sistema e facilitando a análise forense e monitoramento.

#### **Uso do Linux na Segurança:**

- **Análise de logs:** Um analista pode usar comandos como `cat`, `grep` e `tail` para revisar registros de erros e investigar atividades suspeitas.
- **Monitoramento de tráfego de rede:** Comandos como `netstat` e `tcpdump` ajudam a identificar conexões inesperadas.
- **Automação de tarefas:** Bash scripting pode ser usado para automatizar análises e respostas a incidentes.

💡 **Exemplo prático:** Se um tráfego incomum for detectado na rede, um analista pode usar o Linux para acessar e analisar os logs rapidamente, identificando possíveis ataques.

---

### **2. SQL: A Linguagem dos Bancos de Dados**

**SQL (Structured Query Language)** é usada para **consultar e manipular dados armazenados em bancos de dados**. Como um banco de dados pode conter milhões de registros, SQL permite que um analista recupere informações relevantes rapidamente.

#### **Uso do SQL na Segurança:**

- **Identificação de acessos suspeitos:** Consultas podem revelar tentativas de login fora do horário comum ou de locais incomuns.
- **Análise de logs armazenados:** Empresas registram eventos de segurança em bancos de dados e um analista pode usar SQL para filtrar registros importantes.
- **Auditorias de segurança:** Verifica alterações em bancos de dados críticos para detectar acessos não autorizados.

💡 **Exemplo prático:** Um analista pode rodar um comando SQL como:

SQL;
`SELECT * FROM logs WHERE event_type = 'failed_login' AND timestamp > NOW() - INTERVAL 1 DAY;`

Isso retorna todas as tentativas de login malsucedidas nas últimas 24 horas, ajudando a detectar ataques de força bruta.

---

### **3. Python: Automação e Análise**

**Python** é amplamente usado na segurança cibernética devido à sua simplicidade e eficiência. Ele permite criar scripts que automatizam tarefas demoradas e realizam análises detalhadas.

#### **Uso do Python na Segurança:**

- **Automação de varreduras de segurança:** Pode ser usado para rodar scripts de verificação automática de vulnerabilidades.
- **Análise de logs e pacotes de rede:** Com bibliotecas como `pandas` e `scapy`, é possível processar grandes volumes de dados rapidamente.
- **Criação de ferramentas customizadas:** Muitos hackers éticos criam seus próprios scripts para testar a segurança de sistemas.

💡 **Exemplo prático:** Um script em Python pode verificar endereços IP bloqueados em logs:

python; 
```
import pandas as pd  

logs = pd.read_csv("logs.csv") 
ip_bloqueados = logs[logs["status"] == "blocked"] 
print(ip_bloqueados)

```


Isso economiza tempo, pois evita a busca manual em milhares de registros.

---

### **Conclusão**

- **Linux:** Essencial para análise forense, monitoramento de tráfego e gerenciamento de logs.
- **SQL:** Permite recuperar rapidamente dados importantes de bancos de dados.
- **Python:** Ajuda na automação e análise de grandes volumes de informações.

Cada empresa pode ter ferramentas diferentes, mas dominar esses fundamentos mostra que você é capaz de se adaptar e aprender novas tecnologias rapidamente.

Próximo Modulo [[Usar Ferramentas para proteger as operações comerciais]]
