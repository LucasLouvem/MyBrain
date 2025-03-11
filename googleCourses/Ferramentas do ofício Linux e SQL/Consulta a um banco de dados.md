## Consultas Básicas em Bancos de Dados: SELECT, FROM e ORDER BY

**Consultas SQL Essenciais:**

- **SELECT e FROM:** Palavras-chave fundamentais para consultar bancos de dados SQL.
    - `SELECT`: Especifica as colunas a serem retornadas.
    - `FROM`: Indica a tabela a ser consultada.
- **Banco de Dados Chinook:** Banco de dados de amostra utilizado para consultas, contendo dados de uma empresa de mídia digital.

**Comando SELECT:**

- **Especificação de Colunas:**
    - `SELECT customerid`: Retorna a coluna "customerid".
    - `SELECT customerid, city`: Retorna as colunas "customerid" e "city".
- **Retorno de Todas as Colunas:**
    - `SELECT *`: Retorna todas as colunas da tabela.
- **Observação:** Em bancos de dados grandes, o uso de `SELECT *` pode ser ineficiente.

**Comando FROM:**

- **Especificação da Tabela:**
    - `FROM customers`: Indica que a tabela "customers" será consultada.
- **Ponto e Vírgula (;)**: Marca o fim da consulta.
- **Quebras de Linha**: Opcionais, mas melhoram a legibilidade.

**Comando ORDER BY:**

- **Organização de Resultados**: Ordena os registros com base em uma ou mais colunas.
- **Ordem Crescente (Padrão)**:
    - Dados numéricos: Do menor para o maior.
    - Dados alfabéticos: De A a Z.
    - `ORDER BY city`: Ordena os registros pela coluna "city" em ordem crescente.
- **Ordem Decrescente (DESC)**:
    - Dados numéricos: Do maior para o menor.
    - Dados alfabéticos: De Z a A.
    - `ORDER BY city DESC`: Ordena os registros pela coluna "city" em ordem decrescente.
- **Múltiplas Colunas**:
    - `ORDER BY country, city`: Ordena por "country" e, dentro de cada "country", por "city".

**Conclusões Principais:**

- `SELECT` e `FROM` são a base das consultas SQL.
- O `ORDER BY` organiza os resultados de forma eficiente.
- O domínio dessas palavras-chave é fundamental para consultas SQL mais avançadas.