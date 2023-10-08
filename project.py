from bs4 import BeautifulSoup
import requests
import csv
from datetime import datetime
import sys

def main():
    online_database = []
    try:
        database_csv = get_data_segmentos()
        for item in database_csv:
            if item[1] != "REAL ESTATE FUNDS":
                type = "acoes"
            else:
                type = "fundos-imobiliarios"
            online_database.append(get_data_online(type, item[0], item[1]))
    except:
        sys.exit("Was not possible to get list of actions")

    try:
        save_data(online_database)
    except:
         sys.exit("Error saving data")


def get_data_segmentos():
    db = []
    with open('data_to_search.csv', 'r') as f:
        data = csv.reader(f)
        next(data)  # Pular a primeira linha
        for linha in data:
            db.append(linha)
    return db


def get_data_online(type, action, segment):
    url = f"https://statusinvest.com.br/{type}/{action}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"}

    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')

    get_compania = soup.find("header", id="main-header")
    compania = str(get_compania.get_text()).strip().split('\n')
    if compania == None:
        return [action, "Not found"]

    compania_name = compania[7]

    get_ativo = soup.find("div", title="Valor atual do ativo")
    valor_ativo = str(get_ativo.get_text()).strip().split('\n')
    ativo_preco = valor_ativo[2]

    get_dividend = soup.find("div", title="Dividend Yield com base nos últimos 12 meses")
    valor_dividend = str(get_dividend.get_text()).strip().split('\n')
    dividend_percent = valor_dividend[-2]

    get_codigo_datas = soup.find("div", class_="list-content")
    filtro = str(get_codigo_datas).strip().split('\n')
    for i in filtro:
        if '<div style="min-height:' in i:
            codigo = i.split('"')

    get_datas = soup.find("div", style=codigo[1])

    if get_datas == None:
        return [type, compania_name, action.upper(), ativo_preco, dividend_percent]

    datas_compac = str(get_datas.get_text()).strip().split('\n')
    if datas_compac[11] == "Não há histórico de proventos para este ativo":
        return [type, compania_name, action.upper(), ativo_preco, dividend_percent]
    else:
        data_com = datas_compac[11]
        data_pag = datas_compac[12]
        valor_pag = datas_compac[13]

    hora = str(datetime.now())
    pacote = [action.upper(), segment, compania_name, ativo_preco, dividend_percent, data_com, data_pag, valor_pag, hora[:-7]]
    return pacote


def save_data(database):
    with open('online_action.csv', 'w', encoding='utf8', newline='') as f:
        thewriter = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        header = ['INVESTIMENT','GROUP','COMPANY','CURRENT VALUE (R$)','DIVIDEND YIELD %','DATE COM','DATE OF PAYMENT','VALUE OF PAYMENT (R$)','DATE/TIME']
        thewriter.writerow(header)
        for row in database:
            thewriter.writerow(row)


if __name__ == "__main__":
    main()