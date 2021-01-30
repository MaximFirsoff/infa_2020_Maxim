import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import browsercookie
# for e-mailing
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# url страницы
urllist = ['https://pokupki.market.yandex.ru/product/sukhoi-korm-dlia-sterilizovannykh-koshek-bozita-s-iagnenkom-10-kg' \
      '/649568027?track=wishlist&show-uid=16119410193745615923106001&offerid=iAwx2k5NOfSJ_ffYk5dy1g',
      'https://www.wildberries.ru/catalog/12226932/detail.aspx?targetUrl=WL',
      'https://www.ozon.ru/context/detail/id/176331184/']

# fist prices
bestprice = [7647, \
             895, \
             795]


def mailsend():
      """
      sending e-mail
      """
      # create message object instance
      msg = MIMEMultipart()

      message = "Thank you"

      # setup the parameters of the message
      password = "SoloTres12"
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
      ourprice = str(ourprice).split()  # split the string
      ourprice = int(ourprice[2])  # get our price as number
      return ourprice

def ozon(soup):
      """
      the price for Ozon
      input: parsed string
      return: price
      """
      ourprice = soup.find_all('span', {'class': 'c8q7 c8q8'})  # Получаем строку с ценой
      ourprice = str(ourprice).split()
      ourprice = str(ourprice[4]).split('>')
      ourprice = int(ourprice[1])
      return ourprice


def yandex(soup):
      """
      the price for Yandex
      input: parsed string
      return: price
      """
      ourprice = soup.find_all('span', {'data-tid': 'c3eaad93'})  # Получаем строку с ценой
      ourprice = str(ourprice).replace(' ', '')
      # ourprice = ourprice.split()
      ourprice = str(ourprice).split('>')
      ourprice = str(ourprice[1]).split('<')
      ourprice = int(ourprice[0])
      return ourprice


#mailsend()

for i in range(len(urllist)):

      cj = browsercookie.firefox()  # get cookies from firefox
      req = requests.get(urllist[i], headers={'User-Agent': UserAgent().random}, cookies=cj)  #отправляем HTTP запрос подставляя фэйковый запрос
      req.encoding = 'utf8'  # определяем кодировку
      htmlString = req.text
      soup = BeautifulSoup(htmlString)  # Отправляем полученную страницу в библиотеку для парсинга
      #print(htmlString)
      #print(req)
      #print(req.content)
      #ourprice = str(ourprice).split(sep='\n')

      if i == 0:
            ourprice = yandex(soup)
      elif i == 1:
            ourprice = wildberries(soup)
      elif i == 2:
            ourprice = ozon(soup)

      #print(cj)

      print(ourprice)

      # if ourprice < bestprice[0]:
      #       print('In ', urllist[0], ' \n is price decreasing \n was ', bestprice[0], '\n now ', ourprice)


      # в цикле получим ответ страницы как она нас видит
      # for key, value in req.request.headers.items():
      #     print(key+": "+value)