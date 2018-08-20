from pathlib import Path
import json
from datetime import datetime
from colors import *

def converter_data(data):
    return datetime.strptime(data, '%Y-%m-%d')

def obter_quantidade_de_dias_desde_de(data):
    return (datetime.today() - data).days

def exibir_linha_com_informacoes(nome_do_vicio, inicio_da_abstinencia):
    data_do_inicio = converter_data(inicio_da_abstinencia)
    quantidade_de_dias = obter_quantidade_de_dias_desde_de(data_do_inicio)
    print(color(f'{nome_do_vicio} - {quantidade_de_dias} days without', fg='yellow'))


CAMINHO_DO_ARQUIVO_DE_CONFIGURACAO = f'{Path.home()}/.novice/vices'
vicios = json.loads(open(CAMINHO_DO_ARQUIVO_DE_CONFIGURACAO).read())

print(color('YOUR VICE CONTROL', fg='green'))
print('=' * 25)
for vicio, data in vicios.items():
    exibir_linha_com_informacoes(vicio, data)
print('')