
"""Você recebeu a lista abaixo vinda do banco de dados da loja. Sua missão é extrair blocos de informações específicas para diferentes departamentos
(Logística, Financeiro e Marketing) usando apenas fatiamento.
Estrutura: [ID, Nome, Preço, Estoque, Categoria, Ativo]produto = [1024,
"Monitor Gamer 24p", 1200.0, 5, "Eletrônicos", True]
1) Bloco de Identificação (Logística):Crie uma nova lista chamada dados_basicos que contenha apenas o ID e o Nome do produto.Regra: Use o
fatiamento que começa no índice 0.
2) Bloco de Operação (Financeiro):Crie uma lista chamada valores que contenha o Preço Unitário e a Quantidade em Estoque.Atenção: Lembre-se
que no fatiamento [início:fim], o índice final é exclusivo (não entra na contagem).
3) Bloco de Classificação (Marketing):Crie uma lista chamada caracteristicas que contenha a Categoria e o Status de Ativo.Desafio de Especialista:
Obtenha esses dois itens usando índices negativos (contando do final para o começo).
4) Cálculo de Verificação:Utilizando a lista valores que você criou na Tarefa 2, multiplique o primeiro elemento pelo segundo para descobrir o valor
total investido nesse estoque. Exiba o resultado.
5) Simulação de Backup:Crie uma cópia exata da lista produto em uma nova variável chamada produto_backup, mas faça isso usando o fatiamento
de "lista completa" ([:])"""


produto = [1024, "Monitor Gamer 24p", 1200.0, 5, "Eletrônicos", True]

dados_basicos = produto[0:2]
print("Dados básicos:", dados_basicos)

valores = produto[2:4]
print("Valores:", valores)

caracteristicas = produto[-2:]
print("Características:", caracteristicas)

total = valores[0] * valores[1]
print("Valor total em estoque:", total)

produto_backup = produto[:]
print("Backup:", produto_backup)