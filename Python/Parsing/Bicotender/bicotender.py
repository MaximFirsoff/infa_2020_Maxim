"""
this function compares prices of the sites in list
"""
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import browsercookie
import time
import re
from datetime import datetime
from datetime import timedelta

list_of_tenders = []  # to get all tenders on the page
list_of_otrsl = [i for i in range(1, 25)]  # list of industrial branch
list_of_tenders_type = [i for i in range(1, 22)]  # list of tender's type
tender_days = 30  # period we need to get
# dictionary of industrial subbranches
dict_of_otrsl = {7: [1029, 1033, 1006, 1007, 1032, 1031, 1009, 1008, 1004, 1030],
                1: [1001, 1005, 1003, 1002],
                2: [1011, 1012, 1015, 1010, 1014, 1162, 1013],
                3: [1016, 1020, 1018, 1017, 1019],
                4: [1022, 1024, 1021, 1023],
                5: [1025],
                6: [1028, 1026, 1027],
                8: [1035, 1041, 1039, 1038, 1036, 1034, 1037, 1040],
                }


def getsoup(url):
    """
    get page from URL
    input: url - url
    return: html page
    """
    cj = browsercookie.firefox()  # get cookies from firefox
    req = requests.get(url, headers={'User-Agent': UserAgent().Firefox},
                       cookies=cj)  # отправляем HTTP запрос подставляя фэйковый куки
    req.encoding = 'utf8'  # определяем кодировку
    htmlstring = req.text
    soup = BeautifulSoup(htmlstring, 'html.parser')  # Отправляем полученную страницу в библиотеку для парсинга
    return soup


def element_of_tuple(split_name_one, split_name_two='>'):
    """
    this function was not useful
    """
    print(tr_of_data)
    name = str(tr_of_data).split(split_name_one)
    name = str(name[1]).split(split_name_two)
    return name


def tenderquantity():
    """
    control if quantity of tenders os more than 20
    """
    list_of_qu = soup.find_all('span', {'class': "note"})  # get number of found tenders
    if not list_of_qu:  # if no information about tender`s quantity
        list_of_qu = [0]
    num_of_tenders = str(list_of_qu[0]).replace(u'\xa0', '')  # get out non-breaking spaces
    num_of_tenders = re.findall(r'\d+', num_of_tenders)  # getting number from string
    num_of_tenders = int(num_of_tenders[0])
    if num_of_tenders > 20 and check_tender_num != tender_days:
        print(url)
        wait = input("in that url number of tenders is more then 20 second time press Enter to continue.")
        num_of_tenders = 0
    return num_of_tenders


def getnameoftender():
    """
    getting the name for therow of excel
    """
    name_of_tender = str(tr_list_of_data).split("Название")
    name_of_tender = str(name_of_tender[1]).split(">")
    name_of_tender = re.findall(r'[а-яА-Я]+', name_of_tender[1])  # get Russian letters only
    name_of_tender = " ".join(name_of_tender)
    return name_of_tender


def gettypeoftender():
    """
    getting type of the tender for the row of excel
    """
    type_of_tender = str(tr_list_of_data).split('Тип тендера')
    type_of_tender = str(type_of_tender[1]).split('>')
    type_of_tender = re.findall(r'[а-яА-Я]+', type_of_tender[1])  # get Russian letters only
    type_of_tender = " ".join(type_of_tender)
    return type_of_tender


def getpriceoftender():
    """
    getting price of the tender for the row of excel
    """
    price_of_tender = str(tr_list_of_data).split('Начальная цена')

    print(len(price_of_tender))

    if len(price_of_tender) > 1:  # if price exists
        price_of_tender = str(price_of_tender[1]).split('>')
        price_of_tender = re.findall(r'\d+', price_of_tender[2])  # getting number from string
        price_of_tender = "".join(price_of_tender)
    else:  # if no price
        price_of_tender = "не указано"

    return price_of_tender


def getperiod():
    """
    getting period of the tender for the row of excel
    """
    period = str(tr_list_of_data).split('Период показа')
    period = str(period[1]).split('>')
    periodfrom = re.findall(r'\d{2}.\d{2}.\d{4}', str(period[4]))  # getting date from string
    periodfrom = " ".join(periodfrom)
    periodto = re.findall(r'\d{2}.\d{2}.\d{4}', str(period[5]))  # getting date from string
    periodto = " ".join(periodto)
    return periodfrom, periodto


