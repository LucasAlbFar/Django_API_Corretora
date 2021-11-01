[<img src="https://img.shields.io/badge/author-Lucas Faria-yellow?style=flat-square"/>](https://github.com/LucasAlbFar)

# API Django REST Framework Corretora

API que simula uma corretora de investimentos, permitindo ao client:
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
[requirements.txt](https://github.com/LucasAlbFar/Django_REST_FRAMEWORK_API_Corretora/blob/main/requirements.txt)

## Contato:
[<img src="https://img.shields.io/badge/LucasFaria-0A66C2?style=flat-square&logo=linkedin&logoColor=white" />](https://www.linkedin.com/in/lucasalbfar/)
[<img src="https://img.shields.io/badge/lucasalbfar@gmail.com-EA4335?style=flat-square&logo=Gmail&logoColor=white" />](mailto:lucasalbfarw@gmail.com)
