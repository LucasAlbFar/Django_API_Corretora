[<img src="https://img.shields.io/badge/author-Lucas-yellow?style=flat-square"/>](https://github.com/LucasAlbFar)

# API Django REST Framework Corretora
Projeto desenvolvido para aplicar os conhecimentos do Django REST Framework.

## Resumo:
API que simula uma corretora de investimentos, podendo o client:
 * Cadastrar um ativo nas modalidades de renda fixa, renda variável e cripto moedas e seu preço de mercado;
 * Realizar uma aplicação ou resgate de um ativo;
 * Consultar saldo de investimentos, calculado atráves das movimentações de aplicações e regate;
 * Consultar ativos por tipo de modalidade;
 * Consultar a carteira de investimentos, contendo o ativo, o preço negociado e preço de mercado atual, a quantidade de ativos disponíveis na carteira e a performance (lucro/prejuízo) de acordo com o preço de mercado;

## Endpoints:
* /admin/ -> administração site
* /ativos/ -> cadastrar novo ativo e visualizar os investimentos disponíveis;
* /movimentacoes/ -> cadastrar uma transação de aplicação ou resgate de um ativo;
* /saldo/ -> visualizar o saldo de carteira;
* /carteira/ -> visualizar a carteira de investimentos;
* /tipo/<str:tipo>/ -> vusualizar os ativos por tipo de modalidade;
* /swagger/ -> documentação da API 
* /redoc/ -> documentação da API 

## Informações de ambiente:
* Django==3.2.5
* django-filter==2.4.0
* djangorestframework==3.12.4

## Contato:
<a href="https://www.linkedin.com/in/lucasalbfar/">![](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)</a>
<a href="https://github.com/LucasAlbFar">![](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)</a>



[<img src="https://img.shields.io/badge/LucasFaria-0A66C2?style=flat-square&logo=linkedin&logoColor=white" />](https://www.linkedin.com/in/lucasalbfar/)
[<img src="https://img.shields.io/badge/lucasalbfar@gmail.com-EA4335?style=flat-square&logo=Gmail&logoColor=white" />](mailto:lucasalbfarw@gmail.com)
