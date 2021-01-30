# FinanceDB
Aplicação para controle de finanças


## Como rodar o projeto 

* Clone o repositorio:
```
    git clone https://github.com/clemidio/FinanceDB.git
```
* Crie um virtualenv com python:
```
    python -m venv .venv
```
* Ative o virtualenv:

* Instale as dependencias: \n
```
    pip install -r requirements.txt \n
    python contrib/env_gen.py
```
* Rode as migrations:
```
    python manage.py migrate
```
