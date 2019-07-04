# Projeto final de Desenvolvimento de Software - Universidade de Brasília

## Membros:

- Ian Fillipe Pontes Ferreira - 18/0102087
- Guilherme de Morais Richter - 18/0101617
- Ítalo Vinícius Pereira Guimarães - 18/0102656
- Lucas Rodrigues Fonseca - 18/0114077
- Eric Chagas de Oliveira - 18/0119508

# Qual o seu privilégio?

## Algumas informações:
- Criamos um site em Flask, que tem como foco a classificação do indivíduo na sociedade, classificações as quais depende de alguns fatores como a renda, gênero, sexo, estado, tamanho da família, etc.
- Para calcular a porcentagem de privilégio do usuário, utilizamos principalmente o dataframe do PNAD 2012 e outras informações externas, como classificação das classes sociais no Brasil, ranking das melhores regiões e definimos uma visão social pessimista porém muito realista em nosso meio, que seria a classificação do gênero e do sexo agrupados.
- Este site é um apêndice ao jogo desenvolvido pelos outros grupos do projeto final, com o objetivo de expor as dificuldades e privilégios da realidade social brasileira.
Este trabalho foi orientado pelo docente Pr. Dr. Fábio Macêdo Mendes.

## Método para cálculo do privilégio
### Analisamos a raça e o gênero em 4 diferentes níveis de porcentagem

- Mulher negra = 0%
- Homem negro = 33%
- Mulher branca = 66%
- Homem branco = 100%

### Analisamos a educação em 7 diferentes níveis de porcentagem

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

# Como rodar o site em sua máquina ?

Você deve ter o Python 3+* e o pipenv** instalado para rodar o site.

1º - Baixe ou clone o repositório

2º - Vá até o caminho do repositório, no caso, pelo terminal, o meu está localizado no Desktop

[Imgur](https://i.imgur.com/9caDnK6.png)

3º - Digite 'pipenv shell', o nome do ambiente virtual foi definido como shell

[Imgur](https://i.imgur.com/t8791qW.png)

4º - Digite 'pipenv install -r ./requirements.tt', este comando vai instalar todas as bibliotecas necessárias

[Imgur](https://i.imgur.com/r281BlS.png)

5º - Digite 'flask run', isso vai criar um servidor local para o site

[Imgur](https://i.imgur.com/EOMF1Ux.png)

6º - Entre no link que apareceu, este é o endereço do site.

Para sair do flask no terminal digite 'Ctrl+c'

Para desativar o ambiente virtual digite 'deactivate' 

*(Se utiliza o Windows, adicione o Python na PATH)
**(utilizamos um ambiente virtual para que não instale nada que o usuário não goste em sua máquina)

