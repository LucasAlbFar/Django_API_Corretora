[<img src="https://img.shields.io/badge/author-Lucas Faria-yellow?style=flat-square"/>](https://github.com/LucasAlbFar)

# Django REST Framework Brokerage API

API that simulates an investment brokerage, allowing the client to:
* Register an asset in fixed income, variable income and cryptocurrencies and its market price;
* Make an application or redemption of an asset;
* Consult the balance of investments, calculated through the movement of applications and redemption;
* Consult assets by type of modality;
* Consult the investment portfolio, containing the asset, the traded price and current market price, the quantity of assets available in the portfolio and the performance (profit/loss) according to the market price;

## Endpoints:
* admin/ -> site administration
* /assets/ -> register a new asset and view the available investments;
* /movimentacoes/ -> register a transaction of application or redemption of an asset;
* /balance/ -> view the portfolio balance;
* /portfolio/ -> view the investment portfolio;
* /type/str:type/ -> view assets by type of modality;
* /swagger/ -> API documentation
* /redoc/ -> API documentation

## Environment information::
[requirements.txt](https://github.com/LucasAlbFar/Django_REST_FRAMEWORK_API_Corretora/blob/main/requirements.txt)

## Contact:
[<img src="https://img.shields.io/badge/LucasFaria-0A66C2?style=flat-square&logo=linkedin&logoColor=white" />](https://www.linkedin.com/in/lucasalbfar/)
[<img src="https://img.shields.io/badge/lucasalbfar@gmail.com-EA4335?style=flat-square&logo=Gmail&logoColor=white" />](mailto:lucasalbfarw@gmail.com)
