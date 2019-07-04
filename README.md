# Projeto final de Desenvolvimento de Software - Universidade de Brasília

## Membros:

- Ian Fillipe Pontes Ferreira / 180102087
- Guilherme de Morais Richter / 180101617
- Ítalo Vinícius Pereira Guimarães / 180102656
- Lucas Rodrigues Fonseca / 180114077
- Eric Chagas de Oliveira / 180119508

# Qual o seu privilégio ?

## Algumas informações:
Criamos um site que tem como foco a classificação do indivíduo na sociedade, classificações as quais depende de alguns fatores como a renda, gênero, sexo, estado, tamanho da família, etc.
Para calcular a porcentagem de privilégio do usuário, utilizamos principalmente o dataframe do PNAD 2012 e outras informações externas, como classificação das classes sociais no Brasil, ranking das melhores regiões e definimos uma visão social pessimista porém muito realista em nosso meio, que seria a classificação do gênero e do sexo agrupados.
Este site é um apêndice ao jogo desenvolvido pelos outros grupos do projeto final, com o objetivo de expor as dificuldades e privilégios da realidade social brasileira.
Este trabalho foi orientado pelo docente Pr. Dr. Fábio Macêdo Mendes.

## Método para cálculo do privilégio
### Analisamos a raça e o gênero em 4 diferentes níveis de porcentagem

- Mulher negra = 0%
- Homem negro = 33%
- Mulher branca = 66%
- Homem branco = 100%

### Analisamos a educação em 7 diferentes niveis de porcentagem

- Sem estudo = 0%
- Ensino fundamental incompleto = 16%
- Ensino fundamental completo = 33%
- Ensino médio incompleto = 50%
- Ensino médio completo = 66%
- Ensino superior incompleto = 83%
- Ensino superior completo = 100%

### Analisamos a região em 5 diferentes níveis de porcentagem
- Nordeste = 0%
- Norte = 25%
- Sul = 50%
- Centro-oeste = 75%
- Sudeste = 100%

### Analisamos a renda a partir do dataframe do PNAD 2012
- Calculamos a diferença salarial entre o mais rico e mais pobre e aplicamos a proporção à porcentagem do salário informado, em trabalho coordenado com o grupo Whiskritório, responsável pelo processamento de dados.



