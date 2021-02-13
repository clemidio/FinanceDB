import timeit
import csv
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from transaction.models import Transaction
from asset.models import Asset
from nota.models import Nota
from datetime import datetime
from decimal import Decimal


def csv_to_list(filename: str) -> list:
    try:
        with open(filename, encoding="utf8") as csv_file:
            reader = csv.DictReader(csv_file, delimiter=',')
            csv_data = [line for line in reader]
        return csv_data
    except IOError:
        print("Error: File does not appear to exist.")


def delete_users():
    users = User.objects.exclude(username='admin')
    users.delete()


def delete_assets():
    asset = Asset.objects.all()
    asset.delete()


def delete_transactions():
    transaction = Transaction.objects.all()
    transaction.delete()


def delete_notas():
    nota = Nota.objects.all()
    nota.delete()


def valid_num(num):
    try:
        val = float(str(num).replace(',', '.'))  # Decimal()
    except ValueError:
        val = '0'
    return val


def valid_nota(nota, date):
    try:
        nota = Nota.objects.get(n_nota=nota)
        print(nota, 'ja existe no banco de dados')
    except Nota.DoesNotExist:
        nota = Nota.objects.create(account_name=nota, n_nota=nota, date=date)
        print(nota, 'Foi criado com sucesso')
    return nota


def valid_asset(asset_in):
    try:
        asset = Asset.objects.get(sigla=asset_in)
        print(asset, 'ja existe no banco de dados')
    except Asset.DoesNotExist:
        asset = Asset.objects.create(sigla=asset_in)
        print(asset, 'Foi criado com sucesso')
    return asset


def valid_date(date_in):
    date = datetime.strptime(date_in, '%d/%m/%Y').strftime('%Y-%m-%d')
    print(date)
    return date


def save_transactions(data):
    '''
    Salva os dados no banco
    '''
    aux = []
    for item in data:
        print(item)
        asset = valid_asset(item.get('asset'))
        date = valid_date(item.get('date'))
        operation = item.get('operation')
        amount = valid_num(item.get('qtd'))
        price = valid_num(item.get('price'))  # Decimal(price.replace(',','.'))
        commission = valid_num(item.get('commission'))
        bank = item.get('account_bank')
        nota = valid_nota(bank, date)

        transaction = dict(
            asset=asset,
            date=date,
            operation=operation,
            amount=amount,
            price=price,
            commission=commission,
            nota_id=nota,
            account_bank=bank
        )
        # import ipdb
        # ipdb.set_trace()
        print(transaction)
        try:
            r = Transaction.objects.create(**transaction)
            print(r, 'inserido com sucesso!!')
        except Transaction.DoesNotExist:
            print('Não foi possivel criar transação: ', r)
    #   aux.append(obj)
    # Transaction.objects.bulk_create(aux)


def save_assets(data):
    for item in data:
        print(item)
        sigla = item.get('sigla')
        # import ipdb
        # ipdb.set_trace()
        try:
            asset = Asset.objects.get(sigla=sigla)
            print(asset, 'ja existe no banco de dados')
            asset.symbol = item.get('symbol')
            asset.name = item.get('name')
            asset.isin = item.get('isin')
            asset.classe = item.get('classe')
            asset.market_cod = item.get('market_cod')
            asset.market = item.get('market')
            asset.price = valid_num(item.get('price'))
            asset.setor = item.get('setor')
            asset.subsetor = item.get('subsetor')
            asset.segmento = item.get('segmento')
            asset.codcvm = item.get('codcvm')
            asset.cnpj = item.get('cnpj')
            asset.razao_social = item.get('razao_social')
            asset.cnpj_adm = item.get('cnpj_adm')
            asset.razao_social_adm = item.get('razao_social_adm')
            asset.save()
            # asset.objects.update(**data)
            print('atualizando registro', asset)
        except Asset.DoesNotExist:
            print(sigla)
            data = dict(
                sigla=sigla,
                symbol=item.get('symbol'),
                name=item.get('name'),
                isin=item.get('isin'),
                classe=item.get('classe'),
                market_cod=item.get('market_cod'),
                market=item.get('market'),
                price=valid_num(item.get('price')),
                setor=item.get('setor'),
                subsetor=item.get('subsetor'),
                segmento=item.get('segmento'),
                codcvm=item.get('codcvm'),
                cnpj=item.get('cnpj'),
                razao_social=item.get('razao_social'),
                cnpj_adm=item.get('cnpj_adm'),
                razao_social_adm=item.get('razao_social_adm')
            )
            asset = Asset.objects.create(**data)
            print(asset, 'Foi criado com sucesso')

    #   aux.append(obj)
    # Transaction.objects.bulk_create(aux)


class Command(BaseCommand):
    help = ''' Importa os dados. '''

    def handle(self, *args, **kwargs):
        tic = timeit.default_timer()
        # print('Limpamdo dados do banco de dados')
        # delete_assets()
        # delete_transactions()
        # delete_notas()
        # print('Lendo dados do arquivo csv')
        # data = csv_to_list('media/csv_imports/assets2.csv')
        # # print(data)
        # print('Salvando dados no banco de dados')
        # save_assets(data)
        data = csv_to_list('media/csv_imports/transactions.csv')
        # print(data)
        save_transactions(data)
        toc = timeit.default_timer()
        print('time:', toc - tic)
