"""
this function compares prices of the sites in list
"""
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import browsercookie
import pandas as pd
import time
import re

url = 'https://www.bicotender.ru/tender/search/?keywords=&region_id%5B%5D=4996&status_id%5B%5D=3&on_page=20&submit=найти'
list_of_tenders = []  # to get all tenders on the page
list_of_otrsl = [i for i in range(1, 24)]  # list of industrial branch
list_of_tenders_type = [i for i in range(1, 21)]  # list of tender's type


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
    htmlString = req.text
    soup = BeautifulSoup(htmlString, 'html.parser')  # Отправляем полученную страницу в библиотеку для парсинга
    return soup

def element_of_tuple(split_name_one, split_name_two = '>'):
    """
    this function was not useful
    """
    print(tr_of_data)
    name = str(tr_of_data).split(split_name_one)
    name = str(name[1]).split(split_name_two)
    return name


def gettupleline(list_of_data):
    """
    get tuple from el of list of soup
    input: element of list of soup
    return: tuple of data
    """

    name_of_tender = str(list_of_data).split("Название")
    name_of_tender = str(name_of_tender[1]).split(">")
    name_of_tender = re.findall(r'[а-яА-Я]+', name_of_tender[1])  # get Russian letters only
    name_of_tender = " ".join(name_of_tender)

    type_of_tender = str(list_of_data).split('Тип тендера')
    type_of_tender = str(type_of_tender[1]).split('>')
    type_of_tender = re.findall(r'[а-яА-Я]+', type_of_tender[1])  # get Russian letters only
    type_of_tender = " ".join(type_of_tender)

    price_of_tender = str(list_of_data).split('Цена')
    if len(price_of_tender) > 1:  # if price exists
        price_of_tender = str(price_of_tender[1]).split('>')
        price_of_tender = re.findall(r'\d+', price_of_tender[1])  # getting number from string
        price_of_tender = "".join(price_of_tender)
    else:  # if no price
        price_of_tender = "не указано"

    period = str(list_of_data).split('Период показа')
    period = str(period[1]).split('>')
    period = re.findall(r'\d{2}.\d{2}.\d{4}', str(period[5]))  # getting date from string
    period = " ".join(period)

    region = str(list_of_data).split('Регион')
    region = str(region[1]).split('Отрасли')
    region = re.findall(r'[а-яА-Я]+', region[0])  # get Russian letters only
    region = " ".join(region)

    branchname = str(list_of_data).split('Отрасли')
    branchname = str(branchname[1]).split('Отрасли')
    branchname = re.findall(r'[а-яА-Я]+', branchname[0])  # get Russian letters only
    branchname = " ".join(branchname)

    return (name_of_tender, type_of_tender, price_of_tender, period, region, branchname)

resultFyle = open("output.csv",'w')  # Open File
resultFyle.write("Наименование;Тип тендера;Цена;До;Регион;Отрасль\n")  # Write first row to file

for type_of_tender in range(1, len(list_of_tenders_type)):
    for industial_otrasl in range(1, len(list_of_otrsl)):
        url = "https://www.bicotender.ru/tender/search/?keywords=&no_search_by_positions=0&no_search_by_positions=1&keywordsStrict=0&nokeywords=&no_exclude_by_positions=0&no_exclude_by_positions=1&documentationKeywords=&nodocumentationKeywords=&region_id%5B%5D=4996&field_id%5B%5D={}&multifields=0&company%5Bname%5D=&company%5BexcludeName%5D=0&company%5BkeywordsStrict%5D=0&company%5Binn%5D=&costRub%5Bfrom%5D=&costRub%5Bto%5D=&costRub%5BwithZero%5D=0&prepaymentPercent%5Bfrom%5D=&prepaymentPercent%5Bto%5D=&loadTime%5Bfrom%5D=&loadTime%5Bto%5D=&finishDate%5Bfrom%5D=&finishDate%5Bto%5D=&status_id%5B%5D=3&type_id%5B%5D={}&sourceUrl=&excludeSourceUrl=0&tender_id=&srcNoticeNumber=&show_expiration=0&show_expiration=on&on_page=20&order=bcNewness+DESC&searchInFound=0&submit=Искать".format(industial_otrasl, type_of_tender)
        soup = getsoup(url)  # get http page
        list_of_data = soup.find_all('tr')  # get list of tenders


        for i in range(1, len(list_of_data)-1):  # get data of tender
            tupleline = gettupleline(list_of_data[i])
            print(tupleline)


            for r in tupleline:
                resultFyle.write(r + ";")  # Write data to file
            resultFyle.write(";\n")


resultFyle.close()  # close File


    #name = element_of_tuple('Название')
    #print(name)

    #for i in range(1, len(list_of_data)-2):
