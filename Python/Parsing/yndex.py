import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

# url страницы
urllist = ['https://pokupki.market.yandex.ru/product/sukhoi-korm-dlia-sterilizovannykh-koshek-bozita-s-iagnenkom-10-kg' \
      '/649568027?track=wishlist&show-uid=16119410193745615923106001&offerid=iAwx2k5NOfSJ_ffYk5dy1g',
      'https://www.wildberries.ru/catalog/12226932/detail.aspx?targetUrl=WL',
      'https://www.ozon.ru/context/detail/id/176331184/']

# fist prices
bestprice = [7647, 895, 795]

def wildberries(soup):
      """
      the price for Wildberries
      input: parsed string
      return: price
      """
      ourprice = soup.find_all('span', {'class': 'final-cost'})  # Получаем строку с ценой
      ourprice = str(ourprice).split()
      ourprice = int(ourprice[2])
      return ourprice

req = requests.get(urllist[1], headers={'User-Agent': UserAgent().random})  #отправляем HTTP запрос подставляя фэйковый запрос от хром
req.encoding = 'utf8'  # определяем кодировку
htmlString = req.text
soup = BeautifulSoup(htmlString)  # Отправляем полученную страницу в библиотеку для парсинга
#print(htmlString)
#rint(req)
#print(req.content)
#ourprice = str(ourprice).split(sep='\n')
ourprice = wildberries(soup)
print(ourprice)

# в цикле получим ответ страницы как она нас видит
# for key, value in req.request.headers.items():
#     print(key+": "+value)