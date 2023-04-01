import requests
from bs4 import BeautifulSoup
import pandas as pd


url = "https://www.fundamentus.com.br/fii_resultado.php"

headers = {
    'User-Agent'      : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'Accept'          : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language' : 'en-US,en;q=0.5',
    'DNT'             : '1', 
    'Connection'      : 'close'
}

data = requests.get(url, headers=headers, timeout=5).text
soup = BeautifulSoup(data,"html.parser")

table = soup.find('table')

df = pd.DataFrame(columns=['Papel', "Segmento", "Cotação", "FFO Yield", "Dividend Yield", "P/VP", "Valor de Mercado", "Liquidez", "Qtd de imóveis", "Preço do m2", "Aluguel por m2", "Cap Rate", "Vacância Média"])

for row in table.tbody.find_all('tr'):
    columns = row.find_all('td')
    if (columns != []):
        Papel = columns[0].text.strip(' ')
        Segmento = columns[1].text.strip(' ')
        Cotacao = columns[2].text.strip(' ')
        FFOYield = columns[3].text.strip(' ')
        DividendYield = columns[4].text.strip(' ')
        P_VP = columns[5].text.strip(' ')
        ValordeMercado = columns[6].text.strip(' ')
        Liquidez = columns[7].text.strip(' ')
        Qtddeimoveis = columns[8].text.strip(' ')
        Precodom2 = columns[9].text.strip(' ')
        Aluguelporm2 = columns[10].text.strip(' ')
        CapRate = columns[11].text.strip(' ')
        VacanciaMedia = columns[12].text.strip(' ')
        df = pd.concat([df,pd.DataFrame.from_records([{'Papel': Papel, 'Segmento': Segmento, 'Cotação': Cotacao, 'FFO Yield': FFOYield, 'Dividend Yield': DividendYield, 'P/VP': P_VP, 'Valor de Mercado': ValordeMercado, 'Liquidez': Liquidez, 'Qtd de imóveis': Qtddeimoveis, 'Preço do m2': Precodom2, 'Aluguel por m2': Aluguelporm2, 'Cap Rate': CapRate, 'Vacância Média': VacanciaMedia}])],ignore_index=True)
    df.head(389)


cont = 0
for i in df['Papel']:
    print(f'{cont:^3} - {i:^10}', end=' | ')
    cont = cont + 1
    if cont % 5 == 0:
        print('\n', end='')


fundo1 = df.loc[229]  
fundo2 = df.loc[368]  
fundo3 = df.loc[388]  
print()
print('-='*17)
print(fundo1)       
print('-='*17)      
print(fundo2)       
print('-='*17)
print(fundo3)
print('-='*17)