# Resumo Básico de Python

## Introdução
Python é uma linguagem de programação de alto nível, interpretada e de fácil leitura. Possui uma sintaxe simples e é amplamente utilizada para desenvolvimento web, automação, análise de dados, inteligência artificial e muito mais.

## Sintaxe Básica
### 1. Variáveis e Tipos de Dados
```python
nome = "Lucas"  # String
idade = 22       # Inteiro
altura = 1.75    # Float
ativo = True     # Booleano
```

### 2. Entrada e Saída
```python
nome = input("Digite seu nome: ")
print("Olá,", nome)
```

### 3. Operadores Básicos
```python
soma = 10 + 5   # Adição
sub = 10 - 5    # Subtração
mult = 10 * 5   # Multiplicação
div = 10 / 5    # Divisão
divInt = 10 // 5 # Dívisão Inteira
mod = 10 % 3    # Módulo
exp = 2 ** 3    # Exponenciação
```

## Estruturas de Controle
### 4. Condicionais
```python
idade = 18
if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")
```

### 5. Laços de Repetição
```python
# Loop for
for i in range(5):
    print(i)

# Loop while
x = 0
while x < 5:
    print(x)
    x += 1
```

## Funções
```python
def saudacao(nome):
    return f"Olá, {nome}!"

print(saudacao("Lucas"))
```

## Estruturas de Dados
### 6. Listas
```python
numeros = [1, 2, 3, 4]
numeros.append(5)  # Adiciona elemento
print(numeros[0])  # Acessa elemento
```

### 7. Dicionários
```python
pessoa = {"nome": "Lucas", "idade": 22}
print(pessoa["nome"])
```

## Manipulação de Arquivos
```python
with open("arquivo.txt", "w") as f:
    f.write("Olá, mundo!")
```

## Bibliotecas Úteis
```python
import math      # Funções matemáticas
import random    # Geração de números aleatórios
import datetime  # Manipulação de datas e horas