def getregion():
    """
    getting region of the tender for the row of excel
    """
    region = str(tr_list_of_data).split('Регион')
    region = str(region[1]).split('Отрасли')
    region = re.findall(r'[а-яА-Я]+', region[0])  # get Russian letters only
    region = " ".join(region)
    return region


def getbranchname():
    branchname = str(tr_list_of_data).split('Отрасли')
    branchname = str(branchname[1]).split('Отрасли')
    branchname = re.findall(r'[а-яА-Я]+', branchname[0])  # get Russian letters only
    branchname = " ".join(branchname)
    return branchname


def gettupleline():
    """
    get tuple from el of list of soup
    input: element of list of soup
    return: tuple of data
    """
    name_of_tender = getnameoftender()
    type_of_tender = gettypeoftender()
    price_of_tender = getpriceoftender()
    periodfrom, periodto = getperiod()
    region = getregion()
    branchname = getbranchname()

    return (name_of_tender, price_of_tender, periodto, type_of_tender, periodfrom, region, branchname)


resultFyle = open("output.csv", 'w')  # Open File
resultFyle.write("Наименование;Цена;До;Тип тендера;От;Регион;Отрасль\n")  # Write first row to file


check_tender_num = tender_days  # for if there is more than 20 tenders on the page we will use everyday cycle

check_type_of_tender = ""  # check-marker for escape cycle
type_of_tender = 1
while type_of_tender <= list_of_tenders_type[-1]:
#for type_of_tender in range(1, len(list_of_tenders_type)):

    check_industrial_otrasl = ""  # check-marker for escape cycle
    industial_otrasl = 1
    while industial_otrasl <= list_of_otrsl[-1]:
#    for industial_otrasl in range(1, len(list_of_otrsl)):

        dais_count = tender_days
        while dais_count > check_tender_num-1:  # for each day in period
 #       for dais_count in range(tender_days, check_tender_num-1, -1):  # for each day in period
            loaddate = (datetime.today() - timedelta(days=dais_count-1)).strftime('%d.%m.%Y')  # get string of load date
            print(dais_count)
            print(check_tender_num)
            print("industial_otrasl-", industial_otrasl)
            print("type_of_tender-", type_of_tender)
            if check_tender_num == tender_days and  dais_count == tender_days:
                loaddate = ""
            elif check_tender_num != tender_days and  dais_count == 1:
                check_tender_num = tender_days
                dais_count = tender_days
            print("Идет поиск за ", loaddate)
            url = "https://www.bicotender.ru/tender/search/?keywords=&no_search_by_positions=0&no_search_by_positions=1" \
                  "&keywordsStrict=0&nokeywords=&no_exclude_by_positions=0&no_exclude_by_positions=1" \
                  "&documentationKeywords=&nodocumentationKeywords=&region_id%5B%5D=4996&field_id%5B%5D={" \
                  "}&multifields=0&company%5Bname%5D=&company%5BexcludeName%5D=0&company%5BkeywordsStrict%5D=0&company" \
                  "%5Binn%5D=&costRub%5Bfrom%5D=&costRub%5Bto%5D=&costRub%5BwithZero%5D=0&prepaymentPercent%5Bfrom%5D" \
                  "=&prepaymentPercent%5Bto%5D=&loadTime%5Bfrom%5D={}&loadTime%5Bto%5D={}&finishDate%5Bfrom%5D=&finishDate" \
                  "%5Bto%5D=&status_id%5B%5D=3&type_id%5B%5D={" \
                  "}&sourceUrl=&excludeSourceUrl=0&tender_id=&srcNoticeNumber=&show_expiration=0&show_expiration=on" \
                  "&on_page=20&order=bcNewness+DESC&searchInFound=0&submit=Искать".format(industial_otrasl, loaddate,
                                                                                          loaddate, type_of_tender)
            soup = getsoup(url)  # get http page
            print(url)
            num_of_tenders = tenderquantity()  # check quantity of tenders on the page
            if num_of_tenders >20:  # if there is more than 20 tender on the page we go to everyday cycle

                check_tender_num = 1
 #               dais_count = 1
                continue


            list_of_data = soup.find_all('tr')  # get list of tenders

            for i in range(1, len(list_of_data) - 1):  # get data of tender
                tr_list_of_data = list_of_data[i]
                tupleline = gettupleline()
                print(tupleline)

                for r in tupleline:
                    resultFyle.write(r + ";")  # in cycle write data to file
                resultFyle.write(";\n")
            dais_count -= 1
        industial_otrasl += 1
    type_of_tender += 1

resultFyle.close()  # close File
