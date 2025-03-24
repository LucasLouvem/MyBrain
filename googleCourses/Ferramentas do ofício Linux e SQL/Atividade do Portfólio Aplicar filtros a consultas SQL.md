# **Relatório de Consultas SQL**

## **Descrição do Projeto**

Este projeto tem como objetivo simular consultas SQL aplicadas ao ambiente corporativo de uma empresa de tecnologia. Para isso, realizamos consultas em um banco de dados, abordando diferentes cenários, como tentativas de login, filtragem de funcionários por departamento e localização, e o uso de operadores SQL para refinar os resultados.

---

## **1. Recuperar Tentativas de Login com Falha Após o Expediente**

Para identificar tentativas de login fracassadas após o expediente (18h), utilizamos a seguinte consulta SQL:

```sql
SELECT * FROM log_in_attempts WHERE login_time > '18:00' AND success = '0';
```
### **Explicação:**

- **`login_time > '18:00'`** → Filtra registros onde o horário de login foi após as 18h.
- **`success = '0'`** → Filtra apenas tentativas de login malsucedidas.

---

## **2. Recuperar Tentativas de Login em Datas Específicas**

Para recuperar tentativas de login em dias específicos, usamos a seguinte consulta:

```sql
SELECT * FROM log_in_attempts WHERE login_date = '2022-05-08' OR login_date = '2022-05-09' ORDER BY login_date, login_time;
```
### **Explicação:**

- **`login_date = '2022-05-08' OR login_date = '2022-05-09'`** → Filtra tentativas de login realizadas nos dias 8 e 9 de maio.
- **`ORDER BY login_date, login_time`** → Ordena os resultados primeiro pela data e depois pelo horário da tentativa de login.

---

## **3. Recuperar Tentativas de Login Fora do México**

Para encontrar tentativas de login realizadas fora do México, utilizamos:

```sql
SELECT * FROM log_in_attempts WHERE NOT country LIKE 'MEX%';
```
### **Explicação:**

- **`LIKE 'MEX%'`** → Busca registros onde o país começa com "MEX".
- **`NOT`** → Exclui esses registros, retornando apenas tentativas de login feitas fora do México.

---

## **4. Recuperar Funcionários do Departamento de Marketing**

```sql
SELECT * FROM employees WHERE department = 'Marketing' AND office LIKE 'East%';
```
### **Explicação:**

- **`department = 'Marketing'`** → Filtra funcionários do setor de Marketing.
- **`office LIKE 'East%'`** → Retorna apenas aqueles que trabalham em escritórios localizados na região Leste.

---

## **5. Recuperar Funcionários dos Departamentos de Financeiro ou Vendas**

```sql
SELECT * FROM employees WHERE department = 'Sales' OR department = 'Finance';
```
### **Explicação:**

- **`department = 'Sales' OR department = 'Finance'`** → Retorna funcionários que pertencem ao departamento de Vendas ou Financeiro.

---

## **6. Recuperar Funcionários que Não Trabalham no Setor de TI**

```sql
SELECT * FROM employees WHERE NOT department = 'Information Technology';
```
### **Explicação:**

- **`NOT department = 'Information Technology'`** → Retorna todos os funcionários que não pertencem ao departamento de TI.

---

# **Resumo**

Este projeto aplicou diversas consultas SQL para recuperar informações relevantes de um banco de dados corporativo. Exploramos:  
✅ Filtragem de tentativas de login por horário e sucesso/falha.  
✅ Busca de tentativas de login em datas específicas.  
✅ Uso do operador `LIKE` para filtrar padrões textuais.  
✅ Aplicação dos operadores `AND`, `OR` e `NOT` para refinar buscas.  
✅ Seleção de funcionários com base no departamento e localização.

Com essas consultas, conseguimos simular cenários comuns do dia a dia de uma empresa, auxiliando na análise de segurança, gestão de equipes e tomada de decisões estratégicas.