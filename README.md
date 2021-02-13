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
* Ative o virtualenv (windowns):
```
    .\.venv\Scripts\activate
```
* Instale as dependencias: 
```
    pip install -r requirements.txt \n
    python contrib/env_gen.py
```
* Rode as migrations:
```
    python manage.py migrate
```
* Criar usuario para acesso:
```
    python manage.py createsuperuser
```
* Rodar a aplicação:
```
    python manage.py runserver
```


## Rodando Jupyter notebook
* Instalando e rodando notebook :
```
    pip install ipython[notebook]
    python manage.py shell_plus --notebook
```

* Importe o arquivo note_imports com as configurações para usar o notebook
```
import note_imports
```


## Usando Makefile no windowns
* Instale GNU MAKE com o chocolatey
```
choco install make
```
* Usando os comandos make
```
make run
```

