# Page To PDF

Função simples e grosseira para gerar PDF a partir de uma página web. :smile:

# Estrutura

O projeto é gerenciado pelo [Serverless Framework](https://www.serverless.com/), usando Python, pelos seguintes motivos:
- Serverless não nos deixa presos à AWS;
- Utiliza AWS Lambda, permitindo uma escala gigantesca;
- Python é a linguagem com melhor performance na plataforma Lamda;

A lib `pdfkit` é utilizada (ainda que não mais mantida) por ser compatível com a lib de mesmo nome para Ruby, sendo assim, não ficamos presos nem ao Python.

## Instalação de dependências

### Serverless

Será necessário instalar o Serverless Framework, [pelo link acima](#estrutura).

### Node

Na raiz do projeto, execute:
```sh
npm install
```

### Python

#### Tradicional

Com o python e pip instalados:
```sh
pip install -r requirements.txt
```

#### Com pipenv

Para instalar todas as dependências, instale o [pipenv](https://pipenv-fork.readthedocs.io/), seguindo as instruções para seu sistema operacional, depois, na pasta do projeto, rode um `pipenv install` e estará pronto!

## Desenvolvimento local

Após instalar as dependências, utilizar o comando `sls offline` com a porta 3000 livre e utilizar curl ou semelhante:
```sh
curl http://localhost:3000/production/pdf
```

## Rodar testes

Instale o `pytest` com o comando `pip install -U pytest` (caso use pipenv, só usar um `pipenv install`).

Utilize o comando `pytest` na raiz do projeto para rodar os testes.

## Fazer deploy
Na raiz do projeto, execute o comando `make` ou `make deploy` e pronto.

## Fazer deploy em novo ambiente
Basta editar o `serverless.yml` conforme necessário, baixar as dependências.

**Caso queira mudar o nome do serviço, ou domínio, execute:**
```sh
sls create_domain
```

## Dúvidas? Bugs? Raiva? Feedback?
ulissescaon@gmail.com