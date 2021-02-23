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
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# for e-mailing
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

try:
    file = 'shops.xls'  # get file with data
    xl = pd.ExcelFile(file)  # make a DataFrame
    dfexcel = xl.parse('Лист1')  # parse Sheet1
except FileNotFoundError:  # if no the file
    print("""there must be the file "shop.xls" somewhere""")

mustmodul = 'modulrequest'  # module we will use to get page

def mailsend():
    """
      sending e-mail
      """
    # create message object instance
    msg = MIMEMultipart()

    message = "Thank you"

    # setup the parameters of the message
    password = ""
    msg['From'] = "nixtaganrog@mail.ru"
    msg['To'] = "mfirsoff@mail.ru"
    msg['Subject'] = "Subscription"

    # add in the message body
    msg.attach(MIMEText(message, 'plain'))

    # create server
    server = smtplib.SMTP('smtp.mail.ru: 465')

    server.starttls()

    # Login Credentials for sending the mail
    server.login(msg['From'], password)

    # send the message via the server.
    server.sendmail(msg['From'], msg['To'], msg.as_string())

    server.quit()

    print
    "successfully sent email to %s:" % (msg['To'])


def wildberries(soup):
    """
      the price for Wildberries
      input: parsed string
      return: price
      """
    ourprice = soup.find('span', {'class': 'final-cost'})  # Получаем строку с ценой
    ourprice = str(ourprice).replace(u'\xa0', '')  # getout non-breaking spaces
    ourprice = str(ourprice).split()  # split the string
    ourprice = str(ourprice[2])[:-1]  # getting element without last symbol
    ourprice = int(ourprice)  # get our price as number

    return ourprice


def ozon(soup):
    """
      the price for Ozon
      input: parsed string
      return: price
      """
    # Получаем строку с ценой for both "c8q7" and "c8q7 c8q8" classes
    ourprice = soup.find_all('span', {'class': re.compile("(c8q7|c8q8)")})
    ourprice = str(ourprice).replace(u'\xa0', '')  # getout non-breaking spaces
    ourprice = str(ourprice).split('>')
    ourprice = re.findall(r'\d+', str(ourprice[2]))  # getting number from string
    ourprice = int(ourprice[0])
    return ourprice


def pokupkiyandex(soup):
    """
      the price for Yandex
      input: parsed string
      return: price
      """
    ourprice = soup.find_all('span', {'data-tid': 'c3eaad93'})  # Получаем строку с ценой
    ourprice = str(ourprice).replace(' ', '')  # delete all spaces
    ourprice = str(ourprice).split('>')
    ourprice = str(ourprice[1]).split('<')
    ourprice = int(ourprice[0])
    return ourprice


def yandex(soup):
    """
      the price for Yandex
      input: parsed string
      return: price
      """
    ourprice = soup.find_all('div', {'data-tid': '23fad448'})  # Получаем строку с ценой
    ourprice = str(ourprice).replace(' ', '')  # delete all spaces
    ourprice = str(ourprice).split('>')
    ourprice = re.findall(r'\d+', str(ourprice[3]))  # getting number from string
    ourprice = int(ourprice[0])
    return ourprice


def petshop(soup):
    """
      the price for Petshop
      input: parsed string
      return: price
      """
    ourprice = soup.find_all('span', {'data-testid': 'Price__val'})  # Получаем строку с ценой
    ourprice = str(ourprice[3]).replace(' ', '')  # delete all spaces
    ourprice = re.findall(r'\d+', ourprice)  # getting number from string
    ourprice = int(ourprice[0])
    return ourprice


def getallcookies():
    """
    make cookies for selenium
    """
    cookieslist = str(cj).replace('<CookieJar[<Cookie ', '')  # replace sting
    cookieslist = str(cookieslist).replace('>]>', '')  # replace sting
    cookieslist = cookieslist.split('>, <Cookie ')  # splitting by '>, <Cookie '
    # splitting by '=", " for ' and "/" to get for each element
    cookieslist = list(map(lambda x: re.split('=| for |/', x), cookieslist))
    return cookieslist


def addcookies():
    """
    adding all cookies for selenium
    """
    for onecooky in cookieslist:
        driver.add_cookie({'name': onecooky[0], 'value': onecooky[1], 'path': '/'+onecooky[3]})

def modulselenium():
    """
    return page of site by Selenium
    """
    oururl = dfexcel.iloc[i]['URL']
    driver.get(oururl)
    addcookies()
    driver.get(oururl)
    return driver.page_source


def modulrequest():
    """
    return page of site by Request
    """
    req = requests.get(dfexcel.iloc[i]['URL'], headers={'User-Agent': UserAgent().Firefox},
                       cookies=cj, stream=True)  # отправляем HTTP запрос подставляя фэйковый куки
    req.encoding = 'utf8'  # определяем кодировку
    return req.text


# mailsend()

for i in range(0, len(dfexcel)):  # for each row in Excel file
    ourprice = 0
    if mustmodul == 'modulselenium':  # if we used Selenium previously
        driver.close()
        mustmodul = 'modulrequest'  # module we will use to get page

    while ourprice == 0:  # if cookies is old and function get error we signaling about it and cycle
        cj = browsercookie.firefox()  # get cookies from firefox
        try:
            htmlString = locals()[mustmodul]()  # start modul - nor 'modulselenium' or 'modulrequest'
            soup = BeautifulSoup(htmlString, 'html.parser')  # Отправляем полученную страницу в библиотеку для парсинга

            if dfexcel.iloc[i]['Site'] == dfexcel.iloc[i - 1]['Site']:  # if same site again waiting because blocks
                time.sleep(3)

            ourprice = locals()[dfexcel.iloc[i]['Site']](soup)  # get function from string
            print(ourprice)

            if ourprice < dfexcel.iloc[i]['Price']:  # if price decrease
                print('In ', dfexcel.iloc[i]['URL'], ' \n is price decreased \n was ',
                      dfexcel.iloc[i]['Price'], '\n now ', ourprice)
                wait = input("Press Enter to continue.")
                print('Please wait')

        # в цикле получим ответ страницы как она нас видит
        # for key, value in req.request.headers.items():
        #     print(key+": "+value)

        except IndexError:  # if got ban
            if mustmodul == 'modulselenium':  # if we do not get the price both modules
                driver.close()
                print('The Site blocks Your cookies. You need open Firefox and go by link')
                print(dfexcel.iloc[i]['URL'])
                print('Enter the captcha')
                wait = input("And press Enter to continue after that.")
                print('Please wait')
                temporarycookies =  browsercookie.firefox()  # get cookies from firefox
                while temporarycookies == cj:  # the cookies do not new in the moment
                    temporarycookies = browsercookie.firefox()  # get cookies again
                cj = temporarycookies  # new cookies
                mustmodul = 'modulrequest'
            else:  # if we do not fet the price Request module we try Selenium module
                print('Module Request is not working. Trying Selenium module.')
                print('Please wait')
                mustmodul = 'modulselenium'
                options = Options()  # for hiden Firefox
                options.headless = True  # for hiden Firefox
                driver = webdriver.Firefox(options=options)  # Delenium driver
                cookieslist = getallcookies()  # split cookies to JSON

            # print(cj)

if mustmodul == 'modulselenium':  # if geckodriver.exe is open, close it
    driver.close()
