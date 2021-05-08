# FinanceDB
Aplicação para controle de finanças


## Como rodar o projeto 

* Clone o repositorio:
```
    git clone https://github.com/clemidio/FinanceDB.git
```
* Crie um virtualenv com python:
```
    python3 -m venv .venv
```
* Ative o virtualenv (windowns):
```
    source .venv/bin/activate (.\.venv\Scripts\activate)
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

## Rodando serviços com docker
* build e Up das imagens dev (prod) :
```
    docker-compose up -d --build
    (docker-compose -f docker-compose.prod.yml up -d --build)
```
* desmontando imagens e volumes associados dev (prod)  :
```
     docker-compose down -v
     (docker-compose -f docker-compose.prod.yml down -v)
```
* lendo logs do container :
```
     docker-compose -f docker-compose.prod.yml logs -f
```
docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
docker-compose  exec web python manage.py createsuperuser
docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear

* acessando database :
```
    docker-compose exec db psql --username=postgres --dbname=postgres
    \l 
    \c name
    \dt
    \q
```
* verificando volume do banco de dados :
```
    docker volume inspect 'project'_postgres_data
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

## Implementações

- Cadastro de Ativos, Transações e Notas
- Login/Logout
- Criação de perfil para cada usuário.


## Referências

- [Google Fonts](https://fonts.google.com/)
- [meterializecss](https://materializecss.com/icons.html) 
- [Material Design Icons](https://google.github.io/material-design-icons)
- [startbootstrap](https://startbootstrap.com/theme/sb-admin-2)


- [django no docker + postgres + bunicorn + nginx](https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/)
- [DjangoSIGE](https://github.com/thiagopena/djangoSIGE)
- [AdminBSBMaterialDesign](https://github.com/gurayyarar/AdminBSBMaterialDesign)
- [geraldo](https://github.com/marinho/geraldo)
- [jQuery-Mask-Plugin](https://igorescobar.github.io/jQuery-Mask-Plugin/)
- [DataTables](https://datatables.net/)
- [JQuery multiselect](http://loudev.com/)


## Ajuda

Para relatar bugs ou fazer perguntas utilize o [Issues](https://github.com/clemidio/FinanceDB) ou via email clemidiovieira@gmail.com